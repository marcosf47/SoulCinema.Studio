'use client';
import { useEffect, useState } from 'react';
export default function CinemaPlayer({video='/video/hero.mp4',label='Watch the story'}){
 const [open,setOpen]=useState(false);
 useEffect(()=>{const esc=e=>e.key==='Escape'&&setOpen(false);window.addEventListener('keydown',esc);return()=>window.removeEventListener('keydown',esc)},[]);
 return <><button className="button gold" onClick={()=>setOpen(true)}>{label}</button>{open&&<div className="cinema-modal" role="dialog" aria-modal="true" aria-label="SoulCinema player"><button className="cinema-close" onClick={()=>setOpen(false)} aria-label="Close player">×</button><video controls autoPlay playsInline src={video}/><div className="cinema-caption"><span>SoulCinema Original</span><b>Every story deserves the screen.</b></div></div>}</>
}
