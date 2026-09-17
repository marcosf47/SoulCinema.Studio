from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# RC420: remove only failed RC419 handoff authority; restore prior proven RC404 handoff engine.
h,n=re.subn(r'<!-- RC419 SEAMLESS THEATER PREMIERE HANDOFF -->\s*<style id="rc419-seamless-theater-handoff-style">.*?</style>\s*<script id="rc419-seamless-theater-premiere-handoff">.*?</script>\s*','',h,flags=re.S)
if n!=1: raise SystemExit(f'expected one RC419 block, found {n}')
marker='<!-- RC420 RESTORE PROVEN THEATER HANDOFF -->\n'
if marker.strip() in h: raise SystemExit('already patched')
h=h.replace('</body>',marker+'</body>',1)
p.write_text(h,encoding='utf-8')
