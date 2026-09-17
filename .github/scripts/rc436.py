from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
old="const live=()=>document.body?.dataset.liveMode==='live'&&document.getElementById('liveCenter')?.classList.contains('active');"
new="const live=()=>{const r=document.getElementById('liveCenter');return !!(r?.classList.contains('active')&&document.getElementById('rc275LiveFrame'))};"
if h.count(old)!=1: raise SystemExit(f'expected one RC400 live trigger, found {h.count(old)}')
h=h.replace(old,new,1)
marker='<!-- RC436 MOBILE LIVE LANDSCAPE AUTHORITY TRIGGER REPAIR -->'
if marker not in h:
 h=h.replace('<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->',marker+'\n<!-- RC433 NATIVE MOBILE LIVE FULLSCREEN ONLY -->',1)
p.write_text(h,encoding='utf-8')
