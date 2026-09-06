const fs=require('fs');
const p='public/index.html';
let s=fs.readFileSync(p,'utf8');
const blob='https://tfamln4qsost6j00.public.blob.vercel-storage.com/';
for(const name of ['the-gate.mp4','grand-lobby.mp4','featured-premiere.mp4','mwen-poukont-mwen-film.mp4','mwen-poukont-mwen.mp3','mwen-poukont-mwen.png','room-307-episode-01-the-envelope.mp4','collection-family-01.mp4','collection-family-02.mp4','collection-nature-01.mp4']){
  s=s.replace(new RegExp("https?://[^'\\\"\\s<>]+/"+name.replace(/[.*+?^${}()|[\\]\\]/g,'\\$&'),'g'),blob+name);
}
s=s.replace(/<div class="story-note">[^<]*<\/div>/,'<div class="story-note"></div>');
s=s.replace(/<div class="production-note">[^<]*<\/div>/,'<div class="production-note"></div>');
s=s.replace(/function primeTheaterOpening\(\)\{[\s\S]*?\n\}\nfunction openTheater/,`function primeTheaterOpening(){
 const v=$('#theaterPlayer');if(!v)return;
 theaterStage='opening';
 const openingLoaded=(v.currentSrc||v.src||'')===THEATER_OPENING_SRC;
 const openingReady=v.dataset.scStage==='opening' && openingLoaded && v.readyState>=2;
 if(openingReady){try{v.currentTime=0}catch(e){}return}
 v.pause();v.preload='auto';
 if(v.dataset.scStage!=='opening' || !openingLoaded){v.src=THEATER_OPENING_SRC;v.dataset.scStage='opening'}
 try{v.load()}catch(e){}
 try{v.currentTime=0}catch(e){}
}
function openTheater`);
s=s.replace(/function handoffToFeature\(\)\{[\s\S]*?\}\nfunction returnFromTheater/,`function handoffToFeature(){const v=$('#theaterPlayer');if(!v||theaterHandoffBusy)return;theaterHandoffBusy=true;$('#theaterStatus').textContent='ENTERING THE STORY';v.classList.remove('theater-handoff','theater-portal-push','theater-feature-enter');loadTheaterStage('film',true);void v.offsetWidth;v.classList.add('theater-feature-enter');$('#theaterStatus').textContent='● NOW PLAYING · MWEN POUKONT MWEN';setTimeout(()=>v.classList.remove('theater-feature-enter'),900);theaterHandoffBusy=false}
function returnFromTheater`);
if(!s.includes('sc-featured-film-prewarm')){
 const block=`\n<script id="sc-featured-film-prewarm">\n(()=>{\n let filmWarmer=null;\n function warmFeaturedFilm(){if(filmWarmer||typeof THEATER_FILM_SRC==='undefined'||!THEATER_FILM_SRC)return;const v=document.createElement('video');v.preload='auto';v.muted=true;v.playsInline=true;v.setAttribute('playsinline','');v.setAttribute('aria-hidden','true');v.style.cssText='position:fixed;width:1px;height:1px;left:-9999px;top:-9999px;opacity:0;pointer-events:none';document.body.appendChild(v);v.src=THEATER_FILM_SRC;try{v.load()}catch(e){}filmWarmer=v}const theaterPlay=document.getElementById('theaterPlay');if(theaterPlay)theaterPlay.addEventListener('click',warmFeaturedFilm,{once:true,capture:true});const theater=document.getElementById('screeningTheater');if(theater&&'MutationObserver' in window){const mo=new MutationObserver(()=>{if(theater.classList.contains('active')){warmFeaturedFilm();mo.disconnect()}});mo.observe(theater,{attributes:true,attributeFilter:['class']})}})();\n</script>\n`;
 s=s.replace('</body>',block+'</body>');
}
fs.writeFileSync(p,s,'utf8');
console.log('MASTER FINAL PATCH APPLIED');
