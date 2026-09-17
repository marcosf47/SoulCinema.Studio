from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
block=re.compile(r'<!-- RC434 MOBILE LIVE LANDSCAPE FULLSCREEN ENHANCEMENT -->\s*<script id="rc434-mobile-live-landscape-fullscreen-enhancement">.*?</script>\s*',re.S)
h,n=block.subn('',h,1)
if n!=1: raise SystemExit('RC434 block missing')
if 'RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY' not in h: raise SystemExit('RC433 checkpoint missing')
if 'rc432LiveFullscreen' in h: raise SystemExit('old custom button detected')
p.write_text(h,encoding='utf-8')
