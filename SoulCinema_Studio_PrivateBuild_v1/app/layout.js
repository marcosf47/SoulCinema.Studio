import './globals.css';
import Navigation from '../components/Navigation';
import Footer from '../components/Footer';
import StudioIntro from '../components/StudioIntro';
import ExperienceShell from '../components/ExperienceShell';
import PageTransition from '../components/PageTransition';
export const viewport={themeColor:'#030303'};
export const metadata={metadataBase:new URL('https://soulcinema.studio'),title:{default:'SoulCinema Studio',template:'%s | SoulCinema Studio'},description:'Private preview of SoulCinema Studio — originals, music, stories, live experiences, and the studio behind them.',applicationName:'SoulCinema Studio',openGraph:{title:'SoulCinema Studio',description:'Every heart hides a story.',url:'https://soulcinema.studio',siteName:'SoulCinema Studio',type:'website',images:['/images/studio-exterior.png']},twitter:{card:'summary_large_image',title:'SoulCinema Studio',description:'Every heart hides a story.',images:['/images/studio-exterior.png']}};
export default function RootLayout({children}){return <html lang="en"><body><StudioIntro/><ExperienceShell/><Navigation/><main><PageTransition>{children}</PageTransition></main><Footer/></body></html>}
