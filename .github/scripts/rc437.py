from pathlib import Path
import re

p=Path('public/index.html')
h=p.read_text(encoding='utf-8')

# Live Center mobile only. Remove RC400's viewport/CSS pseudo-fullscreen authority;
# it cannot hide browser chrome and competes with the native player fullscreen path.
h,n=re.subn(r'<!-- RC400 MASTER MOBILE LIVE FULLSCREEN AUTHORITY -->.*?</script>\s*', '', h, count=1, flags=re.S)
if n!=1:
    raise SystemExit(f'expected one RC400 authority block, found {n}')

# RC436 was only a trigger repair for RC400; remove its marker with that authority.
h=h.replace('<!-- RC436 MOBILE LIVE LANDSCAPE AUTHORITY TRIGGER REPAIR -->\n','',1)

marker='<!-- RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY -->'
block='''<!-- RC437 MOBILE LIVE NATIVE FULLSCREEN AUTHORITY -->
<script id="rc437-mobile-live-native-fullscreen-authority">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const live=()=>document.getElementById('liveCenter')?.classList.contains('active');
 const frame=()=>document.getElementById('rc275LiveFrame');
 const authorize=()=>{
  const f=frame();if(!f)return null;
  f.allowFullscreen=true;
  f.setAttribute('allowfullscreen','');
  f.setAttribute('webkitallowfullscreen','');
  f.setAttribute('allow','autoplay; fullscreen; picture-in-picture');
  return f;
 };
 const sync=()=>{
  if(!live())return;
  authorize();
  // Native player fullscreen is the only true fullscreen authority.
  // Browser policy requires a user activation for entering fullscreen;
  // orientation events alone cannot legally force it.
 };
 const host=document.getElementById('liveCenter')||document.body;
 new MutationObserver(sync).observe(host,{subtree:true,childList:true,attributes:true,attributeFilter:['class']});
 window.addEventListener('orientationchange',sync,{passive:true});
 screen.orientation?.addEventListener?.('change',sync);
 window.addEventListener('resize',sync,{passive:true});
 authorize();sync();
})();
</script>
'''
if marker not in h:
    anchor='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
    if h.count(anchor)!=1: raise SystemExit(f'expected one RC433 anchor, found {h.count(anchor)}')
    h=h.replace(anchor,block+anchor,1)

# Locked-room invariants: refuse to write if they disappeared.
for locked in ('RC418 THEATER FULLSCREEN EXIT ISOLATION','RC417 NATIVE THEATER FULLSCREEN ONLY','RC414 MOBILE CINEMATIC PORTALS REBUILD'):
    if locked not in h: raise SystemExit('missing locked marker: '+locked)

p.write_text(h,encoding='utf-8')
