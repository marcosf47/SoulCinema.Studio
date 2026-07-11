'use client';
import { useEffect, useState } from 'react';
export default function StudioIntro(){
 const [show,setShow]=useState(false);
 useEffect(()=>{if(!sessionStorage.getItem('sc-intro')){setShow(true);const t=setTimeout(()=>{setShow(false);sessionStorage.setItem('sc-intro','1')},2400);return()=>clearTimeout(t)}},[]);
 if(!show)return null;
 return <div className="studio-intro" aria-hidden="true"><div className="intro-ring"><span>SC</span></div><p>Every heart hides a story.</p></div>
}
