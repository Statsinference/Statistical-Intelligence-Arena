const fs=require('fs');
const path=require('path');
const {JSDOM}=require('jsdom');
const {mathjax}=require('mathjax-full/js/mathjax.js');
const {TeX}=require('mathjax-full/js/input/tex.js');
const {SVG}=require('mathjax-full/js/output/svg.js');
const {liteAdaptor}=require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler}=require('mathjax-full/js/handlers/html.js');
const {AllPackages}=require('mathjax-full/js/input/tex/AllPackages.js');
const adaptor=liteAdaptor();RegisterHTMLHandler(adaptor);
const tex=new TeX({packages:AllPackages,maxMacros:1000,maxBuffer:100000,formatError:(_jax,error)=>{throw error;}});
const math=mathjax.document('',{InputJax:tex,OutputJax:new SVG({fontCache:'none'})});
const directory=path.join(process.cwd(),'registry','drafts');
const before=JSON.parse(fs.readFileSync(process.env.RUNNER_TEMP+'/math-baseline.json','utf8'));
const files=fs.readdirSync(directory).filter(p=>p.endsWith('.md')).sort();
if(JSON.stringify(files)!==JSON.stringify(Object.keys(before).sort()))throw Error('Record filenames differ between original and regenerated catalog');
const fence=new RegExp('^'+String.fromCharCode(96).repeat(3)+'math[ \\t]*\\r?\\n([\\s\\S]*?)^'+String.fromCharCode(96).repeat(3)+'[ \\t]*$','gm');

let total=0,githubAddedSlashes=0;
const tasks=files.map(file=>{
 const source=fs.readFileSync(path.join(directory,file),'utf8');
 const expressions=[...source.matchAll(fence)].map(x=>x[1].trim());
 const previous=before[file].map(x=>x.trim());
 if(expressions.length!==previous.length)throw Error('Display equation count changed in '+file);
 for(let i=0;i<expressions.length;i++){
  if(expressions[i]!==previous[i])throw Error('Mathematical input changed in '+file+' #'+(i+1));
 }
 if(/(^|\n)\$\$[ \t]*(\r?\n|$)/m.test(source))throw Error('Legacy $$ block left in '+file);
 if(/\|\s*Evidence status\s*\|/i.test(source))throw Error('Evidence status column still present in '+file);
 total+=expressions.length;
 return {file,source,expressions};
});
if(files.length!==183||total!==1382)throw Error('Insufficient coverage: '+files.length+' records, '+total+' equations');
const batches=[];
for(let i=0;i<tasks.length;i+=23)batches.push(tasks.slice(i,i+23));
(async()=>{
 let count=0,docs=0;const problems=[];
 for(let k=0;k<batches.length;k++){
  const group=batches[k];
  const text=group.map(x=>x.source).join('\n\n<!-- file boundary -->\n\n');
  const expected=group.flatMap(x=>x.expressions.map((expr,i)=>({file:x.file,index:i+1,expr})));
  let response=await fetch('https://api.github.com/markdown',{
   method:'POST',headers:{Authorization:'Bearer '+process.env.GH_TOKEN,Accept:'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json'},
   body:JSON.stringify({text,mode:'gfm',context:'Statsinference/stats-inference-arena'})
  });
  if(!response.ok)throw Error('GitHub Markdown HTTP '+response.status+' on batch '+(k+1));
  const html=await response.text();
  const document=new JSDOM(html).window.document;
  const elements=[...document.querySelectorAll('math-renderer.js-display-math')];
  if(elements.length!==expected.length)throw Error('GitHub returned '+elements.length+' blocks vs '+expected.length+' source blocks in batch '+(k+1));
  for(let i=0;i<elements.length;i++){
   const x=expected[i];let received=elements[i].textContent.trim();
   if(!received.startsWith('$$')||!received.endsWith('$$'))throw Error('Unexpected GitHub math wrapper '+x.file+' #'+x.index);
   received=received.slice(2,-2).trim();
   const githubExpected=x.expr.replace(/(?<!\\)\\\\(?=\r?\n)/g,match=>{githubAddedSlashes++;return match+'\\';});
   if(received!==githubExpected){problems.push({file:x.file,index:x.index,error:'Unexpected GitHub input change',expected:githubExpected,received});continue;}
   try{const rendered=math.convert(received,{display:true});if(adaptor.outerHTML(rendered).includes('data-mjx-error'))throw Error('MathJax error element');count++;}
   catch(error){problems.push({file:x.file,index:x.index,error:String(error)});}
  }
  docs+=group.length;
  console.log('Verified batch '+(k+1)+'/'+batches.length+': '+group.length+' documents, '+expected.length+' formulas');
 }
 console.log(JSON.stringify({documents:docs,documentsExpected:files.length,blocks:count,blocksExpected:total,githubAddedSlashes,errors:problems},null,2));
 if(problems.length||docs!==files.length||count!==total)process.exitCode=1;
})().catch(error=>{console.error(error);process.exitCode=1});
