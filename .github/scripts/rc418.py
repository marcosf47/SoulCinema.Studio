from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
old="const sync=()=>{if(!mobile())return;const on=live()&&landscape();document.body.classList.toggle('rc400-live-landscape',on);if(!on&&document.fullscreenElement){document.exitFullscreen?.().catch?.(()=>{})}};"
new="const sync=()=>{if(!mobile())return;const on=live()&&landscape();document.body.classList.toggle('rc400-live-landscape',on);const fs=document.fullscreenElement||document.webkitFullscreenElement;const liveRoom=document.getElementById('liveCenter');if(!on&&fs&&liveRoom?.contains(fs)){document.exitFullscreen?.().catch?.(()=>{})}};"
if old not in h: raise SystemExit('RC400 sync target missing')
h=h.replace(old,new,1)
marker='<!-- RC418 THEATER FULLSCREEN EXIT ISOLATION -->'
if marker not in h:h=h.replace('</body>',marker+'\n</body>',1)
p.write_text(h,encoding='utf-8')
