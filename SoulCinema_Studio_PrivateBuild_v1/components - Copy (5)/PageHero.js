import Reveal from './Reveal';
export default function PageHero({eyebrow,title,text,children}){return <section className="page-hero"><div className="page-hero-glow"/><div className="hero-grid-lines"/><div className="shell"><Reveal><span className="eyebrow">{eyebrow}</span><h1>{title}</h1><p>{text}</p>{children}</Reveal></div></section>}
