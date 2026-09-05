import { mkdir, writeFile } from 'node:fs/promises';

const ORIGIN = 'https://soulcinema-master.vercel.app';
const res = await fetch(`${ORIGIN}/?qa_snapshot=${Date.now()}`, {
  headers: { 'user-agent': 'SoulCinema-Final-QA-Builder/1.0', 'cache-control': 'no-cache' }
});
if (!res.ok) throw new Error(`MASTER snapshot fetch failed: ${res.status} ${res.statusText}`);
let html = await res.text();
if (!html.includes('SOULCINEMA') || html.includes('404: NOT_FOUND')) {
  throw new Error('MASTER snapshot validation failed');
}

// Preview-only media bridge. The QA snapshot stays byte-for-byte in structure/logic;
// only relative asset references are made absolute so the Git preview does not depend
// on the incomplete historical Git media tree.
const reps = [
  ['data-kids-src="video/', `data-kids-src="${ORIGIN}/video/`],
  ["data-kids-src='video/", `data-kids-src='${ORIGIN}/video/`],
  ['src="video/', `src="${ORIGIN}/video/`],
  ["src='video/", `src='${ORIGIN}/video/`],
  ['src="audio/', `src="${ORIGIN}/audio/`],
  ["src='audio/", `src='${ORIGIN}/audio/`],
  ['src="posters/', `src="${ORIGIN}/posters/`],
  ["src='posters/", `src='${ORIGIN}/posters/`],
  ["url('../public/", `url('${ORIGIN}/public/`],
  ['url("../public/', `url("${ORIGIN}/public/`],
  ['="../public/', `="${ORIGIN}/public/`],
  ["='../public/", `='${ORIGIN}/public/`]
];
for (const [from, to] of reps) html = html.split(from).join(to);

html = html.replace('</head>', `<meta name="soulcinema-qa-source" content="master-snapshot">\n</head>`);
await mkdir('public', { recursive: true });
await writeFile('public/index.html', html, 'utf8');
console.log(`SoulCinema QA snapshot prepared: ${Buffer.byteLength(html)} bytes`);
