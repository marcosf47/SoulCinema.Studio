const ORIGIN="https://live.soulcinema.studio";
const STREAM="soulcinemad-opus";
const candidates=[
  `${ORIGIN}/v3/paths/get/${STREAM}`,
  `${ORIGIN}/v3/paths/list`
];

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  for(const url of candidates){
    try{
      const r=await fetch(url,{cache:"no-store",headers:{accept:"application/json","user-agent":"SoulCinema-Live-Probe/2.0"}});
      if(!r.ok)continue;
      const data=await r.json();
      let item=data;
      if(Array.isArray(data?.items)) item=data.items.find(x=>x?.name===STREAM);
      if(!item) continue;
      const live=Boolean(item.ready===true || item.sourceReady===true || item.source?.ready===true);
      return res.status(200).json({live,reliable:true});
    }catch(e){}
  }
  res.status(200).json({live:false,reliable:false});
};