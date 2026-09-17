from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC430 MOBILE-ONLY LIVE FULLSCREEN RECOVERY -->'
if marker in h: raise SystemExit('already patched')
# Remove failed RC429 bridge only; keep RC400 layout authority and all desktop code untouched.
s=h.find('<!-- RC429 LIVE FULLSCREEN USER-ACTIVATION BRIDGE -->')
if s!=-1:
    e=h.find('</script>',s)
    if e!=-1:h=h[:s]+h[e+9:]
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
patch=r'''<!-- RC430 MOBILE-ONLY LIVE FULLSCREEN RECOVERY -->
<script id="rc430-mobile-only-live-fullscreen-recovery">
(()=>{
 const mobile=()=>matchMedia('(pointer:coarse)').matches&&Math.max(screen.width,screen.height)<=1400;
 const live=()=>document.body?.dataset.liveMode==='live'&&document.getElementById('liveCenter')?.classList.contains('active');
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 const frame=()=>document.getElementById('rc275LiveFrame');
 let armed=false;
 const prep=()=>{const f=frame();if(!f)return null;f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');const a=f.getAttribute('allow')||'';if(!/fullscreen/i.test(a))f.setAttribute('allow',(a?a+'; ':'')+'fullscreen *');return f};
 const enter=()=>{if(!mobile()||!live()||!landscape()||document.fullscreenElement||document.webkitFullscreenElement)return;const f=prep();if(!f)return;try{const q=f.requestFullscreen?.({navigationUI:'hide'})||f.webkitRequestFullscreen?.();q?.catch?.(()=>{})}catch(_){}};
 const arm=e=>{if(!mobile()||!live())return;const f=frame(),stage=f?.parentElement;if(!f||!(e.target===f||stage?.contains?.(e.target)))return;armed=true;if(landscape())enter()};
 document.addEventListener('pointerdown',arm,true);
 document.addEventListener('touchstart',arm,{capture:true,passive:true});
 const sync=()=>{if(!mobile()||!live())return;if(landscape()&&armed)enter()};
 window.addEventListener('orientationchange',()=>setTimeout(sync,60));
 screen.orientation?.addEventListener?.('change',()=>setTimeout(sync,60));
 prep();
})();
</script>
'''
h=h.replace(anchor,patch+anchor,1)
p.write_text(h,encoding='utf-8')
