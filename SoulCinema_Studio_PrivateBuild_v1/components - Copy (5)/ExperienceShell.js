'use client';
import { useEffect } from 'react';
export default function ExperienceShell(){
 useEffect(()=>{const move=e=>{document.documentElement.style.setProperty('--mx',`${e.clientX}px`);document.documentElement.style.setProperty('--my',`${e.clientY}px`)};window.addEventListener('pointermove',move);return()=>window.removeEventListener('pointermove',move)},[]);
 return <div className="cursor-glow" aria-hidden="true"/>
}
