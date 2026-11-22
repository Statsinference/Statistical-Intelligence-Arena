'use strict';
// Publish source-reported suites without pooling targets, metric scales or timing cohorts.
const baseValidate=validate;
validate=function(data){
 baseValidate(data);
 for(const s of data.suites){
  if(s.dgp_results!=null&&!Array.isArray(s.dgp_results))throw Error('Invalid DGP results');
  for(const r of s.dgp_results||[]){
   if(!GROUPS.includes(r.group)||typeof r.dgp!=='string'||typeof r.method!=='string'||!['pfn','classical'].includes(r.family))throw Error('Invalid DGP result row');
   for(const {k} of COLS.slice(2)){const v=r[k];if(v!=null&&(!number(v)||(k!=='bias'&&v<0)||(k==='coverage'&&v>1)))throw Error('Invalid DGP metric');}
  }
  for(const r of [...s.rows,...(s.dgp_results||[])]){
   if(r.reported_se!=null&&(!number(r.reported_se)||r.reported_se<0))throw Error('Invalid reported SE');
   if(r.variance_is_approximate&&(r.variance_basis!=='square_of_rounded_reported_se'||!number(r.reported_se)||!number(r.variance)||Math.abs(r.variance-r.reported_se*r.reported_se)>1e-10))throw Error('Invalid variance transcription');
   if(r.reported_display!=null&&(!r.reported_display||typeof r.reported_display!=='object'||Object.values(r.reported_display).some(v=>typeof v!=='string')))throw Error('Invalid source display tokens');
  }
  if(s.timing_comparisons!=null&&!Array.isArray(s.timing_comparisons))throw Error('Invalid timing comparisons');
  for(const t of s.timing_comparisons||[]){
   if(t.scope!=='previous_model_and_test_set'||!Array.isArray(t.rows)||!number(t.tables)||!number(t.threads))throw Error('Timing cohort must be explicit');
   for(const r of t.rows)if(typeof r.method!=='string'||!number(r.median_time_s)||r.median_time_s<=0||!number(r.median_paired_ratio)||r.median_paired_ratio<=0)throw Error('Invalid paired timing');
  }
 }
 return data;
};
// Preserve printed precision, with explicit approximate SE-to-variance conversion.
function releaseMetric(r,k){
 if(!number(r[k]))return '—';
 if(r.reported_display?.[k]!=null)return esc(r.reported_display[k]);
 if(k==='coverage')return (r[k]*100).toFixed(2)+'%';
 const v=r[k],a=Math.abs(v),digits=k==='time_s'?4:k==='variance'?5:4;
 const text=a!==0&&(a>=10000||a<.0001)?a.toExponential(2):a.toFixed(digits);
 return (k==='variance'&&r.variance_is_approximate?'≈':'')+(v<0?'−':k==='bias'&&v>0?'+':'')+text;
}
renderTable=function(){
 $('#thead').innerHTML=COLS.map((c,i)=>`<th scope="col" class="${i>1?'r':''} ${sortKey===c.k?'sorted':''}"${c.k==='group'?'':` aria-sort="${sortKey===c.k?(sortDir===1?'ascending':'descending'):'none'}"`} title="${esc(c.hint||c.label)}">${c.k==='group'?c.label:`<button data-sort="${c.k}">${c.label}${sortKey===c.k?`<span class="arrow">${sortDir===1?'↑':'↓'}</span>`:''}</button>`}</th>`).join('');
 const rr=rows();$('#export-btn').disabled=!rr.some(r=>r.status!=='not_reported');
 $('#tbody').innerHTML=groups().map(g=>{const gr=rr.filter(r=>r.group===g).sort(compare);if(!gr.length)return `<tr class="row-pending"><td><span class="group-tag ${g.toLowerCase()}">${g}</span></td><td>${loadError?'Results unavailable':current()?'No matching published results':'Results not yet published'}</td>${COLS.slice(2).map(()=>'<td class="r num">—</td>').join('')}</tr>`;return gr.map(r=>`<tr class="${r.status==='not_reported'?'row-unreported':'row-reported'}"><td><span class="group-tag ${g.toLowerCase()}">${g}</span></td><td><span class="mname">${esc(r.method)}</span>${pill(r.family)}${r.status==='not_reported'?'<span class="org missing-result">Not reported for this run</span>':''}${r.org?`<span class="org">${esc(r.org)}</span>`:''}</td>${COLS.slice(2).map(c=>`<td class="r num"${c.k==='variance'&&r.variance_is_approximate?` title="Approximate: rounded reported SE ${r.reported_se} squared."`: ''}>${releaseMetric(r,c.k)}</td>`).join('')}</tr>`).join('');}).join('');
};
const baseScatter=scatter;
scatter=function(selector,xkey,ykey,xlabel,ylabel,isCoverage=false){const norm=current()?.metric_scale==='per_table_y_sd';baseScatter(selector,xkey,ykey,norm&&xkey==='length'?'Normalized mean CI length':xlabel,norm&&ykey==='rmse'?'Normalized RMSE':ylabel,isCoverage);};
// Replace only the CSV listener, retaining the existing public control and styles.
const oldExport=document.getElementById('export-btn'),newExport=oldExport.cloneNode(true);oldExport.replaceWith(newExport);
newExport.addEventListener('click',()=>{
 const s=current(),rr=rows();if(!s||!rr.some(r=>r.status!=='not_reported'))return;
 const keys=[...COLS.map(c=>c.k),'reported_se','variance_is_approximate','variance_basis','status','suite_id','source_date','metric_scale','variance_definition','hardware','timing_scope'];
 const out=groups().flatMap(g=>rr.filter(r=>r.group===g).sort(compare)).map(r=>({...r,suite_id:s.id,source_date:s.report_date,metric_scale:s.metric_scale,variance_definition:s.variance_definition,hardware:s.hardware,timing_scope:s.timing_scope}));
 const text=[keys.join(','),...out.map(r=>keys.map(k=>csvCell(r[k])).join(','))].join('\r\n');
 const url=URL.createObjectURL(new Blob([text],{type:'text/csv;charset=utf-8'})),a=document.createElement('a');a.href=url;a.download='statistical-inference-arena-'+task+'-'+split+'.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
});
const baseColumnLabels=Object.fromEntries(COLS.map(c=>[c.k,c.label]));
function normPrefix(){return current()?.metric_scale==='per_table_y_sd'?'Norm. ':'';}
function syncMetricLabels(){
 const s=current(),np=normPrefix();
 for(const c of COLS){c.label=(['bias','variance','rmse','length'].includes(c.k)?np:'')+baseColumnLabels[c.k];if(c.k==='variance')c.hint=s?.variance_definition||s?.variance_note||'Variance convention is specified separately for each evaluation suite.';}
}
function renderReleaseDetails(){
 const s=current(),container=document.getElementById('report-details');
 container.hidden=!s?.source;
 if(!s?.source){container.innerHTML='';return;}
 const filterDGP=r=>(split==='both'||r.group===split)&&(family==='all'||r.family===family)&&(!query||(r.method+' '+r.dgp).toLowerCase().includes(query));
 const dd=(s.dgp_results||[]).filter(filterDGP),np=normPrefix(),vk=s.dgp_variability==='reported_se'?'reported_se':'variance';
 const vlabel=vk==='reported_se'?'Reported SE':np+'Variance';
 const dgpHead='<tr><th scope="col">Split</th><th scope="col">DGP configuration</th><th scope="col">Method</th>'+[[np+'Bias','bias'],[vlabel,vk],[np+'RMSE','rmse'],[np+'Length','length'],['Coverage','coverage'],['Time (s)','time_s']].map(([label])=>'<th scope="col" class="r">'+esc(label)+'</th>').join('')+'</tr>';
 const dgpRows=dd.map(r=>`<tr><td><span class="group-tag ${r.group.toLowerCase()}">${esc(r.group==='OOD'?(s.split_label||'OOD'):'ID')}</span></td><td>${esc(r.dgp)}</td><td>${esc(r.method)}</td>${['bias',vk,'rmse','length','coverage','time_s'].map(k=>`<td class="r num">${releaseMetric(r,k)}</td>`).join('')}</tr>`).join('');
 const detail=(s.dgp_results||[]).length?`<details><summary>Results by DGP <span class="muted">· ${dd.length} method–configuration rows in this filter</span></summary><div class="detail-inner"><p>${esc(s.dgp_note||'Transcribed from the report. Missing values were not supplied and are not zero.')}</p><div class="tbl-wrap" tabindex="0" role="region" aria-label="Scrollable DGP results"><table class="detail-table"><thead>${dgpHead}</thead><tbody>${dgpRows||'<tr><td colspan="9">No reported per-DGP results for this filter.</td></tr>'}</tbody></table></div></div></details>`:'';
 const timing=(s.timing_comparisons||[]).map(t=>`<section class="timing-block" aria-label="Previous-run CPU comparison"><h3>${esc(t.label)}</h3><span class="scope-badge">PREVIOUS MODEL &amp; TEST SET · TIMING ONLY</span><p class="timing-note">${esc(t.note)}</p><div class="tbl-wrap" tabindex="0" role="region" aria-label="Scrollable paired CPU timing table"><table class="timing-table"><caption class="sr-only">Previous-run timing on ${t.tables} matched tables; not current ID/OOD accuracy results</caption><thead><tr><th scope="col">Method</th><th scope="col">Configuration</th><th scope="col" class="r">Median time / table</th><th scope="col" class="r">Median paired ratio</th></tr></thead><tbody>${t.rows.map(r=>`<tr><td>${esc(r.method)}</td><td>${esc(r.configuration)}</td><td class="r num">${r.median_time_s.toFixed(3)} s</td><td class="r num">${r.median_paired_ratio.toFixed(2)}×</td></tr>`).join('')}</tbody></table></div><p class="data-footnote">${t.tables} matched tables · ${t.threads} CPU threads · ${esc(t.hardware)}. Source: ${esc(t.source_table)}. These values do not enter current-run rankings.</p></section>`).join('');
 const facts=[['Target',s.target],['Sampling',s.sample_design],['ID / OOD',s.split_definition],['Generator scope',s.generator_scope],['Aggregation',s.aggregation],['Metric scale',s.metric_scale==='per_table_y_sd'?'Each table normalized by its observed Y sample SD before aggregation; coverage and seconds are unchanged.':s.metric_scale==='original'?'Original outcome/effect units.':'As reported; no additional normalization applied by the website.'],['Variance / SE',s.variance_note],['Coverage uncertainty',s.coverage_note],['Runtime',[s.hardware,s.timing_scope].filter(Boolean).join(' ')],['Comparison scope',s.comparison_note],['Source file',s.source.file],['Source locations',Object.entries(s.source.locators||{}).map(([k,v])=>k+': '+v).join('; ')],['Source status',s.source.verification]].filter(([,v])=>v);
 const byline=[s.source.author,s.source.date].filter(Boolean).join(' · ');
 container.innerHTML=`<div class="section-label">SOURCE-REPORTED EVALUATION</div><h2>Results, in context.</h2><div class="release-meta"><span>${esc(s.source.title)}</span>${byline?`<span>· ${esc(byline)}</span>`:''}<a href="data/results.json" download="statistical-inference-arena-results.json">Download source-reported data ↗</a></div>${detail}${timing}<details><summary>Evaluation protocol &amp; source notes</summary><div class="detail-inner"><dl class="release-facts">${facts.map(([k,v])=>`<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl></div></details>`;
}
// Keep the existing chart, search, sorting and theme implementation.
const baseRenderResults=renderResults;
renderResults=function(){syncMetricLabels();baseRenderResults();renderReleaseDetails();};
const baseRender=render;
render=function(){
 syncMetricLabels();baseRender();
 const s=current(),context=document.getElementById('release-context'),np=normPrefix();
 context.hidden=!s?.source;
 if(s?.source){
  context.innerHTML=(s.source.date?'<strong>Report date: '+esc(s.source.date)+'.</strong> ':'')+esc(s.context_note||s.sample_design||'Source-reported results.')+' <a href="#report-details">Protocol &amp; source notes ↘</a>';
  document.getElementById('view-note').textContent=(np?'Normalized by per-table SD(Y)':'Results as reported')+(s.report_date?' · '+s.report_date:'');
  document.getElementById('table-note').textContent=(s.display_note||s.variance_note||'Source definitions apply.')+' Missing cells are not reported, not zero. No cross-domain pooling.';
  const measured=new Set((s.rows||[]).filter(r=>number(r.rmse)).map(r=>r.method_id||r.method));
  document.querySelector('[data-card="ranking"] .card-bottom>span').textContent=measured.size===1?'One reported method · no comparative rank':'Within each test split';
 }else{context.innerHTML='';document.querySelector('[data-card="ranking"] .card-bottom>span').textContent='Within each test split';}
 document.querySelector('[data-card="ranking"] h3').textContent='Methods by '+np+'RMSE';
 document.querySelector('[data-card="runtime"] h3').textContent=np+'RMSE vs Time';
 document.querySelector('[data-card="coverage"] h3').textContent='Coverage vs '+np+'Length';
 document.querySelector('[data-card="runtime"] .card-sub').textContent='Reported timing · see hardware';
 const publishedDomains=new Set(DATA.suites.filter(x=>x.rows.some(r=>number(r.rmse))).map(x=>x.domain));
 if(!loadError&&publishedDomains.size){
  document.getElementById('release-status').textContent='RESULTS · '+publishedDomains.size+' DOMAINS';
  document.getElementById('release-description').textContent='Source-reported results. Definitions, scales and timing conditions are documented for each evaluation.';
 }
 for(const b of document.querySelectorAll('[data-t]')){const present=publishedDomains.has(b.dataset.t);b.classList.toggle('has-results',present);b.title=present?'Reported results available':'Results not yet published';}
};
try{DATA=validate(DATA);render();}catch(e){loadError='Unable to validate reported result metadata.';render();console.error(e);}
