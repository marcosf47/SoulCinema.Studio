(()=>{
  const player=document.getElementById('theaterPlayer');
  const folder=document.getElementById('kidsAnimationFolder');
  const autoBtn=document.getElementById('kidsAutoPlay');
  const room307=document.querySelector('.collection-card.room307-card');
  if(!player)return;

  /* Kids Auto Play: keep the proven ENDED-based handoff. No early cut.
     Prime only the NEXT title aggressively enough to have decoded media ready. */
  if(folder&&autoBtn){
    const cards=[...folder.querySelectorAll('[data-kids-src]')];
    const primers=new Map();

    const getIndex=()=>{
      const title=(document.getElementById('theaterCurrentTitle')?.textContent||'').trim();
      return cards.findIndex(c=>(c.dataset.kidsTitle||'').trim()===title);
    };

    const prime=(src)=>{
      if(!src)return;
      let v=primers.get(src);
      if(!v){
        v=document.createElement('video');
        v.preload='auto';v.muted=true;v.playsInline=true;
        v.setAttribute('playsinline','');v.setAttribute('aria-hidden','true');
        v.style.cssText='position:fixed;width:2px;height:2px;left:-9999px;top:-9999px;opacity:0;pointer-events:none';
        document.body.appendChild(v);primers.set(src,v);v.src=src;
        try{v.load()}catch(e){}
      }
      const kick=()=>{
        if(v.dataset.scPrimed==='1')return;
        v.dataset.scPrimed='1';
        try{
          const p=v.play();
          if(p&&p.then)p.then(()=>setTimeout(()=>{try{v.pause();v.currentTime=0}catch(e){}},320)).catch(()=>{});
        }catch(e){}
      };
      if(v.readyState>=2)kick();
      else v.addEventListener('loadeddata',kick,{once:true});
    };

    const primeNext=()=>{
      if(autoBtn.getAttribute('aria-pressed')!=='true')return;
      const i=getIndex();
      if(i>=0&&cards[i+1])prime(cards[i+1].dataset.kidsSrc);
    };

    autoBtn.addEventListener('click',()=>setTimeout(primeNext,0),true);
    cards.forEach((card,i)=>{
      card.addEventListener('click',()=>{
        if(autoBtn.getAttribute('aria-pressed')==='true'&&cards[i+1])prime(cards[i+1].dataset.kidsSrc);
      },true);
    });
    player.addEventListener('playing',primeNext,true);
    player.addEventListener('timeupdate',()=>{
      if(player.duration&&isFinite(player.duration)&&player.currentTime>1)primeNext();
    },{passive:true});
  }

  /* Room 307 only: prewarm its Blob and clear inherited premiere transforms
     before the existing collection handler runs. No global Theater CSS changes. */
  if(room307){
    const src=room307.dataset.contentSrc;
    let warmer=null;
    const warm=()=>{
      if(warmer||!src)return;
      warmer=document.createElement('video');
      warmer.preload='auto';warmer.muted=true;warmer.playsInline=true;
      warmer.setAttribute('playsinline','');warmer.setAttribute('aria-hidden','true');
      warmer.style.cssText='position:fixed;width:2px;height:2px;left:-9999px;top:-9999px;opacity:0;pointer-events:none';
      document.body.appendChild(warmer);warmer.src=src;
      try{warmer.load()}catch(e){}
    };
    warm();
    room307.addEventListener('pointerenter',warm,{passive:true});
    room307.addEventListener('focusin',warm);
    room307.addEventListener('click',()=>{
      warm();
      player.classList.remove('theater-handoff','theater-portal-push','theater-feature-enter');
    },true);
  }
})();
