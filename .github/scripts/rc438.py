from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC438 MOBILE LIVE FULLSCREEN HOLD GUARD -->'
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit('RC433 anchor mismatch')
    block='''<!-- RC438 MOBILE LIVE FULLSCREEN HOLD GUARD -->
<script id="rc438-mobile-live-fullscreen-hold-guard">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const live=()=>document.getElementById('liveCenter')?.classList.contains('active');
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 const frame=()=>document.getElementById('rc275LiveFrame');
 const fs=()=>document.fullscreenElement||document.webkitFullscreenElement;
 const prep=()=>{const f=frame();if(!f)return null;f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');f.setAttribute('allow','autoplay; fullscreen; picture-in-picture');return f};
 const hold=()=>{
  if(!live()||!landscape())return;
  const f=prep();if(!f||fs())return;
  // Re-entry can only succeed while the browser still exposes user activation.
  if(navigator.userActivation?.isActive){try{const p=f.requestFullscreen?.({navigationUI:'hide'})||f.webkitRequestFullscreen?.();p?.catch?.(()=>{})}catch(_){}}
 };
 document.addEventListener('fullscreenchange',hold,true);
 document.addEventListener('webkitfullscreenchange',hold,true);
 document.addEventListener('pointerup',hold,true);
 document.addEventListener('touchend',hold,{capture:true,passive:true});
 window.addEventListener('orientationchange',hold,{passive:true});
 screen.orientation?.addEventListener?.('change',hold);
})();
</script>
'''
    h=h.replace(anchor,block+anchor,1)
for locked in ('RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY','RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)
p.write_text(h,encoding='utf-8')
