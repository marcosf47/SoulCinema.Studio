'use client';
import Image from 'next/image';
import { useState } from 'react';
const films=[
 {img:'/images/film-1.png',title:'Haiti Toujours',tag:'A story that refuses to fade.',type:'Original'},
 {img:'/images/film-2.png',title:'The Art of Silence',tag:'What remains when the noise disappears?',type:'Short Film'},
 {img:'/images/film-3.png',title:'Mwen Poukont Mwen',tag:'Distance can still carry a heartbeat.',type:'Music Film'},
 {img:'/images/lobby.png',title:'The Arrival',tag:'The first door into the SoulCinema world.',type:'Studio Film'}
];
export default function FilmGallery(){
 const [filter,setFilter]=useState('All');
 const types=['All','Original','Short Film','Music Film','Studio Film'];
 const visible=filter==='All'?films:films.filter(f=>f.type===filter);
 return <>
  <div className="filter-row" aria-label="Filter films">{types.map(type=><button key={type} onClick={()=>setFilter(type)} className={filter===type?'active':''}>{type}</button>)}</div>
  <div className="poster-grid">{visible.map((f,i)=><article className="poster cinematic-card" key={f.title} style={{'--card-delay':`${i*70}ms`}}><div className="poster-image"><Image src={f.img} alt={f.title} fill sizes="(max-width:700px) 90vw, 30vw"/><div className="poster-play">▶</div><span className="poster-type">{f.type}</span></div><span>Film 0{i+1}</span><h3>{f.title}</h3><p>{f.tag}</p></article>)}</div>
 </>
}
