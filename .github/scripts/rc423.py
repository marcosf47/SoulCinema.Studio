from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC423 CLEAN THEATER HANDOFF REVEAL -->'
if marker in h: raise SystemExit('already patched')
old422='''<!-- RC422 THEATER DECODER FRAME GUARD -->\n<script id="rc422-theater-decoder-frame-guard">\n(()=>{\n const v=document.getElementById('theaterPlayer');\n const room=document.getElementById('screeningTheater');\n if(!v||!room)return;\n const FILM='mwen-poukont-mwen-film.mp4';\n const isFilm=()=>String(v.currentSrc||v.src||'').toLowerCase().includes(FILM);\n const hold=()=>room.classList.add('rc421-handoff-mask');\n const release=()=>requestAnimationFrame(()=>requestAnimationFrame(()=>requestAnimationFrame(()=>room.classList.remove('rc421-handoff-mask'))));\n v.addEventListener('loadeddata',()=>{if(isFilm())hold()},true);\n v.addEventListener('canplay',()=>{if(isFilm())hold()},true);\n v.addEventListener('timeupdate',()=>{if(isFilm()&&!v.paused&&v.currentTime>0.045)release()},true);\n v.addEventListener('seeked',()=>{if(isFilm()&&!v.paused&&v.currentTime>0.045)release()},true);\n})();\n</script>\n'''
if old422 not in h: raise SystemExit('RC422 block missing')
h=h.replace(old422,'',1)
old="v.addEventListener('playing',()=>{if(src().includes(FILM))reveal()},true);"
new="""v.addEventListener('playing',()=>{\n  if(!src().includes(FILM))return;\n  const clean=()=>reveal();\n  if(typeof v.requestVideoFrameCallback==='function'){\n    v.requestVideoFrameCallback(()=>v.requestVideoFrameCallback(clean));\n  }else{\n    requestAnimationFrame(()=>requestAnimationFrame(()=>requestAnimationFrame(clean)));\n  }\n },true);"""
if old not in h: raise SystemExit('RC421 playing reveal anchor missing')
h=h.replace(old,new,1)
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
h=h.replace(anchor,marker+'\n'+anchor,1)
p.write_text(h,encoding='utf-8')
