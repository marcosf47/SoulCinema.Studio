from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC422 THEATER DECODER FRAME GUARD -->'
if marker in h: raise SystemExit('already patched')
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
block=r'''<!-- RC422 THEATER DECODER FRAME GUARD -->
<script id="rc422-theater-decoder-frame-guard">
(()=>{
 const v=document.getElementById('theaterPlayer');
 const room=document.getElementById('screeningTheater');
 if(!v||!room)return;
 const FILM='mwen-poukont-mwen-film.mp4';
 const isFilm=()=>String(v.currentSrc||v.src||'').toLowerCase().includes(FILM);
 const hold=()=>room.classList.add('rc421-handoff-mask');
 const release=()=>requestAnimationFrame(()=>requestAnimationFrame(()=>requestAnimationFrame(()=>room.classList.remove('rc421-handoff-mask'))));
 v.addEventListener('loadeddata',()=>{if(isFilm())hold()},true);
 v.addEventListener('canplay',()=>{if(isFilm())hold()},true);
 v.addEventListener('timeupdate',()=>{if(isFilm()&&!v.paused&&v.currentTime>0.045)release()},true);
 v.addEventListener('seeked',()=>{if(isFilm()&&!v.paused&&v.currentTime>0.045)release()},true);
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
