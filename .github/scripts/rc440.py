from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC440 MOBILE LIVE FULLSCREEN REENTRY REARM -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block=r'''<!-- RC440 MOBILE LIVE FULLSCREEN REENTRY REARM -->
<script id="rc440-mobile-live-fullscreen-reentry-rearm">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const selector='#rc414MobilePortals [data-rc414-room="Live Center"],#portals .portal[data-room="Live Center"],#portals .portal[data-mobile-room="Live Center"]';
 const room=()=>document.getElementById('liveCenter');
 let armed=true;
 const fs=()=>document.fullscreenElement||document.webkitFullscreenElement;
 const enter=e=>{
  if(!armed||!e.target?.closest?.(selector)||fs())return;
  const r=room();if(!r)return;
  armed=false;
  try{
   const p=r.requestFullscreen?.({navigationUI:'hide'})||r.webkitRequestFullscreen?.();
   if(p?.then)p.then(()=>screen.orientation?.lock?.('landscape')).catch(()=>{armed=true});
  }catch(_){armed=true}
 };
 const rearm=()=>{
  if(!fs()){
   armed=true;
   try{screen.orientation?.unlock?.()}catch(_){}
  }
 };
 // Exact user gesture on every Live Center entry. Rearm whenever Live fullscreen exits.
 document.addEventListener('pointerup',enter,true);
 document.addEventListener('touchend',enter,{capture:true,passive:true});
 document.addEventListener('click',enter,true);
 document.addEventListener('fullscreenchange',rearm,true);
 document.addEventListener('webkitfullscreenchange',rearm,true);
 const back=document.getElementById('returnLobby');
 back?.addEventListener('click',()=>{armed=true},true);
 new MutationObserver(()=>{
  if(document.body.dataset.experience==='portal_mode')armed=true;
 }).observe(document.body,{attributes:true,attributeFilter:['data-experience']});
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
for locked in ('RC439 MOBILE LIVE ENTRY TRUE FULLSCREEN LOCK','RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
