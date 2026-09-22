const FEED="https://live.soulcinema.studio/soulcinemad-opus/?controls=false&muted=true&autoplay=false&playsInline=true";

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  const ctl=new AbortController();
  const tm=setTimeout(()=>ctl.abort(),6500);
  try{
    const r=await fetch(FEED+"&_sc="+Date.now(),{cache:"no-store",redirect:"follow",signal:ctl.signal,headers:{accept:"text/html,*/*","user-agent":"SoulCinema-Live-Probe/6.0"}});
    const body=await r.text();
    clearTimeout(tm);
    const offline=!r.ok||/stream not found|retrying in some seconds/i.test(body);
    return res.status(200).json({live:!offline,reliable:r.ok,source:"player-page"});
  }catch(e){
    clearTimeout(tm);
    return res.status(200).json({live:false,reliable:false,source:"player-page"});
  }
};