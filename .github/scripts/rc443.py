from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Replace RC442 controller with a user-activation-safe landscape tap authority.
h=re.sub(r'<!-- RC442 SINGLE MOBILE LIVE LANDSCAPE AUTHORITY -->\s*<script id="rc442-single-mobile-live-landscape-authority">.*?</script>\s*','',h,count=1,flags=re.S)
marker='<!-- RC443 MOBILE LIVE LANDSCAPE TAP TRUE FULLSCREEN -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block=r'''<!-- RC443 MOBILE LIVE LANDSCAPE TAP TRUE FULLSCREEN -->
<script id="rc443-mobile-live-landscape-tap-true-fullscreen">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const room=()=>document.getElementById('liveCenter');
 const live=()=>room()?.classList.contains('active');
 const fs=()=>document.fullscreenElement||document.webkitFullscreenElement;
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 let armed=false;
 const card=e=>!!e.target?.closest?.('#rc414MobilePortals [data-rc414-room="Live Center"],#portals .portal[data-room="Live Center"],#portals .portal[data-mobile-room="Live Center"]');
 const authorize=()=>{const f=document.getElementById('rc275LiveFrame');if(f){f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');f.setAttribute('allow','autoplay; fullscreen; picture-in-picture')}};
 document.addEventListener('click',e=>{if(card(e)){authorize();armed=true}},true);
 const enter=e=>{
  if(!armed||!live()||!landscape()||fs())return;
  const r=room();if(!r)return;
  // Parent Live chrome is the gesture target; iframe keeps its own native fullscreen button as fallback.
  if(e.target?.closest?.('#returnLobby,.room-back,[data-back-to-lobby]'))return;
  try{
   const p=r.requestFullscreen?.({navigationUI:'hide'})||r.webkitRequestFullscreen?.();
   if(p?.then)p.then(()=>{armed=false}).catch(()=>{});
  }catch(_){}
 };
 document.addEventListener('pointerup',enter,true);
 document.addEventListener('touchend',enter,{capture:true,passive:true});
 document.addEventListener('click',enter,true);
 const cleanup=()=>{
  armed=false;
  try{screen.orientation?.unlock?.()}catch(_){}
  document.body.classList.remove('rc400-live-landscape');
  delete document.body.dataset.rc400LiveLandscape;
 };
 document.addEventListener('click',e=>{
  if(!e.target?.closest?.('#liveCenter #returnLobby,#liveCenter .room-back,#liveCenter [data-back-to-lobby]'))return;
  const current=fs(),r=room();
  if(current&&(current===r||r?.contains(current))){try{const p=document.exitFullscreen?.()||document.webkitExitFullscreen?.();p?.catch?.(()=>{})}catch(_){}}
  cleanup();
 },true);
 new MutationObserver(()=>{if(document.body.dataset.experience==='portal_mode')cleanup()}).observe(document.body,{attributes:true,attributeFilter:['data-experience']});
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
if 'rc442-single-mobile-live-landscape-authority' in h: raise SystemExit('RC442 controller still present')
for locked in ('RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
