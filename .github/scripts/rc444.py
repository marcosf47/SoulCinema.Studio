from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Remove only the failed RC443 controller. Preserve locked rooms and native iframe permissions.
h=re.sub(r'<!-- RC443 MOBILE LIVE LANDSCAPE TAP TRUE FULLSCREEN -->\s*<script id="rc443-mobile-live-landscape-tap-true-fullscreen">.*?</script>\s*','',h,count=1,flags=re.S)
marker='<!-- RC444 MOBILE LIVE LANDSCAPE ONE-TOUCH FULLSCREEN GATE -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block=r'''<!-- RC444 MOBILE LIVE LANDSCAPE ONE-TOUCH FULLSCREEN GATE -->
<style id="rc444-mobile-live-landscape-one-touch-style">
@media (pointer:coarse) and (orientation:landscape){
 #rc444LiveFsGate{position:fixed;inset:0;z-index:2147483647;background:transparent;border:0;padding:0;margin:0;display:none;touch-action:manipulation}
 body.rc444-live-fs-armed #rc444LiveFsGate{display:block}
}
</style>
<script id="rc444-mobile-live-landscape-one-touch-fullscreen-gate">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const room=()=>document.getElementById('liveCenter');
 const live=()=>room()?.classList.contains('active');
 const fs=()=>document.fullscreenElement||document.webkitFullscreenElement;
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 let armed=false;
 const authorize=()=>{const f=document.getElementById('rc275LiveFrame');if(f){f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');f.setAttribute('allow','autoplay; fullscreen; picture-in-picture')}};
 const gate=document.createElement('button');
 gate.id='rc444LiveFsGate';gate.type='button';gate.setAttribute('aria-label','Enter Live fullscreen');
 document.body.appendChild(gate);
 const sync=()=>{
  authorize();
  const on=armed&&live()&&landscape()&&!fs();
  document.body.classList.toggle('rc444-live-fs-armed',on);
  if(!live()){armed=false;document.body.classList.remove('rc444-live-fs-armed')}
 };
 const arm=e=>{
  if(!e.target?.closest?.('#rc414MobilePortals [data-rc414-room="Live Center"],#portals .portal[data-room="Live Center"],#portals .portal[data-mobile-room="Live Center"]'))return;
  armed=true;authorize();setTimeout(sync,0);setTimeout(sync,180);
 };
 document.addEventListener('click',arm,true);
 const enter=e=>{
  e.preventDefault();e.stopPropagation();
  if(!armed||!live()||!landscape()||fs())return;
  const r=room();if(!r)return;
  try{
   const p=r.requestFullscreen?.({navigationUI:'hide'})||r.webkitRequestFullscreen?.();
   if(p?.then)p.then(()=>{armed=false;sync()}).catch(()=>sync());
   else{armed=false;sync()}
  }catch(_){sync()}
 };
 gate.addEventListener('pointerup',enter,true);
 gate.addEventListener('click',enter,true);
 const clean=()=>{
  armed=false;document.body.classList.remove('rc444-live-fs-armed','rc400-live-landscape');
  delete document.body.dataset.rc400LiveLandscape;
 };
 document.addEventListener('click',e=>{if(e.target?.closest?.('#liveCenter #returnLobby,#liveCenter .room-back,#liveCenter [data-back-to-lobby]'))clean()},true);
 new MutationObserver(sync).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class','data-experience']});
 addEventListener('orientationchange',()=>setTimeout(sync,80),{passive:true});
 screen.orientation?.addEventListener?.('change',()=>setTimeout(sync,80));
 addEventListener('resize',sync,{passive:true});
 document.addEventListener('fullscreenchange',sync);
 sync();
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
if 'rc443-mobile-live-landscape-tap-true-fullscreen' in h: raise SystemExit('RC443 still present')
for locked in ('RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
