import { readFile } from 'node:fs/promises';
import path from 'node:path';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

const PROTECTED_BASE = 'https://soulcinema-music-discovery-dr3t2fv45-soul-cinema-studio.vercel.app';

export async function GET() {
  const filePath = path.join(process.cwd(), 'index (1).html');
  let html = await readFile(filePath, 'utf8');

  // RC170 live-preview delivery recovery only. The locked master HTML/state
  // machine remains untouched; only protected media references are mapped to
  // local public assets on this deployment.
  html = html
    .replaceAll(`${PROTECTED_BASE}/video/the-gate.mp4`, '/video/the-gate.mp4')
    .replaceAll(`${PROTECTED_BASE}/video/grand-lobby.mp4`, '/video/grand-lobby.mp4')
    .replaceAll(`${PROTECTED_BASE}/video/featured-premiere.mp4`, '/video/theater-premiere-opening.mp4')
    .replaceAll(`${PROTECTED_BASE}/featured-premiere.mp4`, '/video/theater-premiere-opening.mp4')
    .replaceAll(`${PROTECTED_BASE}/video/mwen-poukont-mwen-film.mp4`, '/video/mwen-poukont-mwen-film.mp4')
    .replaceAll(`../public/posters/mwen-poukont-mwen.png`, '/video/mwen-poukont-mwen.png');

  return new Response(html, {
    status: 200,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store',
    },
  });
}
