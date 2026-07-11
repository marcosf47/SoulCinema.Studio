'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { usePathname } from 'next/navigation';
const links=[['/','Home'],['/films','Originals'],['/music','Music'],['/journal','Stories'],['/live','Live'],['/about','Studio'],['/contact','Contact']];
export default function Navigation(){
 const [open,setOpen]=useState(false),[solid,setSolid]=useState(false); const path=usePathname();
 useEffect(()=>{const onScroll=()=>setSolid(window.scrollY>24);onScroll();window.addEventListener('scroll',onScroll);return()=>window.removeEventListener('scroll',onScroll)},[]);
 useEffect(()=>setOpen(false),[path]);
 return <header className={`nav ${solid?'nav-solid':''}`}><Link className="brand" href="/"><span className="brand-mark">SC</span><span>SOULCINEMA</span></Link><button className={`menu-button ${open?'active':''}`} aria-label="Toggle navigation" aria-expanded={open} onClick={()=>setOpen(!open)}><span/><span/><span/></button><nav className={open?'nav-links open':'nav-links'} aria-label="Primary navigation">{links.map(([href,label])=><Link key={href} href={href} className={`${label==='Live'?'live-link ':''}${path===href?'active':''}`}>{label==='Live'&&<i/>}{label}</Link>)}</nav></header>
}
