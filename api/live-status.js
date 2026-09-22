const ORIGIN="https://live.soulcinema.studio";
const STREAM="soulcinemad-opus";
const HLS=`${ORIGIN}/${STREAM}/index.m3u8`;

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  try{
    const r=await fetch(HLS,{cache:"no-store",redirect:"follow",headers:{accept:"application/vnd.apple.mpegurl,application/x-mpegURL,*/*","user-agent":"SoulCinema-Live-Probe/5.0"}});
    const body=await r.text();
    const playlist=r.ok&&/#EXTM3U/i.test(body);
    return res.status(200).json({live:playlist,reliable:true,source:"hls-playlist"});
  }catch(e){
    return res.status(200).json({live:false,reliable:false});
  }
};
