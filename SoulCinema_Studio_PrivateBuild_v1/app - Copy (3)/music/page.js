import Image from 'next/image';
import AudioPlayer from '../../components/AudioPlayer';
import PageHero from '../../components/PageHero';
import Reveal from '../../components/Reveal';
export const metadata={title:'Music'};
export default function Music(){return <>
 <PageHero eyebrow="SoulCinema Music" title="Music that becomes cinema." text="Original songs, cinematic soundtracks, and bilingual stories built to live beyond the final note."/>
 <section className="section"><div className="shell music-layout">
  <Reveal><div className="album-art"><Image src="/images/mwen-poukont-mwen-cover.jpg" alt="Mwen Poukont Mwen official SoulCinema artwork" fill priority sizes="(max-width:900px) 100vw, 45vw"/><div className="vinyl-ring"/><div className="equalizer" aria-hidden="true">{Array.from({length:18}).map((_,i)=><i key={i} style={{'--h':`${25+(i%6)*10}%`}}/>)}</div></div></Reveal>
  <Reveal delay={120}><div className="music-copy"><span className="eyebrow">SoulCinema Original #001</span><h2>MWEN POUKONT MWEN</h2><p>A story told in English and Kreyòl. Two people live apart, connected by calls and messages, carrying a love that never becomes a physical meeting.</p><AudioPlayer src="/audio/mwen-poukont-mwen.mp3" title="Mwen Poukont Mwen" subtitle="SoulCinema Original #001"/><div className="track-meta"><span>Format — Cinematic music story</span><span>Language — English / Kreyòl</span><span>Produced by — SoulCinema Studio</span><span>Status — Private launch preparation</span></div></div></Reveal>
 </div></section>
 <section className="section session-band"><div className="shell split"><Reveal><div><span className="eyebrow">The launch story</span><h2>The website and the first original will premiere together.</h2></div></Reveal><Reveal delay={120}><p className="large-quote">“We are not releasing a song. We are opening the studio with its first story.”</p></Reveal></div></section>
 </>}
