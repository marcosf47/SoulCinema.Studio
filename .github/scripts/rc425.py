from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC425 MOBILE THEATER STAGE GUARD -->'
if marker in h: raise SystemExit('already patched')
# RC404 mobile start can be invoked again while theater stays active; never let it reset a film handoff back to opening.
old="""   if(!mobile())return;
   const theater=document.getElementById('screeningTheater'),v=document.getElementById('theaterPlayer'),poster=document.getElementById('theaterPoster');
   if(!theater?.classList.contains('active')||!v)return;
   try{theaterHandoffBusy=false;theaterStage='opening'}catch(_){}"""
new="""   if(!mobile())return;
   const theater=document.getElementById('screeningTheater'),v=document.getElementById('theaterPlayer'),poster=document.getElementById('theaterPoster');
   if(!theater?.classList.contains('active')||!v)return;
   try{if(theaterStage==='film'||v.dataset.scStage==='film')return;theaterHandoffBusy=false;theaterStage='opening'}catch(_){}"""
if old not in h: raise SystemExit('RC404 mobile start anchor missing')
h=h.replace(old,new,1)
# Keep RC424 as sole handoff authority and distinct film URL.
if "v.src=THEATER_FILM_SRC" not in h: raise SystemExit('RC424 film handoff missing')
if "const THEATER_FILM_SRC='https://tfamln4qsost6j00.public.blob.vercel-storage.com/mwen-poukont-mwen-film.mp4';" not in h: raise SystemExit('film source missing')
h=h.replace('</body>',marker+'\n</body>',1)
p.write_text(h,encoding='utf-8')
