import test from 'node:test';
import assert from 'node:assert/strict';
import {createHandler, normalizeModelURL} from '../api/submit.js';
const origin='https://statsinference.github.io';
const env={GITHUB_SUBMISSIONS_TOKEN:'fake-github-secret',TURNSTILE_SECRET_KEY:'fake-turnstile-secret'};
const valid={huggingface_url:'https://huggingface.co/Brownight/tabpfn-iv-adapter-v0.3',domain:'iv',turnstile_token:'single-use-test-token',website:''};
const repo={id:1426616721,full_name:'Statsinference/stats-inference-arena',private:true,has_issues:true};
const receipt='7c6ffbce-4475-4e20-aea1-c7859954a78f';
const response=(data,status=200)=>new Response(JSON.stringify(data),{status});
async function invoke({body=valid,method='POST',headers={},environment=env,steps}={}){
 const calls=[];
 const fetchImpl=async (url,options)=>{calls.push({url,options});const s=(steps||[
  ()=>response({success:true,hostname:'statsinference.github.io',action:'method_submit'}),()=>response(repo),()=>response({number:42},201)
  ])[calls.length-1];if(!s)throw Error('Unexpected network call');return s(url,options);};
 const req={method,headers:{origin,'content-type':'application/json','x-arena-submission':'1',...headers},body};
 const res={headers:{},statusCode:0,setHeader(k,v){this.headers[k]=v;},end(v){this.body=v?JSON.parse(v):null;}};
 await createHandler({env:environment,fetchImpl,uuid:()=>receipt})(req,res);
 return {res,calls};
}
test('HF model URL validation',()=>{
 assert.equal(normalizeModelURL(valid.huggingface_url+'/'),valid.huggingface_url);
 assert.equal(normalizeModelURL('https://huggingface.co/owner/model/tree/main'),'https://huggingface.co/owner/model/tree/main');
 for(const url of ['http://huggingface.co/a/b','https://huggingface.co.evil.test/a/b','https://user:secret@huggingface.co/a/b','https://huggingface.co/a/b?token=secret','https://huggingface.co/datasets/a/b','https://huggingface.co/spaces/a','https://huggingface.co/a/b#token','https://huggingface.co/a/%62','https://127.0.0.1/a/b','javascript:alert(1)'])assert.equal(normalizeModelURL(url),null,url);
});
test('private write succeeds and returns only receipt',async()=>{
 const {res,calls}=await invoke();assert.equal(res.statusCode,201);assert.deepEqual(res.body,{ok:true,receipt});assert.equal(calls.length,3);
 assert.equal(calls[2].url,'https://api.github.com/repos/Statsinference/stats-inference-arena/issues');
 const issue=JSON.parse(calls[2].options.body);assert.equal(issue.title,'[Method submission] Brownight/tabpfn-iv-adapter-v0.3');assert.ok(issue.body.includes(valid.huggingface_url));
 assert.ok(!JSON.stringify(res).includes('fake-github-secret'));assert.ok(!JSON.stringify(res.body).includes('42'));
});
test('missing deployment secrets fails closed',async()=>{const {res,calls}=await invoke({environment:{}});assert.equal(res.statusCode,503);assert.equal(calls.length,0);});
test('does not accept public or wrong repository as inbox',async()=>{
 for(const metadata of [{...repo,private:false},{...repo,id:999},{...repo,has_issues:false}]){
  const {res,calls}=await invoke({steps:[()=>response({success:true,hostname:'statsinference.github.io',action:'method_submit'}),()=>response(metadata)]});assert.equal(res.statusCode,503);assert.equal(calls.length,2);
 }
});
test('bad origin and read requests cannot read or write',async()=>{
 let r=await invoke({headers:{origin:'https://evil.test'}});assert.equal(r.res.statusCode,403);assert.equal(r.calls.length,0);assert.equal(r.res.headers['Access-Control-Allow-Origin'],undefined);
 r=await invoke({method:'GET'});assert.equal(r.res.statusCode,405);assert.equal(r.calls.length,0);
 r=await invoke({method:'OPTIONS'});assert.equal(r.res.statusCode,204);assert.equal(r.calls.length,0);assert.equal(r.res.headers['Access-Control-Allow-Origin'],origin);
});
test('invalid bodies never reach the private inbox',async()=>{
 for(const body of [{...valid,website:'bot'}, {...valid,domain:'fake'}, {...valid,turnstile_token:''},{...valid,repository:'other/public'},null,'bad json',Array(20000).fill('x').join('')]){
  const r=await invoke({body});assert.ok(r.res.statusCode>=400);assert.equal(r.calls.length,0);
 }
});
test('captcha hostname and action verified server side',async()=>{
 for(const c of [{success:false},{success:true,hostname:'evil.test',action:'method_submit'},{success:true,hostname:'statsinference.github.io',action:'wrong'}]){
  const r=await invoke({steps:[()=>response(c)]});assert.equal(r.res.statusCode,403);assert.equal(r.calls.length,1);
 }
});
test('upstream failure never produces a success receipt',async()=>{
 const r=await invoke({steps:[()=>response({success:true,hostname:'statsinference.github.io',action:'method_submit'}),()=>response(repo),()=>response({message:'private error'},500)]});assert.equal(r.res.statusCode,503);assert.equal(r.res.body.ok,false);assert.ok(!JSON.stringify(r.res.body).includes('private error'));
});
test('body, content type and custom header are bounded',async()=>{
 for(const headers of [{'content-length':'99999'},{'content-type':'text/plain'},{'x-arena-submission':''}]){const r=await invoke({headers});assert.ok(r.res.statusCode>=400);assert.equal(r.calls.length,0);}
});
