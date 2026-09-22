const ORIGIN="https://live.soulcinema.studio";
const STREAM="soulcinemad-opus";
const probes=[
  {url:`${ORIGIN}/${STREAM}/index.m3u8`,kind:"hls"},
  {url:`${ORIGIN}/v3/paths/get/${STREAM}`,kind:"api"}
];

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  for(const p of probes){
    try{
      const r=await fetch(p.url,{cache:"no-store",headers:{accept:p.kind==="hls"?"application/vnd.apple.mpegurl":"application/json","user-agent":"SoulCinema-Live-Probe/3.0"}});
      if(p.kind==="hls"){
        if(r.ok){
          const body=await r.text();
          if(/#EXTM3U/i.test(body)) return res.status(200).json({live:true,reliable:true,source:"hls"});
        }
        if(r.status===404) return res.status(200).json({live:false,reliable:true,source:"hls"});
      }else if(r.ok){
        const item=await r.json();
        const live=Boolean(item?.ready===true||item?.sourceReady===true||item?.source?.ready===true);
        return res.status(200).json({live,reliable:true,source:"api"});
      }
    }catch(e){}
  }
  res.status(200).json({live:false,reliable:false});
};