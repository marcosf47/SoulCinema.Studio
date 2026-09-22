const LIVE_URL="https://live.soulcinema.studio/soulcinemad-opus/?controls=true&muted=true&autoplay=false&playsInline=true";

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  try{
    const r=await fetch(LIVE_URL,{cache:"no-store",headers:{"user-agent":"SoulCinema-Live-Probe/1.0"}});
    const body=await r.text();
    const off=!r.ok||/stream not found|retrying in some seconds|not found/i.test(body);
    res.status(200).json({live:!off});
  }catch(e){
    res.status(200).json({live:false});
  }
};