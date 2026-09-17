from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC415 MOBILE THEATER FULLSCREEN STABILITY -->'
if marker in h: raise SystemExit('already patched')
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
block=r'''<!-- RC415 MOBILE THEATER FULLSCREEN STABILITY -->
<script id="rc415-mobile-theater-fullscreen-stability">
(()=>{
 const mobile=()=>matchMedia('(max-width:860px)').matches;
 const v=()=>document.getElementById('theaterPlayer');
 const active=()=>document.getElementById('screeningTheater')?.classList.contains('active');
 let native=false;
 const sync=()=>{const x=v();native=!!(document.fullscreenElement||document.webkitFullscreenElement||x?.webkitDisplayingFullscreen);document.body.classList.toggle('rc415-native-theater-fullscreen',native&&active());};
 document.addEventListener('fullscreenchange',sync,true);
 document.addEventListener('webkitfullscreenchange',sync,true);
 document.addEventListener('click',e=>{if(!mobile()||!active())return;const x=v();if(!x)return;if(e.target===x||e.target?.closest?.('.theater-screen-frame'))requestAnimationFrame(sync);},true);
 window.addEventListener('orientationchange',()=>{if(native)return;},true);
 window.addEventListener('resize',()=>{if(native)return;},true);
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
