from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC419 SEAMLESS THEATER PREMIERE HANDOFF -->'
if marker in h: raise SystemExit('already patched')
anchor='</body>'
if anchor not in h: raise SystemExit('body anchor missing')
block=r'''<!-- RC419 SEAMLESS THEATER PREMIERE HANDOFF -->
<style id="rc419-seamless-theater-handoff-style">
#screeningTheater.rc419-handoff #theaterPlayer{opacity:1!important;visibility:visible!important;background:#000!important}
#screeningTheater.rc419-handoff #theaterPoster{opacity:0!important;visibility:hidden!important;pointer-events:none!important}
</style>
<script id="rc419-seamless-theater-premiere-handoff">
(()=>{
 const v=document.getElementById('theaterPlayer');
 const room=document.getElementById('screeningTheater');
 if(!v||!room)return;
 const FILM='https://tfamln4qsost6j00.public.blob.vercel-storage.com/mwen-poukont-mwen-film.mp4';
 let armed=false,swapping=false;
 const isOpening=()=>{const s=(v.currentSrc||v.src||'').toLowerCase();return s.includes('featured-premiere.mp4')};
 const preload=document.createElement('video');
 preload.preload='auto'; preload.muted=true; preload.playsInline=true; preload.src=FILM;
 try{preload.load()}catch(e){}
 const swap=()=>{
   if(swapping||!isOpening())return;
   swapping=true; room.classList.add('rc419-handoff');
   v.src=FILM;
   v.load();
   const go=()=>{v.removeEventListener('canplay',go);v.removeEventListener('loadeddata',go);const q=v.play();if(q&&q.catch)q.catch(()=>{});setTimeout(()=>room.classList.remove('rc419-handoff'),180);swapping=false};
   v.addEventListener('loadeddata',go,{once:true});
   v.addEventListener('canplay',go,{once:true});
 };
 v.addEventListener('timeupdate',()=>{
   if(!isOpening()||!Number.isFinite(v.duration)||v.duration<=0)return;
   const left=v.duration-v.currentTime;
   if(left<1.25&&!armed){armed=true;try{preload.play().then(()=>{preload.pause();preload.currentTime=0}).catch(()=>{})}catch(e){}}
   if(left<=0.12)swap();
 },true);
 v.addEventListener('ended',swap,true);
 v.addEventListener('loadedmetadata',()=>{if(isOpening()){armed=false;swapping=false}},true);
})();
</script>
'''
h=h.replace(anchor,block+anchor,1)
p.write_text(h,encoding='utf-8')
