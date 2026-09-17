from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC429 LIVE FULLSCREEN USER-ACTIVATION BRIDGE -->'
if marker in h: raise SystemExit('already patched')
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
patch=r'''<!-- RC429 LIVE FULLSCREEN USER-ACTIVATION BRIDGE -->
<script id="rc429-live-fullscreen-user-activation-bridge">
(()=>{
 const mobile=()=>matchMedia('(pointer:coarse)').matches&&Math.max(screen.width,screen.height)<=1400;
 const live=()=>document.body?.dataset.liveMode==='live'&&document.getElementById('liveCenter')?.classList.contains('active');
 const frame=()=>document.getElementById('rc275LiveFrame');
 const request=()=>{
   if(!mobile()||!live()||document.fullscreenElement||document.webkitFullscreenElement)return;
   const f=frame();if(!f)return;
   f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');
   try{const q=f.requestFullscreen?.({navigationUI:'hide'})||f.webkitRequestFullscreen?.();q?.catch?.(()=>{})}catch(_){}
 };
 // RC400 already owns layout/exit. This only restores the proven user-gesture trigger on the live stage.
 document.addEventListener('pointerup',e=>{const f=frame(),stage=f?.parentElement;if(f&&stage?.contains?.(e.target))request()},{capture:true});
 document.addEventListener('touchend',e=>{const f=frame(),stage=f?.parentElement;if(f&&stage?.contains?.(e.target))request()},{capture:true,passive:true});
})();
</script>
'''
h=h.replace(anchor,patch+anchor,1)
p.write_text(h,encoding='utf-8')
