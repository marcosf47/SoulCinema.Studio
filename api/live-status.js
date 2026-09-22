const ORIGIN="https://live.soulcinema.studio";
const STREAM="soulcinemad-opus";
const FEED=`${ORIGIN}/${STREAM}/?controls=false&muted=true&autoplay=false&playsInline=true`;

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  try{
    const r=await fetch(FEED,{cache:"no-store",redirect:"follow",headers:{accept:"text/html","user-agent":"SoulCinema-Live-Probe/4.0"}});
    const body=await r.text();
    if(!r.ok) return res.status(200).json({live:false,reliable:false});
    const offline=/stream not found|retrying in some seconds/i.test(body);
    return res.status(200).json({live:!offline,reliable:true,source:"player-state"});
  }catch(e){
    return res.status(200).json({live:false,reliable:false});
  }
};