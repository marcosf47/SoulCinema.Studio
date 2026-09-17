from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Remove RC416 custom fullscreen UI/authority completely.
h=re.sub(r'<!-- RC416 DIRECT MOBILE THEATER FULLSCREEN -->\s*<style id="rc416-direct-mobile-theater-fullscreen-style">.*?</style>\s*<script id="rc416-direct-mobile-theater-fullscreen">.*?</script>\s*','',h,flags=re.S)
# Remove RC415 tracker too: native video controls become sole theater fullscreen authority.
h=re.sub(r'<!-- RC415 MOBILE THEATER FULLSCREEN STABILITY -->\s*<script id="rc415-mobile-theater-fullscreen-stability">.*?</script>\s*','',h,flags=re.S)
marker='<!-- RC417 NATIVE THEATER FULLSCREEN ONLY -->'
if marker in h: raise SystemExit('already patched')
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
block=r'''<!-- RC417 NATIVE THEATER FULLSCREEN ONLY -->
<script id="rc417-native-theater-fullscreen-only">
(()=>{
 const v=document.getElementById('theaterPlayer');
 if(!v)return;
 // Keep browser-native video controls/fullscreen button. No custom fullscreen button,
 // no orientation/resize fullscreen authority, and no forced fullscreen exit.
 v.setAttribute('controls','');
 v.setAttribute('playsinline','');
 v.setAttribute('webkit-playsinline','');
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
