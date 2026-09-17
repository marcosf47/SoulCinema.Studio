from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC416 DIRECT MOBILE THEATER FULLSCREEN -->'
if marker in h: raise SystemExit('already patched')
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
block=r'''<!-- RC416 DIRECT MOBILE THEATER FULLSCREEN -->
<style id="rc416-direct-mobile-theater-fullscreen-style">
@media(max-width:860px){#rc416TheaterFullscreen{position:absolute;right:10px;bottom:10px;z-index:2147483000;width:42px;height:42px;min-height:42px;padding:0;border-radius:8px;font-size:22px;line-height:1;letter-spacing:0;background:rgba(0,0,0,.68);color:#fff;border:1px solid rgba(255,255,255,.45);display:grid;place-items:center}}
</style>
<script id="rc416-direct-mobile-theater-fullscreen">
(()=>{
 const mobile=()=>matchMedia('(max-width:860px)').matches;
 const theater=()=>document.getElementById('screeningTheater');
 const player=()=>document.getElementById('theaterPlayer');
 const frame=()=>player()?.closest('.theater-screen-frame')||player()?.parentElement;
 function ensure(){
  if(!mobile()||!theater()?.classList.contains('active'))return;
  const f=frame(); if(!f||document.getElementById('rc416TheaterFullscreen'))return;
  if(getComputedStyle(f).position==='static')f.style.position='relative';
  const b=document.createElement('button'); b.id='rc416TheaterFullscreen'; b.type='button'; b.setAttribute('aria-label','Full screen'); b.textContent='⛶';
  b.addEventListener('click',async e=>{e.preventDefault();e.stopImmediatePropagation();const v=player();if(!v)return;try{if(v.requestFullscreen)await v.requestFullscreen();else if(v.webkitEnterFullscreen)v.webkitEnterFullscreen();else if(f.requestFullscreen)await f.requestFullscreen();}catch(_){try{if(f.requestFullscreen)await f.requestFullscreen();}catch(__){}}},true);
  f.appendChild(b);
 }
 new MutationObserver(ensure).observe(document.documentElement,{attributes:true,subtree:true,attributeFilter:['class']});
 document.addEventListener('playing',e=>{if(e.target===player())ensure()},true);
 window.addEventListener('resize',ensure,{passive:true}); ensure();
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
