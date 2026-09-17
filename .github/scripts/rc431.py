from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC431 MOBILE LIVE IFRAME FULLSCREEN PERMISSION -->'
if marker in h: raise SystemExit('already patched')
# Remove failed RC430 gesture override. RC400 remains the locked mobile layout/exit authority.
s=h.find('<!-- RC430 MOBILE-ONLY LIVE FULLSCREEN RECOVERY -->')
if s!=-1:
    e=h.find('</script>',s)
    if e!=-1:h=h[:s]+h[e+9:]
anchor='<!-- RC404 MOBILE THEATER PREMIERE REVEAL -->'
if anchor not in h: raise SystemExit('anchor missing')
patch=r'''<!-- RC431 MOBILE LIVE IFRAME FULLSCREEN PERMISSION -->
<script id="rc431-mobile-live-iframe-fullscreen-permission">
(()=>{
 if(!matchMedia('(pointer:coarse)').matches)return;
 const authorize=()=>{
   const f=document.getElementById('rc275LiveFrame');
   if(!f)return false;
   f.allowFullscreen=true;
   f.setAttribute('allowfullscreen','');
   f.setAttribute('webkitallowfullscreen','');
   const a=f.getAttribute('allow')||'';
   if(!/fullscreen/i.test(a))f.setAttribute('allow',(a?a+'; ':'')+'fullscreen *');
   return true;
 };
 // The live iframe is created after page load. Authorize it at insertion time so its own fullscreen control has permission.
 if(authorize())return;
 const host=document.getElementById('liveCenter')||document.body;
 const mo=new MutationObserver(()=>{if(authorize())mo.disconnect()});
 mo.observe(host,{childList:true,subtree:true});
})();
</script>
'''
h=h.replace(anchor,patch+anchor,1)
p.write_text(h,encoding='utf-8')
