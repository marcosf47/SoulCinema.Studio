from pathlib import Path

java = Path('android/app/src/main/java/studio/soulcinema/app/MainActivity.java')
s = java.read_text()
assert 'public class MainActivity extends BridgeActivity {}' in s
s = s.replace('import com.getcapacitor.BridgeActivity;', 'import com.getcapacitor.BridgeActivity;\nimport android.os.Bundle;\nimport android.view.View;')
s = s.replace('public class MainActivity extends BridgeActivity {}', '''public class MainActivity extends BridgeActivity {
  private static final int IMMERSIVE_FLAGS = View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY | View.SYSTEM_UI_FLAG_FULLSCREEN | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_LAYOUT_STABLE;
  private boolean liveImmersive = false;
  private void applyLiveImmersive(boolean enabled) {
    liveImmersive = enabled;
    runOnUiThread(() -> getWindow().getDecorView().setSystemUiVisibility(enabled ? IMMERSIVE_FLAGS : View.SYSTEM_UI_FLAG_VISIBLE));
  }
  @Override public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    getBridge().getWebView().addJavascriptInterface(new Object() {
      @android.webkit.JavascriptInterface public void setImmersive(String enabled) { MainActivity.this.applyLiveImmersive("1".equals(enabled)); }
    }, "SoulImmersive");
  }
  @Override public void onWindowFocusChanged(boolean hasFocus) {
    super.onWindowFocusChanged(hasFocus);
    if (hasFocus && liveImmersive) applyLiveImmersive(true);
  }
}''')
java.write_text(s)

html = Path('android/app/src/main/assets/public/index.html')
h = html.read_text()
needle = 'function go(id){'
assert needle in h
h = h.replace(needle, needle + 'try{if(window.SoulImmersive)window.SoulImmersive.setImmersive(id==="live"?"1":"0")}catch(e){}', 1)
html.write_text(h)
assert 'SoulImmersive.setImmersive' in h
assert 'SOULCINEMA LIVE SCREEN AWAKE LOCK' in h
