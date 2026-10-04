const PLAYER="https://live.soulcinema.studio/soulcinemad-opus/?controls=false&muted=true&autoplay=false&playsInline=true";
const MTX="https://live.soulcinema.studio";
const PATH="soulcinemad-opus";

async function fetchJson(url,timeout=3200){
  const ctl=new AbortController(),tm=setTimeout(()=>ctl.abort(),timeout);
  try{
    const r=await fetch(url+(url.includes("?")?"&":"?")+"_sc="+Date.now(),{cache:"no-store",redirect:"follow",signal:ctl.signal,headers:{accept:"application/json,*/*","user-agent":"SoulCinema-Live-Probe/8.0"}});
    if(!r.ok)return null;
    return await r.json();
  }finally{clearTimeout(tm)}
}

async function fetchText(url,timeout=4200){
  const ctl=new AbortController(),tm=setTimeout(()=>ctl.abort(),timeout);
  try{
    const r=await fetch(url+(url.includes("?")?"&":"?")+"_sc="+Date.now(),{cache:"no-store",redirect:"follow",signal:ctl.signal,headers:{accept:"text/html,*/*","user-agent":"SoulCinema-Live-Probe/8.0"}});
    return {ok:r.ok,body:await r.text()};
  }finally{clearTimeout(tm)}
}

function pathState(d){
  if(!d||typeof d!=="object")return null;
  if(d.ready===true||d.sourceReady===true||d.source?.ready===true)return true;
  if(d.ready===false||d.sourceReady===false||d.source?.ready===false)return false;
  return null;
}

module.exports=async function handler(req,res){
  res.setHeader("Cache-Control","no-store, max-age=0");

  // First recover the authoritative OFF/ON signal from MediaMTX when available.
  let mtxState=null;
  try{
    const d=await fetchJson(MTX+"/v3/paths/get/"+encodeURIComponent(PATH));
    mtxState=pathState(d);
  }catch(e){}
  if(mtxState===null){
    try{
      const d=await fetchJson(MTX+"/v3/paths/list");
      const items=Array.isArray(d?.items)?d.items:[];
      const p=items.find(x=>x?.name===PATH);
      if(p)mtxState=pathState(p);
      else if(Array.isArray(d?.items))mtxState=false;
    }catch(e){}
  }

  // Proven ON path: when the publisher is present, mount the existing player.
  if(mtxState===true)return res.status(200).json({live:true,reliable:true,source:"mediamtx-ready"});

  // Keep the player-page probe as the ON compatibility fallback that previously
  // brought SoulCinema Live on air. An explicit MediaMTX OFF always wins below.
  let playerOnline=false,playerExplicitOff=false;
  try{
    const p=await fetchText(PLAYER);
    playerExplicitOff=!p.ok||/stream not found|retrying in some seconds/i.test(p.body);
    playerOnline=p.ok&&!playerExplicitOff;
  }catch(e){}

  // Authoritative OFF gate: this prevents the raw stream-not-found iframe.
  if(mtxState===false||playerExplicitOff)return res.status(200).json({live:false,reliable:true,source:mtxState===false?"mediamtx-off":"player-off"});

  if(playerOnline)return res.status(200).json({live:true,reliable:false,source:"player-page"});

  // Unknown/transient probe state is not declared reliable OFF, so the mobile
  // watcher will preserve an already-mounted live session and retry automatically.
  return res.status(200).json({live:false,reliable:false,source:"unknown"});
};
