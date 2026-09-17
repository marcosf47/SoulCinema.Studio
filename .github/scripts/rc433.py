from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Remove RC432 custom Live fullscreen UI and authority completely.
h=re.sub(r'<!-- RC432 DIRECT MOBILE LIVE FULLSCREEN -->\s*<style id="rc432-direct-mobile-live-fullscreen-style">.*?</style>\s*<script id="rc432-direct-mobile-live-fullscreen">.*?</script>\s*','',h,flags=re.S)
# Remove failed post-RC418 Live fullscreen experiments if any survived.
for n in (429,430,431):
    h=re.sub(rf'<!-- RC{n}[^>]*LIVE[^>]*-->\s*(?:<style[^>]*>.*?</style>\s*)?(?:<script[^>]*>.*?</script>\s*)?','',h,flags=re.S|re.I)
marker='<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->'
if marker in h: raise SystemExit('already patched')
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
block=r'''<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->
<script id="rc433-native-mobile-live-fullscreen-only">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const authorize=()=>{
  const f=document.getElementById('rc275LiveFrame');if(!f)return false;
  f.allowFullscreen=true;
  f.setAttribute('allowfullscreen','');
  f.setAttribute('webkitallowfullscreen','');
  f.setAttribute('allow','autoplay; fullscreen; picture-in-picture');
  return true;
 };
 if(!authorize()){
  const host=document.getElementById('liveCenter')||document.body;
  const mo=new MutationObserver(()=>{if(authorize())mo.disconnect()});
  mo.observe(host,{childList:true,subtree:true});
 }
 // Native iframe/player fullscreen control is the sole Live fullscreen button.
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
