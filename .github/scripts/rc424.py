from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC424 DISTINCT FEATURE FILM HANDOFF -->'
if marker in h: raise SystemExit('already patched')
old="function handoffToFeature(){const v=$('#theaterPlayer');if(!v||theaterHandoffBusy)return;theaterHandoffBusy=true;$('#theaterStatus').textContent='ENTERING THE STORY';v.classList.remove('theater-handoff','theater-portal-push','theater-feature-enter');loadTheaterStage('film',true);void v.offsetWidth;v.classList.add('theater-feature-enter');$('#theaterStatus').textContent='● NOW PLAYING · MWEN POUKONT MWEN';setTimeout(()=>v.classList.remove('theater-feature-enter'),900);theaterHandoffBusy=false}"
new="""function handoffToFeature(){const v=$('#theaterPlayer');if(!v||theaterHandoffBusy)return;theaterHandoffBusy=true;$('#theaterStatus').textContent='ENTERING THE STORY';screeningTheater.classList.add('rc421-handoff-mask');v.pause();v.classList.remove('theater-handoff','theater-portal-push','theater-feature-enter');theaterStage='film';v.dataset.scStage='film';v.removeAttribute('src');v.src=THEATER_FILM_SRC;v.preload='auto';v.load();const reveal=()=>{const show=()=>{screeningTheater.classList.remove('rc421-handoff-mask');v.classList.add('theater-feature-enter');setTimeout(()=>v.classList.remove('theater-feature-enter'),900)};if(typeof v.requestVideoFrameCallback==='function'){v.requestVideoFrameCallback(()=>v.requestVideoFrameCallback(show))}else{requestAnimationFrame(()=>requestAnimationFrame(show))}};v.addEventListener('playing',reveal,{once:true});v.muted=false;const q=v.play();if(q&&q.catch)q.catch(()=>{v.muted=true;v.play().catch(()=>{})});$('#theaterStatus').textContent='● NOW PLAYING · MWEN POUKONT MWEN';setTimeout(()=>{theaterHandoffBusy=false},1200)}"""
if old not in h: raise SystemExit('handoff anchor missing')
h=h.replace(old,new,1)
# Remove the hidden prewarm video: it can duplicate/compete on mobile.
start=h.find('<script id="sc-featured-film-prewarm">')
if start!=-1:
    end=h.find('</script>',start)
    if end!=-1:h=h[:start]+h[end+9:]
# Ensure exact distinct source constants remain.
opening="const THEATER_OPENING_SRC='https://tfamln4qsost6j00.public.blob.vercel-storage.com/featured-premiere.mp4';"
film="const THEATER_FILM_SRC='https://tfamln4qsost6j00.public.blob.vercel-storage.com/mwen-poukont-mwen-film.mp4';"
if opening not in h or film not in h: raise SystemExit('distinct source constants missing')
h=h.replace('</body>',marker+'\n</body>',1)
p.write_text(h,encoding='utf-8')
