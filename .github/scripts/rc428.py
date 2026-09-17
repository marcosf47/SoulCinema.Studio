from pathlib import Path
p=Path('public/index.html')
h=p.read_text(encoding='utf-8')
marker='<!-- RC428 EXACT RC400 LIVE FULLSCREEN RESTORE -->'
if marker in h: raise SystemExit('already patched')

def remove_block(start_marker,end_marker):
 global h
 s=h.find(start_marker)
 if s!=-1:
  e=h.find(end_marker,s)
  if e==-1: raise SystemExit('end marker missing: '+end_marker)
  h=h[:s]+h[e+len(end_marker):]

# Remove the two later Live fullscreen authorities. RC400 remains untouched.
remove_block('<!-- RC426 RESTORE LOCKED MOBILE LIVE FULLSCREEN -->','</script>')
remove_block('<!-- RC427 NATIVE LIVE FULLSCREEN ON ENTRY -->','</script>')
if 'rc426-restore-mobile-live-fullscreen' in h or 'rc427-native-live-fullscreen-on-entry' in h:
 raise SystemExit('later live fullscreen authority still present')
if 'rc400-master-mobile-live-fullscreen-authority' not in h:
 raise SystemExit('RC400 authority missing')
if 'RC418 THEATER FULLSCREEN EXIT ISOLATION' not in h:
 raise SystemExit('RC418 isolation missing')
h=h.replace('</body>',marker+'\n</body>',1)
p.write_text(h,encoding='utf-8')
