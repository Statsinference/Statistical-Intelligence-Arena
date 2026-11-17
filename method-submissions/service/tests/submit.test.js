import test from 'node:test';
import assert from 'node:assert/strict';
import {DOMAINS, createHandler, normalizeModelURL, readList, emptyList} from '../api/submit.js';
const REPO='Statsinference/stats-inference-arena';
const URL='https://huggingface.co/Brownight/tabpfn-iv-adapter-v0.3';
const API='https://api.github.com/repos/'+REPO;
const env={SUBMISSIONS_ENABLED:'true',GITHUB_SUBMISSIONS_TOKEN:'unit-test-only'};
const timestamp=new Date('2026-11-17T03:00:00.000Z');
const response=(status,data)=>new Response(JSON.stringify(data),{status,headers:{'Content-Type':'application/json'}});
function storage() {
 const state={files:new Map(),calls:[],writes:0,conflicts:0,deny:false,repo:{id:1426616721,full_name:REPO,private:true}};
 state.fetch=async(url,opt={})=>{
  state.calls.push({url,...opt});
  if(url===API)return response(200,state.repo);
  assert.ok(url.startsWith(API+'/contents/method-submissions/received/'));
  const path=new globalThis.URL(url).pathname.split('/contents/')[1];
  assert.match(path,/^method-submissions\/received\/[a-z_]+\/README\.md$/);
  if(opt.method!=='PUT'){
   const f=state.files.get(path);return f?response(200,{type:'file',path,encoding:'base64',sha:f.sha,size:Buffer.byteLength(f.text),content:Buffer.from(f.text).toString('base64')}):response(404,{});
  }
  if(state.deny)return response(403,{});
  if(state.conflicts>0){state.conflicts--;return response(409,{});}
  const p=JSON.parse(opt.body), old=state.files.get(path);
  assert.equal(p.branch,'main');
  if((old?.sha||undefined)!==p.sha)return response(409,{});
  state.writes++;const sha=state.writes.toString(16).padStart(40,'0');
  state.files.set(path,{sha,text:Buffer.from(p.content,'base64').toString('utf8')});
  return response(old?200:201,{content:{path},commit:{sha}});
 };
 return state;
}
function handler(s,options={}){return createHandler({env,fetchImpl:s.fetch,now:()=>timestamp,sleep:async()=>{},...options});}
async function call(h,body={domain:'iv',huggingface_url:URL},overrides={}){
 const req={method:'POST',headers:{origin:'https://statsinference.github.io','content-type':'application/json','x-arena-submission':'1','x-real-ip':'127.0.0.1'},body,...overrides};
 const res={headers:{},setHeader(k,v){this.headers[k]=v;},end(v){this.raw=v;this.body=v?JSON.parse(v):null;}};
 await h(req,res);return res;
}
test('normalizes only supported model links',()=>{
 assert.equal(normalizeModelURL(URL+'/'),URL);
 assert.equal(normalizeModelURL(URL+'/tree/main'),URL+'/tree/main');
 for(const u of ['http://huggingface.co/a/b','https://evil.com/a/b','https://huggingface.co@evil.com/a/b','https://huggingface.co/a/b?token=x','https://huggingface.co/a/../b','https://huggingface.co/datasets/a','https://huggingface.co/spaces/a','https://huggingface.co/a/%62',123])assert.equal(normalizeModelURL(u),null,u);
});
for(const domain of Object.keys(DOMAINS))test('persists to only the '+domain+' list',async()=>{
 const s=storage(),r=await call(handler(s),{domain,huggingface_url:URL});
 assert.equal(r.statusCode,201);assert.equal(s.writes,1);
 assert.deepEqual(readList(s.files.get(`method-submissions/received/${domain}/README.md`).text,domain),[{url:URL,time:timestamp.toISOString(),receipt:r.body.receipt}]);
 assert.ok(!s.calls.some(c=>c.url.includes('/issues')));
 assert.equal(r.headers['Access-Control-Allow-Origin'],'https://statsinference.github.io');
});
test('does not require a private repository or submitter login',async()=>{
 const s=storage();s.repo.private=false;
 assert.equal((await call(handler(s))).statusCode,201);
});
test('duplicates have the same receipt and do not create another commit',async()=>{
 const s=storage(),h=handler(s),a=await call(h),b=await call(h);
 assert.equal(b.statusCode,200);assert.equal(a.body.receipt,b.body.receipt);assert.equal(b.body.duplicate,true);assert.equal(s.writes,1);
});
test('retries after a concurrent SHA conflict',async()=>{
 const s=storage();s.conflicts=1;assert.equal((await call(handler(s))).statusCode,201);assert.equal(s.writes,1);
});
test('concurrent submissions retain both model links',async()=>{
 const s=storage(),h=handler(s);
 const results=await Promise.all([call(h),call(h,{domain:'iv',huggingface_url:'https://huggingface.co/other/model'})]);
 assert.deepEqual(results.map(r=>r.statusCode),[201,201]);
 assert.equal(readList(s.files.get('method-submissions/received/iv/README.md').text,'iv').length,2);
});
test('rejects unknown domain, subdomain, destination overrides and honeypot',async()=>{
 for(const body of [{domain:'__proto__',huggingface_url:URL},{domain:'../data',huggingface_url:URL},{domain:'iv',huggingface_url:URL,subdomain:'late'},{domain:'iv',huggingface_url:URL,path:'README.md'},{domain:'iv',huggingface_url:URL,website:'spam'},{huggingface_url:URL}]){
  const s=storage();assert.equal((await call(handler(s),body)).statusCode,400);assert.equal(s.calls.length,0);
 }
});
test('failed storage writes never return success',async()=>{
 const s=storage();s.deny=true;const r=await call(handler(s));assert.equal(r.statusCode,503);assert.equal(r.body.ok,false);assert.equal(s.writes,0);
});
test('malformed existing file is never overwritten',async()=>{
 const s=storage();s.files.set('method-submissions/received/iv/README.md',{sha:'a'.repeat(40),text:'# Owner notes\nDo not replace'});
 assert.equal((await call(handler(s))).statusCode,503);assert.equal(s.writes,0);
});
test('wrong repository metadata prevents all writes',async()=>{
 const s=storage();s.repo.id=1;assert.equal((await call(handler(s))).statusCode,503);assert.equal(s.writes,0);
});
test('missing credentials fail closed without network calls',async()=>{
 const s=storage();assert.equal((await call(handler(s,{env:{}}))).statusCode,503);assert.equal(s.calls.length,0);
});
test('health reports configuration only',async()=>{
 const s=storage();const r=await call(handler(s,{env:{}}),{}, {method:'GET',headers:{}});
 assert.deepEqual(r.body,{ok:true,configured:false});assert.equal(s.calls.length,0);
});
test('JSON, size, origin and preflight rules',async()=>{
 const s=storage(),h=handler(s);
 assert.equal((await call(h,{}, {headers:{origin:'https://evil.test'}})).statusCode,403);
 assert.equal((await call(h,{}, {headers:{origin:'https://statsinference.github.io','content-type':'text/plain','x-arena-submission':'1'}})).statusCode,415);
 assert.equal((await call(h,{domain:'iv',huggingface_url:'x'.repeat(3000)})).statusCode,413);
 const r=await call(h,{}, {method:'OPTIONS'});assert.equal(r.statusCode,204);assert.equal(s.calls.length,0);
});
test('persistent daily quota and instance burst limit',async()=>{
 const s=storage(),h=handler(s);
 for(let i=0;i<5;i++)assert.ok([200,201].includes((await call(h)).statusCode));
 assert.equal((await call(h)).statusCode,429);
 for(let i=1;i<50;i++)assert.equal((await call(handler(s),{domain:'iv',huggingface_url:`https://huggingface.co/test/model-${i}`})).statusCode,201);
 assert.equal((await call(handler(s),{domain:'iv',huggingface_url:'https://huggingface.co/test/model-51'})).statusCode,429);
 assert.equal(readList(s.files.get('method-submissions/received/iv/README.md').text,'iv').length,50);
});
test('empty lists validate all ten domains',()=>{
 for(const domain of Object.keys(DOMAINS))assert.deepEqual(readList(emptyList(domain),domain),[]);
});
