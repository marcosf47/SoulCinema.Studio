const SOURCE = 'https://live.soulcinema.studio/soulcinemad/index.m3u8';

export const dynamic = 'force-dynamic';
export const revalidate = 0;

export async function GET() {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 2500);

  try {
    const response = await fetch(SOURCE + '?status=' + Date.now(), {
      cache: 'no-store',
      signal: controller.signal,
      headers: { Accept: 'application/vnd.apple.mpegurl, application/x-mpegURL, text/plain' },
    });
    const manifest = await response.text();
    const live = response.ok &&
      manifest.includes('#EXTM3U') &&
      (manifest.includes('#EXT-X-STREAM-INF') ||
       manifest.includes('#EXTINF') ||
       manifest.includes('#EXT-X-TARGETDURATION'));

    return Response.json(
      { live, reliable: true },
      { headers: { 'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0', 'Access-Control-Allow-Origin': '*' } }
    );
  } catch {
    return Response.json(
      { live: false, reliable: false },
      { headers: { 'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0', 'Access-Control-Allow-Origin': '*' } }
    );
  } finally {
    clearTimeout(timeout);
  }
}
