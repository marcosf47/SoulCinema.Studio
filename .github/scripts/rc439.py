from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Remove failed RC438 hold guard.
h=re.sub(r'<!-- RC438 MOBILE LIVE FULLSCREEN HOLD GUARD -->\s*<script id="rc438-mobile-live-fullscreen-hold-guard">.*?</script>\s*','',h,count=1,flags=re.S)
marker='<!-- RC439 MOBILE LIVE ENTRY TRUE FULLSCREEN LOCK -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block=r'''<!-- RC439 MOBILE LIVE ENTRY TRUE FULLSCREEN LOCK -->
<style id="rc439-mobile-live-entry-true-fullscreen-style">
@media (pointer:coarse){
 #liveCenter:fullscreen,#liveCenter:-webkit-full-screen{background:#000!important;padding:0!important;margin:0!important;width:100vw!important;height:100vh!important;overflow:hidden!important}
 #liveCenter:fullscreen .live-head,#liveCenter:fullscreen .live-footer,#liveCenter:fullscreen .room-back,#liveCenter:fullscreen #returnLobby,#liveCenter:-webkit-full-screen .live-head,#liveCenter:-webkit-full-screen .live-footer,#liveCenter:-webkit-full-screen .room-back,#liveCenter:-webkit-full-screen #returnLobby{display:none!important}
 #liveCenter:fullscreen .center,#liveCenter:fullscreen .live-shell,#liveCenter:fullscreen .live-main,#liveCenter:fullscreen .live-stage,#liveCenter:-webkit-full-screen .center,#liveCenter:-webkit-full-screen .live-shell,#liveCenter:-webkit-full-screen .live-main,#liveCenter:-webkit-full-screen .live-stage{position:absolute!important;inset:0!important;width:100%!important;height:100%!important;max-width:none!important;max-height:none!important;margin:0!important;padding:0!important;border:0!important;border-radius:0!important;background:#000!important}
 #liveCenter:fullscreen #rc275LiveFrame,#liveCenter:-webkit-full-screen #rc275LiveFrame{position:absolute!important;inset:0!important;width:100%!important;height:100%!important;border:0!important;border-radius:0!important;background:#000!important}
}
</style>
<script id="rc439-mobile-live-entry-true-fullscreen-lock">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const isLiveCard=e=>!!e.target?.closest?.('#rc414MobilePortals [data-rc414-room="Live Center"],#portals .portal[data-room="Live Center"],#portals .portal[data-mobile-room="Live Center"]');
 const room=()=>document.getElementById('liveCenter');
 const enter=e=>{
  if(!isLiveCard(e)||document.fullscreenElement||document.webkitFullscreenElement)return;
  const r=room();if(!r)return;
  try{
   const p=r.requestFullscreen?.({navigationUI:'hide'})||r.webkitRequestFullscreen?.();
   if(p?.then)p.then(()=>screen.orientation?.lock?.('landscape')).catch(()=>{});
  }catch(_){}
 };
 // Capture phase: runs inside the exact portal tap before RC414 defers room opening.
 document.addEventListener('click',enter,true);
 document.addEventListener('pointerup',enter,true);
 document.addEventListener('touchend',enter,{capture:true,passive:true});
 const unlock=()=>{const f=document.fullscreenElement||document.webkitFullscreenElement;if(!f)try{screen.orientation?.unlock?.()}catch(_){}};
 document.addEventListener('fullscreenchange',unlock,true);
 document.addEventListener('webkitfullscreenchange',unlock,true);
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
for locked in ('RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
