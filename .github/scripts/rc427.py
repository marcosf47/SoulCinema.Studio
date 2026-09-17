from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC427 NATIVE LIVE FULLSCREEN ON ENTRY -->'
if marker in h: raise SystemExit('already patched')
patch=r'''<!-- RC427 NATIVE LIVE FULLSCREEN ON ENTRY -->
<script id="rc427-native-live-fullscreen-on-entry">
(()=>{
 const mobile=()=>matchMedia('(pointer:coarse)').matches&&Math.max(screen.width,screen.height)<=1400;
 const frame=()=>document.getElementById('rc275LiveFrame');
 const prep=()=>{const f=frame();if(!f)return null;f.allowFullscreen=true;f.setAttribute('allowfullscreen','');f.setAttribute('webkitallowfullscreen','');const a=f.getAttribute('allow')||'';if(!/fullscreen/i.test(a))f.setAttribute('allow',(a?a+'; ':'')+'fullscreen *');return f};
 const enterNative=()=>{if(!mobile()||document.fullscreenElement||document.webkitFullscreenElement)return;const f=prep();if(!f)return;try{const q=f.requestFullscreen?.({navigationUI:'hide'})||f.webkitRequestFullscreen?.();q?.catch?.(()=>{})}catch(_){}};
 // Claim the same real user gesture that opens Live Center, before mobile browsers expire user activation.
 const isLivePortal=(e)=>{const x=e.target?.closest?.('#portals [data-room="Live Center"],#portals [data-mobile-room="Live Center"]');return !!x};
 document.addEventListener('pointerup',e=>{if(isLivePortal(e))enterNative()},{capture:true});
 document.addEventListener('touchend',e=>{if(isLivePortal(e))enterNative()},{capture:true,passive:true});
 prep();
})();
</script>
'''
h=h.replace('</body>',patch+'\n</body>',1)
p.write_text(h,encoding='utf-8')
