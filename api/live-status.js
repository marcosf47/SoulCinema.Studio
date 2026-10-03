const ORIGIN="https://live.soulcinema.studio";
const STREAM="soulcinemad-opus";
const candidates=[
  `${ORIGIN}/v3/paths/get/${STREAM}`,
  `${ORIGIN}/v3/paths/list`
];

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  const attempts=[];
  let sawAuthoritativeResponse=false;
  let live=false;

  for(const url of candidates){
    const ctl=new AbortController();
    const tm=setTimeout(()=>ctl.abort(),6500);
    try{
      const r=await fetch(url,{cache:"no-store",signal:ctl.signal,headers:{accept:"application/json","user-agent":"SoulCinema-Live-Status/2.0"}});
      const raw=await r.text();
      let data=null;
      try{data=JSON.parse(raw)}catch(e){}

      let item=null;
      if(Array.isArray(data?.items)) item=data.items.find(x=>x?.name===STREAM)||null;
      else if(data && typeof data==="object") item=data;

      const found=Boolean(item && (item.name===STREAM || !Array.isArray(data?.items)));
      const ready=Boolean(found && (item.ready===true || item.sourceReady===true || item.source?.ready===true));

      if(r.ok && data){
        sawAuthoritativeResponse=true;
        if(ready) live=true;
      }
      attempts.push({path:new URL(url).pathname,http:r.status,json:Boolean(data),found,ready});
    }catch(e){
      attempts.push({path:new URL(url).pathname,error:e?.name||"fetch-error"});
    }finally{clearTimeout(tm)}
  }

  // Only publish a definitive OFF state when MediaMTX answered successfully.
  // If status is unreachable, omit the boolean so the client preserves its current state.
  if(!sawAuthoritativeResponse){
    return res.status(200).json({diagnostic:true,stream:STREAM,attempts});
  }
  return res.status(200).json({live,stream:STREAM,attempts});
};