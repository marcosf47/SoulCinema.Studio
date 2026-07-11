'use client';
import { useEffect, useRef, useState } from 'react';
export default function Reveal({children,className='',delay=0}){
 const ref=useRef(null); const [visible,setVisible]=useState(false);
 useEffect(()=>{const el=ref.current;if(!el)return;const io=new IntersectionObserver(([entry])=>{if(entry.isIntersecting){setVisible(true);io.disconnect()}},{threshold:.14});io.observe(el);return()=>io.disconnect()},[]);
 return <div ref={ref} className={`reveal ${visible?'is-visible':''} ${className}`} style={{'--delay':`${delay}ms`}}>{children}</div>
}
