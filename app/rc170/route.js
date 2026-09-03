import { readFile } from 'node:fs/promises';
import path from 'node:path';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

const PROTECTED_BASE = 'https://soulcinema-music-discovery-dr3t2fv45-soul-cinema-studio.vercel.app';
const MASTER_BLOB_BASE = 'https://tfamln4qsost6j00.public.blob.vercel-storage.com';

const MASTER_MEDIA = {
  featured: `${MASTER_BLOB_BASE}/featured-premiere.mp4`,
  cloud: `${MASTER_BLOB_BASE}/THE%20LITTLE%20CLOUD%20WHO%20WAS%20AFRAID%20TO%20RAIN.mp4`,
  firefly: `${MASTER_BLOB_BASE}/THE%20LITTLE%20FIREFLY%20WHO%20LOST%20HIS%20LIGHT.mp4`,
  tiger: `${MASTER_BLOB_BASE}/THE%20LITTLE%20TIGER%20WHO%20COULDN%27T%20ROAR.mp4`,
  young: `${MASTER_BLOB_BASE}/YOUNG%20LEARNERS.mp4`,
};

export async function GET() {
  const filePath = path.join(process.cwd(), 'index (1).html');
  let html = await readFile(filePath, 'utf8');

  // Preview delivery layer only. Locked master HTML/state machine stays untouched.
  html = html
    .replaceAll(`${PROTECTED_BASE}/video/the-gate.mp4`, '/video/the-gate.mp4')
    .replaceAll(`${PROTECTED_BASE}/video/grand-lobby.mp4`, '/video/grand-lobby.mp4')
    .replaceAll(`${PROTECTED_BASE}/video/featured-premiere.mp4`, MASTER_MEDIA.featured)
    .replaceAll(`${PROTECTED_BASE}/featured-premiere.mp4`, MASTER_MEDIA.featured)
    .replaceAll('/video/theater-premiere-opening.mp4', MASTER_MEDIA.featured)
    .replaceAll('video/featured-premiere.mp4', MASTER_MEDIA.featured)
    .replaceAll('featured-premiere.mp4', MASTER_MEDIA.featured)
    .replaceAll('video/THE%20LITTLE%20CLOUD%20WHO%20WAS%20AFRAID%20TO%20RAIN.mp4', MASTER_MEDIA.cloud)
    .replaceAll('video/THE LITTLE CLOUD WHO WAS AFRAID TO RAIN.mp4', MASTER_MEDIA.cloud)
    .replaceAll('video/THE%20LITTLE%20FIREFLY%20WHO%20LOST%20HIS%20LIGHT.mp4', MASTER_MEDIA.firefly)
    .replaceAll('video/THE LITTLE FIREFLY WHO LOST HIS LIGHT.mp4', MASTER_MEDIA.firefly)
    .replaceAll('video/THE%20LITTLE%20TIGER%20WHO%20COULDN%27T%20ROAR.mp4', MASTER_MEDIA.tiger)
    .replaceAll("video/THE LITTLE TIGER WHO COULDN'T ROAR.mp4", MASTER_MEDIA.tiger)
    .replaceAll('video/YOUNG%20LEARNERS.mp4', MASTER_MEDIA.young)
    .replaceAll('video/YOUNG LEARNERS.mp4', MASTER_MEDIA.young)
    .replaceAll(`${PROTECTED_BASE}/video/mwen-poukont-mwen-film.mp4`, '/video/mwen-poukont-mwen-film.mp4')
    .replaceAll('../public/posters/mwen-poukont-mwen.png', '/video/mwen-poukont-mwen.png');

  return new Response(html, {
    status: 200,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store',
    },
  });
}
