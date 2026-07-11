'use client';
import { useRef, useState } from 'react';
export default function AudioPlayer({src,title,subtitle}){
 const ref=useRef(null); const [playing,setPlaying]=useState(false); const [progress,setProgress]=useState(0);
 const toggle=()=>{const a=ref.current;if(!a)return;if(a.paused){a.play();setPlaying(true)}else{a.pause();setPlaying(false)}};
 return <div className="audio-card"><audio ref={ref} src={src} onTimeUpdate={e=>setProgress((e.currentTarget.currentTime/e.currentTarget.duration||0)*100)} onEnded={()=>setPlaying(false)}/><button onClick={toggle} aria-label={playing?'Pause':'Play'}>{playing?'Ⅱ':'▶'}</button><div><strong>{title}</strong><small>{subtitle}</small><div className="audio-track"><i style={{width:`${progress}%`}}/></div></div></div>
}
