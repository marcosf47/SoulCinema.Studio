import { readFile } from 'node:fs/promises';
import path from 'node:path';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

const PROTECTED_BASE = 'https://soulcinema-music-discovery-dr3t2fv45-soul-cinema-studio.vercel.app';

export async function GET() {
  const filePath = path.join(process.cwd(), 'index (1).html');
  let html = await readFile(filePath, 'utf8');

  // Surgical live-preview recovery only: preserve the RC170 HTML and
  // redirect the two locked cinematic assets to this deployment's public media.
  html = html
    .replace(`${PROTECTED_BASE}/video/the-gate.mp4`, '/video/the-gate.mp4')
    .replace(`${PROTECTED_BASE}/video/grand-lobby.mp4`, '/video/grand-lobby.mp4');

  return new Response(html, {
    status: 200,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store',
    },
  });
}
