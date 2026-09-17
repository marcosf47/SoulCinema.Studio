from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC432 DIRECT MOBILE LIVE FULLSCREEN -->'
if marker in h: raise SystemExit('already patched')
# Remove RC431 experiment only. Preserve RC400, theater and desktop.
s=h.find('<!-- RC431 MOBILE LIVE IFRAME FULLSCREEN PERMISSION -->')
if s!=-1:
    e=h.find('</script>',s)
    if e!=-1:h=h[:s]+h[e+9:]
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
patch=r'''<!-- RC432 DIRECT MOBILE LIVE FULLSCREEN -->
<style id="rc432-direct-mobile-live-fullscreen-style">
@media (pointer:coarse) and (max-width:1400px){
 #rc432LiveFullscreen{position:absolute;right:12px;bottom:12px;z-index:2147483000;width:44px;height:44px;min-height:44px;padding:0;border-radius:9px;font-size:23px;line-height:1;letter-spacing:0;background:rgba(0,0,0,.70);color:#fff;border:1px solid rgba(255,255,255,.48);display:grid;place-items:center}
}
</style>
<script id="rc432-direct-mobile-live-fullscreen">
(()=>{
 const mobile=()=>matchMedia('(pointer:coarse)').matches&&Math.max(screen.width,screen.height)<=1400;
 const room=()=>document.getElementById('liveCenter');
 const frame=()=>document.getElementById('rc275LiveFrame');
 const stage=()=>frame()?.parentElement;
 const enter=async()=>{
  if(!mobile()||!room()?.classList.contains('active'))return;
  const f=frame(),s=stage();if(!f||!s)return;
  f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');
  const a=f.getAttribute('allow')||'';if(!/fullscreen/i.test(a))f.setAttribute('allow',(a?a+'; ':'')+'fullscreen *');
  try{
   if(s.requestFullscreen)await s.requestFullscreen({navigationUI:'hide'});
   else if(s.webkitRequestFullscreen)s.webkitRequestFullscreen();
   else if(f.requestFullscreen)await f.requestFullscreen({navigationUI:'hide'});
   else if(f.webkitRequestFullscreen)f.webkitRequestFullscreen();
  }catch(_){try{if(f.requestFullscreen)await f.requestFullscreen();}catch(__){}}
 };
 function ensure(){
  if(!mobile()||!room()?.classList.contains('active'))return;
  const s=stage();if(!s||document.getElementById('rc432LiveFullscreen'))return;
  if(getComputedStyle(s).position==='static')s.style.position='relative';
  const b=document.createElement('button');b.id='rc432LiveFullscreen';b.type='button';b.setAttribute('aria-label','Full screen');b.textContent='⛶';
  b.addEventListener('pointerdown',e=>{e.preventDefault();e.stopImmediatePropagation();enter()},true);
  b.addEventListener('click',e=>{e.preventDefault();e.stopImmediatePropagation()},true);
  s.appendChild(b);
 }
 new MutationObserver(ensure).observe(document.documentElement,{attributes:true,childList:true,subtree:true,attributeFilter:['class']});
 window.addEventListener('resize',ensure,{passive:true});ensure();
})();
</script>
'''
h=h.replace(anchor,patch+anchor,1)
p.write_text(h,encoding='utf-8')
