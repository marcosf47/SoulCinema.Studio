const ORIGIN="https://live.soulcinema.studio";
const STREAM="soulcinemad-opus";
const candidates=[
  `${ORIGIN}/v3/paths/get/${STREAM}`,
  `${ORIGIN}/v3/paths/list`
];

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");
  const attempts=[];
  for(const url of candidates){
    const ctl=new AbortController();
    const tm=setTimeout(()=>ctl.abort(),6500);
    try{
      const r=await fetch(url,{cache:"no-store",signal:ctl.signal,headers:{accept:"application/json","user-agent":"SoulCinema-Live-Diagnostic/1.0"}});
      const raw=await r.text();
      let data=null;
      try{data=JSON.parse(raw)}catch(e){}
      let item=data;
      if(Array.isArray(data?.items))item=data.items.find(x=>x?.name===STREAM)||null;
      const ready=Boolean(item&&(item.ready===true||item.sourceReady===true||item.source?.ready===true));
      attempts.push({path:new URL(url).pathname,http:r.status,json:Boolean(data),found:Boolean(item),ready});
    }catch(e){
      attempts.push({path:new URL(url).pathname,error:e?.name||"fetch-error"});
    }finally{clearTimeout(tm)}
  }
  return res.status(200).json({diagnostic:true,stream:STREAM,attempts});
};