const PLAYER="https://live.soulcinema.studio/soulcinemad-opus/?controls=false&muted=true&autoplay=false&playsInline=true";
const HLS_CANDIDATES=[
  "https://live.soulcinema.studio/soulcinemad-opus/index.m3u8",
  "https://live.soulcinema.studio/soulcinemad-opus.m3u8"
];

async function fetchText(url,timeout=3500){
  const ctl=new AbortController();
  const tm=setTimeout(()=>ctl.abort(),timeout);
  try{
    const r=await fetch(url+(url.includes("?")?"&":"?")+"_sc="+Date.now(),{
      cache:"no-store",redirect:"follow",signal:ctl.signal,
      headers:{accept:"application/vnd.apple.mpegurl,application/x-mpegURL,text/plain,text/html,*/*","user-agent":"SoulCinema-Live-Probe/7.0"}
    });
    const body=await r.text();
    return {ok:r.ok,status:r.status,body};
  }finally{clearTimeout(tm)}
}

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");

  // Prefer real media evidence. A MediaMTX player page can remain HTTP 200
  // after the publisher disappears, so it must never be authoritative OFF/ON by itself.
  for(const url of HLS_CANDIDATES){
    try{
      const p=await fetchText(url);
      const hasMedia=p.ok&&p.body.includes("#EXTM3U")&&(
        p.body.includes("#EXT-X-STREAM-INF")||
        p.body.includes("#EXTINF")||
        p.body.includes("#EXT-X-TARGETDURATION")
      );
      if(hasMedia)return res.status(200).json({live:true,reliable:true,source:"hls-manifest"});
    }catch(e){}
  }

  // Keep the proven player-page ON path as a compatibility fallback, but only
  // accept it when the response itself does not contain MediaMTX's offline state.
  try{
    const p=await fetchText(PLAYER,4500);
    const explicitOffline=!p.ok||/stream not found|retrying in some seconds/i.test(p.body);
    if(explicitOffline)return res.status(200).json({live:false,reliable:true,source:"player-page-offline"});
  }catch(e){
    return res.status(200).json({live:false,reliable:false,source:"probe-error"});
  }

  // No playable HLS media was found. Do not mount an iframe that can expose the
  // raw "stream not found" page; the next poll will restore ON automatically.
  return res.status(200).json({live:false,reliable:true,source:"no-media"});
};
