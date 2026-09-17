from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC426 RESTORE LOCKED MOBILE LIVE FULLSCREEN -->'
if marker in h: raise SystemExit('already patched')
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
patch=r'''<!-- RC426 RESTORE LOCKED MOBILE LIVE FULLSCREEN -->
<style id="rc426-restore-mobile-live-fullscreen">
@media (pointer:coarse) and (orientation:landscape) and (max-height:700px){
 body.rc426-live-fullscreen #liveCenter.active,
 body.rc426-live-fullscreen #liveCenter.active .center,
 body.rc426-live-fullscreen #liveCenter.active .center>div,
 body.rc426-live-fullscreen #liveCenter.active .center>div>div:nth-of-type(3){position:fixed!important;inset:0!important;width:100vw!important;height:100dvh!important;max-width:none!important;max-height:none!important;margin:0!important;padding:0!important;border:0!important;border-radius:0!important;background:#000!important;box-shadow:none!important;overflow:hidden!important}
 body.rc426-live-fullscreen #liveCenter.active #liveMain{position:fixed!important;inset:0!important;width:100vw!important;height:100dvh!important;max-width:none!important;max-height:none!important;margin:0!important;padding:0!important;border:0!important;border-radius:0!important;background:#000!important}
 body.rc426-live-fullscreen #liveCenter.active #livePlayerWrap,
 body.rc426-live-fullscreen #liveCenter.active #rc275LiveFrame{display:block!important;visibility:visible!important;opacity:1!important;position:absolute!important;inset:0!important;width:100%!important;height:100%!important;max-width:none!important;max-height:none!important;margin:0!important;padding:0!important;border:0!important;border-radius:0!important;background:#000!important;pointer-events:auto!important}
 body.rc426-live-fullscreen #liveCenter.active .eyebrow,
 body.rc426-live-fullscreen #liveCenter.active h2,
 body.rc426-live-fullscreen #liveCenter.active #liveState,
 body.rc426-live-fullscreen #liveCenter.active #publicLiveBadge,
 body.rc426-live-fullscreen #liveCenter.active #liveControls,
 body.rc426-live-fullscreen #liveCenter.active #liveRouteStatus,
 body.rc426-live-fullscreen #liveCenter.active #returnLobby{display:none!important;visibility:hidden!important;opacity:0!important;pointer-events:none!important}
}
</style>
<script id="rc426-restore-mobile-live-fullscreen-runtime">
(()=>{
 const eligible=()=>matchMedia('(pointer:coarse) and (orientation:landscape) and (max-height:700px)').matches;
 const room=()=>document.getElementById('liveCenter');
 const sync=()=>document.body.classList.toggle('rc426-live-fullscreen',!!(eligible()&&room()?.classList.contains('active')));
 const r=room();if(r)new MutationObserver(sync).observe(r,{attributes:true,attributeFilter:['class']});
 addEventListener('orientationchange',()=>{sync();setTimeout(sync,80);setTimeout(sync,300)},{passive:true});
 addEventListener('resize',sync,{passive:true});
 sync();
})();
</script>
'''
h=h.replace(anchor,patch+anchor,1)
p.write_text(h,encoding='utf-8')
