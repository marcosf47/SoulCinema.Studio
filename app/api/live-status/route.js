const SOURCES = [
  'https://live.soulcinema.studio/soulcinemad/index.m3u8',
  'http://162.35.122.62:8888/soulcinemad/index.m3u8',
];

export const dynamic = 'force-dynamic';
export const revalidate = 0;

const headers = {
  Accept: 'application/vnd.apple.mpegurl, application/x-mpegURL, text/plain',
  'User-Agent': 'Mozilla/5.0 SoulCinema-Live-Monitor/1.0',
  Referer: 'https://www.soulcinema.studio/',
};

export async function GET() {
  let confirmedOffline = false;

  for (const source of SOURCES) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 6500);

    try {
      const response = await fetch(source + '?status=' + Date.now(), {
        cache: 'no-store',
        signal: controller.signal,
        headers,
      });
      const manifest = await response.text();
      const live = response.ok &&
        manifest.includes('#EXTM3U') &&
        (manifest.includes('#EXT-X-STREAM-INF') ||
         manifest.includes('#EXTINF') ||
         manifest.includes('#EXT-X-TARGETDURATION'));

      if (live) {
        return Response.json(
          { live: true, reliable: true },
          { headers: { 'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0', 'Access-Control-Allow-Origin': '*' } }
        );
      }

      if (response.status === 404) confirmedOffline = true;
    } catch {
      // An unreachable or blocked probe is unknown, never a confirmed OFF AIR signal.
    } finally {
      clearTimeout(timeout);
    }
  }

  return Response.json(
    { live: false, reliable: confirmedOffline },
    { headers: { 'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0', 'Access-Control-Allow-Origin': '*' } }
  );
}
