from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC434 MOBILE LIVE LANDSCAPE FULLSCREEN ENHANCEMENT -->'
if marker in h: raise SystemExit('already patched')
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
patch=r'''<!-- RC434 MOBILE LIVE LANDSCAPE FULLSCREEN ENHANCEMENT -->
<script id="rc434-mobile-live-landscape-fullscreen-enhancement">
(()=>{
 const mobile=()=>matchMedia('(pointer:coarse)').matches&&Math.max(screen.width,screen.height)<=1400;
 const landscape=()=>matchMedia('(orientation:landscape)').matches;
 const room=()=>document.getElementById('liveCenter');
 const frame=()=>document.getElementById('rc275LiveFrame');
 const live=()=>mobile()&&room()?.classList.contains('active')&&document.body?.dataset.liveMode==='live';
 const prep=()=>{const f=frame();if(!f)return null;f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');const a=f.getAttribute('allow')||'';if(!/fullscreen/i.test(a))f.setAttribute('allow',(a?a+'; ':'')+'fullscreen *');return f};
 const enter=()=>{
  if(!live()||!landscape()||document.fullscreenElement||document.webkitFullscreenElement)return;
  const f=prep();if(!f)return;
  try{const q=f.requestFullscreen?.({navigationUI:'hide'})||f.webkitRequestFullscreen?.();q?.catch?.(()=>{})}catch(_){ }
 };
 // Enhancement only: native player fullscreen remains untouched and remains the fallback.
 const sync=()=>{if(!mobile())return;if(live()&&landscape())enter()};
 window.addEventListener('orientationchange',()=>setTimeout(sync,80));
 screen.orientation?.addEventListener?.('change',()=>setTimeout(sync,80));
 window.addEventListener('resize',()=>setTimeout(sync,80),{passive:true});
 new MutationObserver(sync).observe(document.documentElement,{subtree:true,attributes:true,attributeFilter:['class','data-live-mode']});
 prep();sync();
})();
</script>
'''
h=h.replace(anchor,patch+anchor,1)
p.write_text(h,encoding='utf-8')
