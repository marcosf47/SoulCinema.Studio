export default function Home() {
  return (
    <main style={{ position: 'fixed', inset: 0, width: '100vw', height: '100dvh', margin: 0, padding: 0, overflow: 'hidden', background: '#000' }}>
      <iframe
        src="/rc170"
        title="SoulCinema RC170 Preview"
        style={{ width: '100%', height: '100%', border: 0, display: 'block', background: '#000' }}
        allow="autoplay; fullscreen"
      />
    </main>
  );
}
