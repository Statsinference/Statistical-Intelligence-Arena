const fs = require('fs');
const path = require('path');
const {JSDOM} = require('jsdom');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');
const adaptor=liteAdaptor(); RegisterHTMLHandler(adaptor);
const tex=new TeX({packages:AllPackages, maxMacros:1000, maxBuffer:100000, formatError:(_jax,error)=>{throw error;}});
const math=mathjax.document('', {InputJax:tex,OutputJax:new SVG({fontCache:'none'})});
const directory=path.join(process.cwd(),'registry','drafts');
const before=JSON.parse(fs.readFileSync(process.env.RUNNER_TEMP+'/math-baseline.json','utf8'));
const files=fs.readdirSync(directory).filter(p=>['iv-cui-2023-longitudinal-survival-v1.md','proximal-cui-2024-linear-v1.md','iv-wei-2021-censored-quantile-v1.md','mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1.md'].includes(p)).sort();
const baselineFiles=Object.keys(before).sort();

const fence = new RegExp('^'+String.fromCharCode(96).repeat(3)+'math[ \\t]*\\r?\\n([\\s\\S]*?)^'+String.fromCharCode(96).repeat(3)+'[ \\t]*$', 'gm');
let expectedTotal=0;
const tasks=files.map(file=>{
  const source=fs.readFileSync(path.join(directory,file),'utf8');
  const expressions=[...source.matchAll(fence)].map(x=>x[1].trim());
  const previous=before[file].map(x=>x.trim());
  if(JSON.stringify(expressions)!==JSON.stringify(previous))
    throw Error('Changed, omitted, reordered, or added math in '+file+' (before '+previous.length+', after '+expressions.length+')');
  if(/(^|\n)\$\$[ \t]*(\r?\n|$)/m.test(source))throw Error('Legacy $$ block left in '+file);
  if(/\|\s*Evidence status\s*\|/i.test(source))throw Error('Evidence status column still present in '+file);
  expectedTotal+=expressions.length;
  return {file,source,expressions};
});
if(files.length<1 || expectedTotal<1)throw Error('Insufficient coverage: '+files.length+' records, '+expectedTotal+' equations');
let current=0, checked=0, docs=0, errors=[];
async function worker(){
 while(true){
  let idx=current++;if(idx>=tasks.length)return;
  let {file,source,expressions}=tasks[idx];
  try {
   const response=await fetch('https://api.github.com/markdown',{
    method:'POST',headers:{Authorization:'Bearer '+process.env.GH_TOKEN,Accept:'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json'},
    body:JSON.stringify({text:source,mode:'gfm',context:'Statsinference/stats-inference-arena'})
   });
   if(!response.ok)throw Error('GitHub Markdown HTTP '+response.status);
   const html=await response.text();
   const doc=new JSDOM(html).window.document;
   const elements=[...doc.querySelectorAll('math-renderer.js-display-math')];
   if(elements.length!==expressions.length)throw Error('GitHub returned '+elements.length+' display blocks vs '+expressions.length+' source blocks');
   for(let i=0;i<elements.length;i++){
    let received=elements[i].textContent.trim();
    if(!received.startsWith('$$')||!received.endsWith('$$'))throw Error('Unexpected GitHub math wrapper at equation '+(i+1));
    received=received.slice(2,-2).trim();
    if(received!==expressions[i])throw Error('GitHub changed math input at equation '+(i+1)+' expected='+JSON.stringify(expressions[i])+' received='+JSON.stringify(received));
    const rendered=math.convert(received,{display:true});
    if(adaptor.outerHTML(rendered).includes('data-mjx-error'))throw Error('MathJax error at equation '+(i+1));
    checked++;
   }
   docs++;
  }catch(e){errors.push({file,error:String(e)});}
 }
}
Promise.all(Array.from({length:3},worker)).then(()=>{
 console.log(JSON.stringify({documents:docs,documentsExpected:files.length,blocks:checked,blocksExpected:expectedTotal,errors},null,2));
 if(errors.length || docs!==files.length || checked!==expectedTotal)process.exitCode=1;
}).catch(error=>{console.error(error);process.exitCode=1});
