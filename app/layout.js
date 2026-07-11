import './globals.css';
import Navigation from '../components/Navigation';
import Footer from '../components/Footer';
import StudioIntro from '../components/StudioIntro';
import ExperienceShell from '../components/ExperienceShell';
export const metadata={metadataBase:new URL('https://soulcinema.studio'),title:{default:'SoulCinema Studio',template:'%s | SoulCinema Studio'},description:'An independent cinematic storytelling studio where every heart hides a story.',openGraph:{title:'SoulCinema Studio',description:'Every heart hides a story.',url:'https://soulcinema.studio',siteName:'SoulCinema Studio',type:'website'}};
export default function RootLayout({children}){return <html lang="en"><body><StudioIntro/><ExperienceShell/><Navigation/><main>{children}</main><Footer/></body></html>}
