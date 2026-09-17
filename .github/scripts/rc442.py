from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Remove the RC439 controller only; preserve its fullscreen CSS.
h=re.sub(r'<script id="rc439-mobile-live-entry-true-fullscreen-lock">.*?</script>\s*','',h,count=1,flags=re.S)
# Remove RC441 controller so only one Live fullscreen authority remains.
h=re.sub(r'<!-- RC441 MOBILE LIVE LANDSCAPE GATE \+ LOBBY CLEANUP -->\s*<script id="rc441-mobile-live-landscape-gate-lobby-cleanup">.*?</script>\s*','',h,count=1,flags=re.S)
marker='<!-- RC442 SINGLE MOBILE LIVE LANDSCAPE AUTHORITY -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block=r'''<!-- RC442 SINGLE MOBILE LIVE LANDSCAPE AUTHORITY -->
<script id="rc442-single-mobile-live-landscape-authority">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const room=()=>document.getElementById('liveCenter');
 const live=()=>room()?.classList.contains('active');
 const fs=()=>document.fullscreenElement||document.webkitFullscreenElement;
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 const card=e=>!!e.target?.closest?.('#rc414MobilePortals [data-rc414-room="Live Center"],#portals .portal[data-room="Live Center"],#portals .portal[data-mobile-room="Live Center"]');
 let armed=false, enteredPortrait=false;
 const authorize=()=>{const f=document.getElementById('rc275LiveFrame');if(!f)return;f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');f.setAttribute('allow','autoplay; fullscreen; picture-in-picture')};
 const arm=e=>{if(!card(e))return;authorize();armed=true;enteredPortrait=!landscape()};
 document.addEventListener('click',arm,true);
 const tryLandscape=()=>{
  if(!armed||!enteredPortrait||!live()||!landscape()||fs())return;
  const r=room();if(!r)return;
  try{
   const p=r.requestFullscreen?.({navigationUI:'hide'})||r.webkitRequestFullscreen?.();
   if(p?.then)p.then(()=>{armed=false;screen.orientation?.lock?.('landscape').catch?.(()=>{})}).catch(()=>{});
  }catch(_){}
 };
 window.addEventListener('orientationchange',()=>setTimeout(tryLandscape,80),{passive:true});
 screen.orientation?.addEventListener?.('change',()=>setTimeout(tryLandscape,40));
 window.addEventListener('resize',()=>{if(landscape())setTimeout(tryLandscape,0)},{passive:true});
 const cleanup=()=>{
  armed=false;enteredPortrait=false;
  try{screen.orientation?.unlock?.()}catch(_){}
  document.body.classList.remove('rc400-live-landscape');
  delete document.body.dataset.rc400LiveLandscape;
 };
 // Cleanup before the existing Back handler changes scenes; do not stop propagation.
 document.addEventListener('click',e=>{
  if(!e.target?.closest?.('#liveCenter #returnLobby,#liveCenter .room-back,#liveCenter [data-back-to-lobby]'))return;
  const current=fs(),r=room();
  if(current&&(current===r||r?.contains(current))){try{const p=document.exitFullscreen?.()||document.webkitExitFullscreen?.();p?.catch?.(()=>{})}catch(_){}}
  cleanup();
 },true);
 new MutationObserver(()=>{if(document.body.dataset.experience==='portal_mode')cleanup()}).observe(document.body,{attributes:true,attributeFilter:['data-experience']});
 document.addEventListener('fullscreenchange',()=>{if(!fs())try{screen.orientation?.unlock?.()}catch(_){}});
 document.addEventListener('webkitfullscreenchange',()=>{if(!fs())try{screen.orientation?.unlock?.()}catch(_){}});
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
# RC439 CSS remains, but its entry controller must be gone.
if 'rc439-mobile-live-entry-true-fullscreen-lock' in h: raise SystemExit('RC439 controller still present')
if 'rc441-mobile-live-landscape-gate-lobby-cleanup' in h: raise SystemExit('RC441 controller still present')
for locked in ('RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
