from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
if 'RC414 MOBILE CINEMATIC PORTALS REBUILD' in h: raise SystemExit(0)
# Kill stale delayed room-enforcement callbacks: they can reopen/force scenes after Back.
h=re.sub(r"\n    \[80,300,700,1400\]\.forEach\(ms=>setTimeout\(\(\)=>\{.*?\n    \},ms\)\);",'',h,count=1,flags=re.S)
# Expose the cleaned RC342 room function only to the new isolated mobile portal UI.
needle="  const replace=(el)=>{"
if needle not in h: raise SystemExit('RC342 replace anchor missing')
h=h.replace(needle,"  window.scRc414OpenRoom=(room)=>openRoom(room,null);\n"+needle,1)
# New UI is outside old #portals so the historical portal-card router cannot claim its taps.
block=r'''<!-- RC414 MOBILE CINEMATIC PORTALS REBUILD -->
<style id="rc414-mobile-cinematic-portals-style">
#rc414MobilePortals{display:none}
@media(max-width:700px){
 body[data-experience="portal_mode"] #portals{display:none!important;pointer-events:none!important}
 body[data-experience="portal_mode"] #rc414MobilePortals{display:block;position:fixed;inset:0;z-index:2147482000;background:radial-gradient(circle at 72% 5%,rgba(217,183,96,.13),transparent 25%),linear-gradient(180deg,#090806,#020202 35%,#000);overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;color:#f6f0df;padding:22px 16px 34px}
 #rc414MobilePortals .rc414-head{display:flex;align-items:center;justify-content:space-between;padding:4px 2px 18px;border-bottom:1px solid rgba(217,183,96,.18);margin-bottom:15px}
 #rc414MobilePortals .rc414-brand{font:400 25px/1 Georgia,serif;letter-spacing:.16em;background:linear-gradient(#fff1c4,#d9b760 55%,#8d6823);-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:0 0 25px rgba(217,183,96,.12)}
 #rc414MobilePortals .rc414-seal{width:38px;height:38px;border:1px solid rgba(217,183,96,.52);border-radius:50%;display:grid;place-items:center;font:italic 17px Georgia,serif;color:#e4c46d;box-shadow:0 0 20px rgba(217,183,96,.10)}
 #rc414MobilePortals .rc414-kicker{font:700 8px/1.5 Inter,Arial,sans-serif;letter-spacing:.34em;color:rgba(217,183,96,.72);margin:0 3px 14px}
 #rc414MobilePortals .rc414-list{display:grid;gap:13px}
 #rc414MobilePortals .rc414-card{position:relative;display:block;width:100%;min-height:122px;padding:0;overflow:hidden;border:1px solid rgba(217,183,96,.30);border-radius:19px;background:#080705;box-shadow:0 16px 42px rgba(0,0,0,.46),inset 0 1px 0 rgba(255,240,193,.05);text-align:left;isolation:isolate;transform:translateZ(0)}
 #rc414MobilePortals .rc414-card::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(0,0,0,.96) 0%,rgba(0,0,0,.76) 47%,rgba(0,0,0,.18) 100%)}
 #rc414MobilePortals .rc414-card::before{content:"";position:absolute;inset:0;z-index:-2;background:var(--rc414bg) center/cover no-repeat;filter:saturate(.72) brightness(.62);transform:scale(1.025);transition:transform .8s cubic-bezier(.16,1,.3,1),filter .5s}
 #rc414MobilePortals .rc414-card:active{transform:scale(.986);border-color:rgba(244,211,116,.82)}
 #rc414MobilePortals .rc414-card:active::before{transform:scale(1.07);filter:saturate(.88) brightness(.72)}
 #rc414MobilePortals .rc414-copy{display:flex;min-height:122px;flex-direction:column;justify-content:center;align-items:flex-start;padding:18px 58px 18px 20px;position:relative;z-index:2}
 #rc414MobilePortals .rc414-copy small{font:700 7px/1 Inter,Arial,sans-serif;letter-spacing:.28em;color:#d9b760;margin-bottom:8px}
 #rc414MobilePortals .rc414-copy strong{font:400 24px/1.04 Georgia,serif;letter-spacing:.035em;color:#fff1c8;text-shadow:0 4px 18px #000}
 #rc414MobilePortals .rc414-copy span{margin-top:8px;max-width:235px;font:400 10px/1.45 Georgia,serif;letter-spacing:.035em;color:rgba(255,255,255,.62)}
 #rc414MobilePortals .rc414-arrow{position:absolute;right:17px;top:50%;z-index:3;transform:translateY(-50%);width:34px;height:34px;border:1px solid rgba(229,194,98,.64);border-radius:50%;display:grid;place-items:center;color:#e9c966;background:rgba(0,0,0,.48);font:18px Georgia,serif;box-shadow:0 0 22px rgba(217,183,96,.12)}
 #rc414MobilePortals .rc414-foot{text-align:center;padding:25px 8px 6px;font:400 10px Georgia,serif;letter-spacing:.18em;color:rgba(217,183,96,.48)}
}
</style>
<div id="rc414MobilePortals" aria-label="SoulCinema Rooms">
 <div class="rc414-head"><div class="rc414-brand">SOULCINEMA</div><div class="rc414-seal">S</div></div>
 <div class="rc414-kicker">EVERY HEART HIDES A STORY · EXPLORE THE ROOMS</div>
 <div class="rc414-list">
  <button class="rc414-card" data-rc414-room="Screening Theater" style="--rc414bg:url('https://tfamln4qsost6j00.public.blob.vercel-storage.com/mwen-poukont-mwen.png')"><span class="rc414-copy"><small>FEATURED PREMIERE</small><strong>MWEN POUKONT MWEN</strong><span>Enter the Screening Theater · Film & Stories</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="Music Room" style="--rc414bg:url('https://tfamln4qsost6j00.public.blob.vercel-storage.com/mwen-poukont-mwen.png')"><span class="rc414-copy"><small>LISTEN · DISCOVER</small><strong>MUSIC ROOM</strong><span>SoulCinema Music Discovery · Lyrics & Credits</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="Live Center"><span class="rc414-copy"><small>ON AIR · EVENTS</small><strong>LIVE CENTER</strong><span>Live broadcasts · Premieres · Replay archive</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="Production Room"><span class="rc414-copy"><small>BEHIND THE STORY</small><strong>PRODUCTION ROOM</strong><span>Behind the scenes · Storyboards · Director notes</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="Story Room"><span class="rc414-copy"><small>ORIGINAL STORIES</small><strong>STORY ROOM</strong><span>Discover the human stories behind SoulCinema</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="Visual Bible"><span class="rc414-copy"><small>THE WORLD OF SOULCINEMA</small><strong>VISUAL BIBLE</strong><span>Identity · Atmosphere · Cinematic language</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="About Us"><span class="rc414-copy"><small>THE STUDIO</small><strong>ABOUT US</strong><span>Our mission · Every Heart Hides a Story</span></span><b class="rc414-arrow">›</b></button>
  <button class="rc414-card" data-rc414-room="Contact"><span class="rc414-copy"><small>CONNECT</small><strong>CONTACT US</strong><span>Reach SoulCinema Studio</span></span><b class="rc414-arrow">›</b></button>
 </div>
 <div class="rc414-foot">EVERY HEART HIDES A STORY · SOULCINEMA.STUDIO</div>
</div>
<script id="rc414-mobile-cinematic-portals-controller">
(()=>{
 if(!matchMedia('(max-width:700px)').matches)return;
 const root=document.getElementById('rc414MobilePortals');
 if(!root)return;
 let busy=false;
 root.addEventListener('click',e=>{
   const card=e.target.closest('[data-rc414-room]');
   if(!card||busy||document.body.dataset.experience!=='portal_mode')return;
   e.preventDefault();e.stopPropagation();
   busy=true;
   const room=card.dataset.rc414Room;
   requestAnimationFrame(()=>{
     try{window.scRc414OpenRoom?.(room)}finally{setTimeout(()=>busy=false,320)}
   });
 },false);
 const release=()=>{busy=false};
 window.addEventListener('pageshow',release);
 new MutationObserver(()=>{if(document.body.dataset.experience==='portal_mode')release()}).observe(document.body,{attributes:true,attributeFilter:['data-experience']});
})();
</script>
'''
# Insert before RC393, safely after RC342 closes.
anchor='<script id="rc393-desktop-live-src-reset-guard">'
if anchor not in h: raise SystemExit('RC393 anchor missing')
h=h.replace(anchor,block+'\n'+anchor,1)
p.write_text(h,encoding='utf-8')
