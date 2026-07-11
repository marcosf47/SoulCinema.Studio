import Link from 'next/link';
import RoomCard from '../components/RoomCard';
import Reveal from '../components/Reveal';
import SectionMarquee from '../components/SectionMarquee';

export default function Home(){
 return <>
  <section className="private-ribbon">PRIVATE STUDIO PREVIEW · NOT PUBLICLY ANNOUNCED</section>
  <section className="hero">
   <video className="hero-video" autoPlay muted loop playsInline poster="/images/studio-exterior.png"><source src="/video/hero.mp4" type="video/mp4"/></video>
   <div className="hero-overlay"/><div className="hero-grid-lines"/>
   <div className="hero-content">
    <span className="eyebrow">SoulCinema Studio · Private Build</span>
    <div className="portal-mark"><span>SC</span></div>
    <h1>Every Heart<br/><em>Hides a Story.</em></h1>
    <p>Original films, music, stories, and live experiences created with emotional honesty and cinematic craft.</p>
    <div className="hero-actions"><a className="button gold" href="#lobby">Enter the studio</a><Link className="button ghost" href="/music">Meet Original #001</Link></div>
   </div>
   <a className="scroll-cue" href="#lobby">Scroll to enter <span>↓</span></a>
  </section>
  <SectionMarquee/>
  <section id="lobby" className="section lobby-section"><div className="ambient-orb orb-one"/><div className="ambient-orb orb-two"/><div className="shell">
   <Reveal><div className="section-heading"><span className="eyebrow">The Grand Lobby</span><h2>Choose the story you want to experience.</h2><p>Six focused pillars. One SoulCinema identity.</p></div></Reveal>
   <div className="room-grid">
    <Reveal delay={0}><RoomCard href="/films" eyebrow="01" title="Originals" text="Music films, short films, documentaries, and cinematic stories." image="/images/film-1.png"/></Reveal>
    <Reveal delay={100}><RoomCard href="/music" eyebrow="02" title="Music" text="Songs and soundtracks where every note carries a story." image="/images/mwen-poukont-mwen-cover.jpg"/></Reveal>
    <Reveal delay={200}><RoomCard href="/journal" eyebrow="03" title="Stories" text="The ideas, memories, and production notes behind the work." image="/images/journal-1.png"/></Reveal>
    <Reveal delay={300}><RoomCard href="/live" eyebrow="04" title="Live" text="Real-time conversations and premieres produced through vMix." accent="red" image="/images/studio-lobby-wide.png"/></Reveal>
   </div>
  </div></section>
  <section className="section featured-band"><div className="shell split">
   <Reveal><div><span className="eyebrow">Launch centerpiece</span><h2>SoulCinema Original #001</h2><p className="section-copy"><strong>MWEN POUKONT MWEN</strong> — a bilingual English and Kreyòl story about distance, connection, and two hearts that never meet.</p><div className="studio-stats"><div><strong>01</strong><span>First original</span></div><div><strong>02</strong><span>Languages</span></div><div><strong>01</strong><span>Studio identity</span></div></div></div></Reveal>
   <Reveal delay={120}><div className="today-list"><Link href="/music"><b>Listen</b><span>Mwen Poukont Mwen</span></Link><Link href="/films"><b>Watch</b><span>Music Film — in production</span></Link><Link href="/live"><b>Premiere</b><span>SoulCinema Live</span></Link><Link href="/review"><b>Private review</b><span>Compare video candidates</span></Link></div></Reveal>
  </div></section>
 </>
}
