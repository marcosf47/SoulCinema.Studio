from pathlib import Path
import re
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
# Remove failed additive RC412B router.
h=re.sub(r'<!-- RC412B DIRECT MOBILE PORTAL ROUTER -->.*?</script>\s*','',h,flags=re.S)
# Remove duplicate per-card click ownership.
old='      bind(n,()=>openRoom(room,n));'
if old not in h: raise SystemExit('portal bind not found')
h=h.replace(old,'      // RC413C: portal cards are owned only by the exact-target capture router.',1)
# Replace ambiguous hit testing with exact event target routing.
start=h.find('  const findAction=(e)=>{')
end=h.find('  const rememberTap=(e)=>{',start)
if start<0 or end<0: raise SystemExit('findAction block not found')
new="""  const findAction=(e)=>{
    if(!mobile())return;
    const portalSelector='#portals .portal[data-room],#portals .portal[data-mobile-room],#portals .studio-utility-btn[data-room]';
    const hit=e.target?.closest?.(portalSelector+',button,[role=button]');
    if(!hit)return;
    const id=hit.id||'';
    const room=hit.dataset?.mobileRoom||hit.dataset?.room;
    const returns=new Set(['theaterReturn','musicReturn','returnLobby','productionReturn','storyReturn','journalReturn','bibleReturn','aboutReturn','contactReturn']);
    let action=null;
    if(id==='enter'||id==='preview')action=goEnter;
    else if(id==='back')action=goGate;
    else if(id==='skip')action=goPortals;
    else if(returns.has(id))action=goPortals;
    else if(room&&hit.closest?.('#portals'))action=()=>openRoom(room,hit);
    if(!action)return;
    return {action,hit};
  };
"""
h=h[:start]+new+h[end:]
needle="""    if((e.type==='pointerup'||e.type==='touchend')&&tapStart){
      const p=eventPoint(e);
      const dx=Math.abs(p.x-tapStart.x);
      const dy=Math.abs(p.y-tapStart.y);
      if(dx>32||dy>32)return;
    }"""
repl="""    if((e.type==='pointerup'||e.type==='touchend')&&tapStart){
      const p=eventPoint(e);
      const dx=Math.abs(p.x-tapStart.x);
      const dy=Math.abs(p.y-tapStart.y);
      if(dx>32||dy>32||tapStart.hit!==routed.hit){tapStart=null;return;}
    }"""
if needle not in h: raise SystemExit('gesture block not found')
h=h.replace(needle,repl,1)
# Remove recursive delayed room opening.
old_open="""    if(document.body.dataset.experience==='portal_mode'&&document.body.dataset.rc375RoomOpening!=='1'){
      document.body.dataset.rc375RoomOpening='1';
      source?.classList?.add('rc375-portal-pressed');
      setTimeout(()=>{
        source?.classList?.remove('rc375-portal-pressed');
        delete document.body.dataset.rc375RoomOpening;
        openRoom(room);
      },145);
      return;
    }"""
new_open="""    if(document.body.dataset.experience==='portal_mode'){
      source?.classList?.add('rc375-portal-pressed');
      requestAnimationFrame(()=>source?.classList?.remove('rc375-portal-pressed'));
    }"""
if old_open not in h: raise SystemExit('delayed openRoom block not found')
h=h.replace(old_open,new_open,1)
anchor='<!-- RC375 MOBILE PORTAL SCROLL + ROOM HANDOFF SMOOTHNESS -->'
if anchor not in h: raise SystemExit('RC375 anchor not found')
h=h.replace(anchor,'<!-- RC413C MOBILE PORTALS SINGLE NAVIGATION AUTHORITY -->\n'+anchor,1)
p.write_text(h,encoding='utf-8')
