from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Retire RC440 re-entry trigger: it enters fullscreen immediately on the Live card tap.
h=re.sub(r'<!-- RC440 MOBILE LIVE FULLSCREEN REENTRY REARM -->\s*<script id="rc440-mobile-live-fullscreen-reentry-rearm">.*?</script>\s*','',h,count=1,flags=re.S)
marker='<!-- RC441 MOBILE LIVE LANDSCAPE GATE + LOBBY CLEANUP -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block=r'''<!-- RC441 MOBILE LIVE LANDSCAPE GATE + LOBBY CLEANUP -->
<script id="rc441-mobile-live-landscape-gate-lobby-cleanup">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const live=()=>document.getElementById('liveCenter')?.classList.contains('active');
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 const fs=()=>document.fullscreenElement||document.webkitFullscreenElement;
 const room=()=>document.getElementById('liveCenter');
 let armed=false;
 const liveCard=e=>!!e.target?.closest?.('#rc414MobilePortals [data-rc414-room="Live Center"],#portals .portal[data-room="Live Center"],#portals .portal[data-mobile-room="Live Center"]');
 const prep=()=>{const f=document.getElementById('rc275LiveFrame');if(f){f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');f.setAttribute('allow','autoplay; fullscreen; picture-in-picture')}return f};
 const enter=()=>{
  if(!armed||!live()||!landscape()||fs())return;
  const r=room();if(!r)return;
  // Orientation event itself may not carry activation; consume it only when browser permits.
  try{const p=r.requestFullscreen?.({navigationUI:'hide'})||r.webkitRequestFullscreen?.();if(p?.then)p.then(()=>{armed=false;screen.orientation?.lock?.('landscape').catch?.(()=>{})}).catch(()=>{})}catch(_){}
 };
 // Entering Live in portrait only arms the next landscape transition; never fullscreen on entry.
 document.addEventListener('pointerup',e=>{if(liveCard(e)){armed=true;prep()}},true);
 document.addEventListener('touchend',e=>{if(liveCard(e)){armed=true;prep()}},{capture:true,passive:true});
 document.addEventListener('click',e=>{if(liveCard(e)){armed=true;prep()}},true);
 window.addEventListener('orientationchange',()=>queueMicrotask(enter),{passive:true});
 screen.orientation?.addEventListener?.('change',()=>queueMicrotask(enter));
 window.addEventListener('resize',()=>{if(landscape())queueMicrotask(enter)},{passive:true});
 const cleanup=()=>{
  armed=false;
  const current=fs();const r=room();
  if(current&&(current===r||r?.contains(current))){try{(document.exitFullscreen?.()||document.webkitExitFullscreen?.())?.catch?.(()=>{})}catch(_){}}
  try{screen.orientation?.unlock?.()}catch(_){}
  document.body.classList.remove('rc400-live-landscape');
 };
 // Back to Grand Lobby must leave no fullscreen/orientation state behind.
 document.addEventListener('click',e=>{if(e.target?.closest?.('#liveCenter #returnLobby,#liveCenter .room-back,#liveCenter [data-back-to-lobby]'))cleanup()},true);
 document.addEventListener('fullscreenchange',()=>{if(!fs()&&!live())cleanup()},true);
 document.addEventListener('webkitfullscreenchange',()=>{if(!fs()&&!live())cleanup()},true);
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
for locked in ('RC439 MOBILE LIVE ENTRY TRUE FULLSCREEN LOCK','RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
