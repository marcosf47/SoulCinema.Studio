import './globals.css';
export const metadata={metadataBase:new URL('https://soulcinema.studio'),title:{default:'SoulCinema Studio',template:'%s | SoulCinema Studio'},description:'An independent cinematic storytelling studio where every heart hides a story.',openGraph:{title:'SoulCinema Studio',description:'Every heart hides a story.',url:'https://soulcinema.studio',siteName:'SoulCinema Studio',type:'website'}};
export default function RootLayout({children}){return <html lang="en"><body style={{margin:0,background:'#000',overflow:'hidden'}}>{children}</body></html>}
