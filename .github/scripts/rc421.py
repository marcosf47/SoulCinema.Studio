from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC421 THEATER HANDOFF VISUAL MASK -->'
if marker in h: raise SystemExit('already patched')
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
block=r'''<!-- RC421 THEATER HANDOFF VISUAL MASK -->
<style id="rc421-theater-handoff-visual-mask-style">
#screeningTheater.rc421-handoff-mask #theaterPlayer{opacity:0!important;visibility:hidden!important}
#screeningTheater.rc421-handoff-mask .theater-screen-frame{background:#000!important}
</style>
<script id="rc421-theater-handoff-visual-mask">
(()=>{
 const v=document.getElementById('theaterPlayer');
 const room=document.getElementById('screeningTheater');
 if(!v||!room)return;
 const OPEN='featured-premiere.mp4';
 const FILM='mwen-poukont-mwen-film.mp4';
 let masking=false;
 const src=()=>String(v.currentSrc||v.src||'').toLowerCase();
 const mask=()=>{if(masking)return;masking=true;room.classList.add('rc421-handoff-mask')};
 const reveal=()=>{if(!masking)return;requestAnimationFrame(()=>requestAnimationFrame(()=>{room.classList.remove('rc421-handoff-mask');masking=false}))};
 v.addEventListener('ended',()=>{if(src().includes(OPEN))mask()},true);
 v.addEventListener('loadstart',()=>{if(src().includes(FILM))mask()},true);
 v.addEventListener('playing',()=>{if(src().includes(FILM))reveal()},true);
 v.addEventListener('error',()=>{room.classList.remove('rc421-handoff-mask');masking=false},true);
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
