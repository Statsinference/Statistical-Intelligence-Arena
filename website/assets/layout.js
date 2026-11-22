'use strict';
// Theme and navigation only. The evaluation data and result calculations are untouched.
const themeKey='statsarena-theme-editorial';
theme=function(value){
 document.documentElement.dataset.theme=value;
 const label=value==='dark'?'Switch to light theme':'Switch to dark theme';
 document.getElementById('theme-btn').setAttribute('aria-label',label);
 document.getElementById('theme-btn').title=label;
 document.querySelector('meta[name="theme-color"]').content=value==='dark'?'#1c1c1a':'#f5f1ec';
 try{localStorage.setItem(themeKey,value);}catch(e){}
};
let preferredTheme='light';
try{const saved=localStorage.getItem(themeKey);if(['light','dark'].includes(saved))preferredTheme=saved;}catch(e){}
theme(preferredTheme);
const menuButton=document.getElementById('menu-btn'),sidebar=document.getElementById('sidebar'),scrim=document.getElementById('menu-scrim');
function setMenu(open){sidebar.classList.toggle('open',open);menuButton.setAttribute('aria-expanded',String(open));scrim.hidden=!open;document.body.style.overflow=open?'hidden':'';}
menuButton.addEventListener('click',()=>setMenu(!sidebar.classList.contains('open')));
scrim.addEventListener('click',()=>{setMenu(false);menuButton.focus();});
sidebar.addEventListener('click',e=>{if(e.target.closest('a,[data-t]')&&matchMedia('(max-width:860px)').matches){setMenu(false);(e.target.closest('a[href="#home"]')?menuButton:document.getElementById('main-panel')).focus({preventScroll:true});}});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&sidebar.classList.contains('open')){setMenu(false);menuButton.focus();}});
window.addEventListener('resize',()=>{if(!matchMedia('(max-width:860px)').matches)setMenu(false);});
document.getElementById('tabs').addEventListener('keydown',e=>{
 const b=e.target.closest('[data-t]');if(!b||!['ArrowUp','ArrowDown'].includes(e.key))return;
 e.preventDefault();const i=DOMAINS.findIndex(d=>d.id===b.dataset.t),j=(i+(e.key==='ArrowDown'?1:-1)+DOMAINS.length)%DOMAINS.length;
 chooseTask(DOMAINS[j].id);document.getElementById('tab-'+DOMAINS[j].id).focus();
});
