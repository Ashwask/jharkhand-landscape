import json
model=json.load(open("model.json"))
geo=json.load(open("jh_enriched.geojson"))
MODEL=json.dumps(model, separators=(',',':'))
GEO=json.dumps(geo, separators=(',',':'))

HTML = r'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jharkhand Landscape — Who Does What Where</title>
<style>
:root{
 --ink:#0f2440; --ink2:#31456a; --mut:#6b7a93; --line:#dce3ee; --line2:#eef2f8;
 --bg:#f6f8fc; --card:#ffffff; --accent:#0d6e8c; --accent2:#c2410c; --gold:#b45309;
 --c0:#eef2f8; --hl:#0d6e8c;
 --shadow:0 1px 2px rgba(15,36,64,.04),0 6px 24px rgba(15,36,64,.06);
}
*{box-sizing:border-box}
html,body{margin:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
 background:var(--bg); color:var(--ink); font-size:14px; line-height:1.45; -webkit-font-smoothing:antialiased;}
.wrap{max-width:1320px; margin:0 auto; padding:28px 22px 80px}
h1{font-size:23px; margin:0 0 3px; letter-spacing:-.02em; font-weight:700}
.sub{color:var(--mut); font-size:13px; margin:0 0 2px}
.prov{color:var(--mut); font-size:11.5px; margin:6px 0 0}
a{color:var(--accent)}
.strip{display:flex; gap:12px; flex-wrap:wrap; margin:20px 0 22px}
.stat{background:var(--card); border:1px solid var(--line); border-radius:12px; padding:12px 15px; min-width:120px; box-shadow:var(--shadow)}
.stat .n{font-size:22px; font-weight:700; letter-spacing:-.02em; line-height:1}
.stat .l{color:var(--mut); font-size:11px; margin-top:5px; text-transform:uppercase; letter-spacing:.04em}
.stat.warn .n{color:var(--accent2)}
.grid{display:grid; grid-template-columns:1.35fr 1fr; gap:18px; align-items:start}
@media(max-width:960px){.grid{grid-template-columns:1fr}}
.card{background:var(--card); border:1px solid var(--line); border-radius:14px; box-shadow:var(--shadow)}
.card h2{font-size:13px; text-transform:uppercase; letter-spacing:.05em; color:var(--ink2); margin:0; padding:14px 16px; border-bottom:1px solid var(--line2)}
.cardpad{padding:14px 16px}
.lens{display:flex; gap:6px; flex-wrap:wrap; padding:12px 16px 0}
.lens button{font:inherit; font-size:12px; border:1px solid var(--line); background:#fff; color:var(--ink2);
 padding:6px 11px; border-radius:8px; cursor:pointer; transition:.12s}
.lens button:hover{border-color:var(--accent)}
.lens button.on{background:var(--ink); color:#fff; border-color:var(--ink)}
svg.map{width:100%; height:auto; display:block}
.dist{stroke:#fff; stroke-width:.8; cursor:pointer; transition:fill .2s}
.dist:hover{stroke:var(--ink); stroke-width:1.6}
.dist.sel{stroke:var(--ink); stroke-width:2}
.dlabel{font-size:8.5px; fill:#25324a; pointer-events:none; text-anchor:middle; font-weight:500}
.dlabel.lite{fill:#eaf0f8}
.legend{display:flex; align-items:center; gap:10px; flex-wrap:wrap; padding:8px 16px 16px; font-size:11.5px; color:var(--mut)}
.legend .sw{display:inline-flex; align-items:center; gap:5px}
.legend .box{width:14px; height:12px; border-radius:3px; border:1px solid rgba(0,0,0,.05)}
.legtitle{font-size:11px; text-transform:uppercase; letter-spacing:.04em; color:var(--ink2); font-weight:600}
/* detail */
#detail .empty{color:var(--mut); font-size:13px; padding:26px 16px; text-align:center}
.dh{display:flex; align-items:baseline; justify-content:space-between; gap:8px; margin-bottom:2px}
.dh .name{font-size:17px; font-weight:700}
.badge{font-size:10.5px; padding:2px 8px; border-radius:20px; font-weight:600; white-space:nowrap}
.badge.asp{background:#fdece3; color:var(--accent2)}
.badge.tri{background:#e2f1f6; color:var(--accent)}
.kv{display:flex; gap:18px; margin:10px 0 4px; flex-wrap:wrap}
.kv .k{color:var(--mut); font-size:11px; text-transform:uppercase; letter-spacing:.03em}
.kv .v{font-size:16px; font-weight:700}
.sec{margin-top:14px}
.sec .t{font-size:11px; text-transform:uppercase; letter-spacing:.04em; color:var(--ink2); font-weight:600; margin-bottom:6px}
.chips{display:flex; gap:5px; flex-wrap:wrap}
.chip{font-size:11.5px; padding:3px 9px; border-radius:7px; background:var(--c0); color:var(--ink2); border:1px solid var(--line)}
.plist{list-style:none; margin:0; padding:0}
.plist li{padding:6px 0; border-bottom:1px solid var(--line2); font-size:13px}
.plist li:last-child{border:0}
.blk{font-size:12px; color:var(--ink2); background:var(--c0); border-radius:8px; padding:8px 10px; margin-top:4px}
.spark{display:flex; align-items:flex-end; gap:3px; height:44px; margin-top:6px}
.spark .bar{flex:1; background:var(--accent); border-radius:2px 2px 0 0; min-height:2px; opacity:.85}
.spark .bar:hover{opacity:1}
.sparkx{display:flex; justify-content:space-between; font-size:9px; color:var(--mut); margin-top:3px}
/* matrix */
.mtx{overflow-x:auto}
table{border-collapse:collapse; width:100%; font-size:12.5px}
.mtx th{font-weight:600; color:var(--ink2); text-align:left; padding:7px 8px; position:sticky; top:0; background:#fff}
.mtx{padding-top:6px}
.mtx th.rot{vertical-align:bottom; padding:0; text-align:center}
.mtx th.rot > div{writing-mode:vertical-rl; transform:rotate(180deg); white-space:nowrap; font-size:11px; line-height:1; font-weight:600; margin:0 auto; padding:8px 0 6px; color:var(--ink2)}
.mtx thead th{border-bottom:2px solid var(--line)}
.mtx td{text-align:center; padding:0; border:1px solid var(--line2)}
.mtx td.name{text-align:left; padding:6px 8px; white-space:nowrap; font-weight:500; color:var(--ink)}
.cell{width:26px; height:26px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:10px; font-weight:700}
.mtx td.tot{font-weight:700; color:var(--ink2); background:#f8fafd}
/* directory + table */
.tbl{overflow-x:auto}
.tbl table{font-size:12.5px}
.tbl th{text-align:left; padding:9px 10px; border-bottom:2px solid var(--line); color:var(--ink2); cursor:pointer; user-select:none; white-space:nowrap}
.tbl th:hover{color:var(--accent)}
.tbl td{padding:8px 10px; border-bottom:1px solid var(--line2); vertical-align:top}
.tbl tr:hover td{background:#f8fafd}
.tbl .num{text-align:right; font-variant-numeric:tabular-nums}
.tag{font-size:10.5px; padding:1px 6px; border-radius:5px; background:var(--c0); color:var(--ink2); margin:1px 2px 1px 0; display:inline-block; border:1px solid var(--line)}
.mini{color:var(--mut); font-size:11px}
.dot{width:8px; height:8px; border-radius:50%; display:inline-block; margin-right:4px}
.section-title{font-size:15px; font-weight:700; margin:30px 0 4px; letter-spacing:-.01em}
.section-sub{color:var(--mut); font-size:12px; margin:0 0 12px}
.foot{color:var(--mut); font-size:11px; margin-top:34px; border-top:1px solid var(--line); padding-top:14px}
.pill{cursor:pointer}
/* ecosystem health */
.health{display:grid; grid-template-columns:1.1fr 2fr; gap:14px}
@media(max-width:760px){.health{grid-template-columns:1fr}}
.hindex{background:linear-gradient(155deg,#0f2440,#22406e); color:#fff; border-radius:14px; padding:20px 22px; display:flex; flex-direction:column; justify-content:center}
.hindex .big{font-size:48px; font-weight:800; letter-spacing:-.03em; line-height:.95}
.hindex .big small{font-size:19px; opacity:.65; font-weight:600}
.hindex .lbl{font-size:11.5px; text-transform:uppercase; letter-spacing:.06em; opacity:.8; margin-top:4px}
.hindex .band{align-self:flex-start; margin-top:13px; font-size:12px; font-weight:700; padding:4px 13px; border-radius:20px}
.hindex .desc{font-size:12.5px; opacity:.9; margin-top:12px; line-height:1.45}
.hcards{display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px}
@media(max-width:760px){.hcards{grid-template-columns:1fr 1fr}}
.hc{border:1px solid var(--line); border-radius:12px; padding:12px 13px; background:#fff}
.hc .band{font-size:9.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:20px}
.hc .m{font-size:21px; font-weight:700; letter-spacing:-.02em; margin:9px 0 1px}
.hc .nm{font-size:11px; color:var(--ink2); font-weight:600}
.hc .bar{height:5px; background:var(--line2); border-radius:3px; margin:9px 0 7px; overflow:hidden}
.hc .bar > i{display:block; height:100%; border-radius:3px}
.hc .d{font-size:10.5px; color:var(--mut); line-height:1.38}
/* place health */
.ph{padding:4px 16px 14px}
.phrow{display:grid; grid-template-columns:158px 1fr 82px; gap:12px; align-items:center; padding:7px 0; border-bottom:1px solid var(--line2)}
.phrow:last-child{border-bottom:0}
.phrow .pn{font-weight:600; font-size:13px; display:flex; align-items:center; gap:6px; cursor:pointer}
.phrow .pn:hover{color:var(--accent)}
.phrow .track{height:9px; background:var(--line2); border-radius:5px; overflow:hidden}
.phrow .track > i{display:block; height:100%; border-radius:5px}
.phrow .right{display:flex; align-items:center; justify-content:flex-end; gap:8px}
.phrow .sc{font-weight:700; font-variant-numeric:tabular-nums; font-size:13px; min-width:26px; text-align:right}
.tagp{font-size:9px; font-weight:700; padding:2px 7px; border-radius:20px; white-space:nowrap}
.phhead{display:grid; grid-template-columns:158px 1fr 82px; gap:12px; padding:2px 16px 0; font-size:10px; text-transform:uppercase; letter-spacing:.04em; color:var(--mut)}
</style></head>
<body><div class="wrap">
<h1>Jharkhand Landscape — Who Does What Where</h1>
<p class="sub">Partners × districts × themes, with TRI presence, Common Ground blocks and CSR flow. Internal sense-making view.</p>
<p class="prov">Sources: Partners Geography &amp; Thematic focus · TRI Geographic Presence (Jul 2026) · Common Ground block list · Jharkhand CSR data (MCA) · district boundaries © udit-001/india-maps-data (2011 census). District names &amp; themes normalised; some partner rows list out-of-state / town names (kept out of the map).</p>

<div class="strip" id="strip"></div>

<div class="section-title">Ecosystem health</div>
<p class="section-sub">A funder-facing read on the state of the partner ecosystem — coverage, reach into priority districts, resilience, thematic balance, network depth and how well resources track effort.</p>
<div class="card cardpad"><div class="health"><div class="hindex" id="hindex"></div><div class="hcards" id="hcards"></div></div></div>

<div class="grid">
 <div class="card">
   <h2>District map</h2>
   <div class="lens" id="lens"></div>
   <div id="mapbox"></div>
   <div class="legend" id="legend"></div>
 </div>
 <div class="card" id="detail"><h2>District detail</h2>
   <div class="empty" id="detEmpty">Click a district on the map to see partners, themes, blocks and CSR trend.</div>
   <div class="cardpad" id="detBody" style="display:none"></div>
 </div>
</div>

<div class="section-title">Partner × Theme matrix</div>
<p class="section-sub">Where thematic energy concentrates. Cell = 1 if the partner works on that theme; darker = the theme is carried by more partners overall.</p>
<div class="card cardpad mtx" id="matrix"></div>

<div class="section-title">Partner directory</div>
<p class="section-sub">Click a column header to sort. Click a partner's district tag to focus the map.</p>
<div class="card tbl" id="dirtbl"></div>

<div class="section-title">Place health — where attention is needed</div>
<p class="section-sub">Each district scored 0–100 on how well it is served (partner presence 45% · thematic breadth 30% · resilience/no single-point-of-failure 25%), ranked neediest-first. Priority = aspirational &amp; weakly served.</p>
<div class="card">
 <div class="phhead"><span>District</span><span>Coverage strength</span><span style="text-align:right">Score</span></div>
 <div class="ph" id="placehealth"></div>
</div>

<div class="section-title">District coverage table</div>
<p class="section-sub">The full grid: partners, themes, aspirational status (per TRI), TRI presence and latest-year CSR.</p>
<div class="card tbl" id="distbl"></div>

<div class="foot" id="foot"></div>
</div>

<script>
const MODEL=__MODEL__;
const GEO=__GEO__;
const D=MODEL.districts, CANON=MODEL.canon, THEMES=MODEL.themes, YEARS=MODEL.years, PARTNERS=MODEL.partners;
const Y0=YEARS[0];
const fmtCr=v=>'₹'+(v/1e7).toFixed(v/1e7<10?1:0)+' Cr';
const el=(t,c,h)=>{const e=document.createElement(t); if(c)e.className=c; if(h!=null)e.innerHTML=h; return e;};

/* ---------- theme frequency (for matrix shading + dominant) ---------- */
const themeFreq={}; THEMES.forEach(t=>themeFreq[t]=0);
PARTNERS.forEach(p=>p.themes.forEach(t=>{if(t in themeFreq)themeFreq[t]++;}));
const maxTF=Math.max(...Object.values(themeFreq),1);

/* ---------- summary strip ---------- */
const covered=CANON.filter(d=>D[d].partners.length>0).length;
const white=CANON.filter(d=>D[d].partners.length===0);
const csrTot=CANON.reduce((s,d)=>s+(D[d].csr[Y0]||0),0);
const stats=[
 ['24','Districts'],
 [PARTNERS.length,'Partners mapped'],
 [covered,'Districts covered'],
 [white.length,'Whitespace (0 partners)','warn'],
 [CANON.filter(d=>D[d].aspirational).length,'Aspirational (TRI)'],
 [fmtCr(csrTot),'CSR '+Y0]
];
const strip=document.getElementById('strip');
stats.forEach(s=>{const c=el('div','stat'+(s[2]?' '+s[2]:'')); c.appendChild(el('div','n',s[0])); c.appendChild(el('div','l',s[1])); strip.appendChild(c);});

/* ---------- projection (equirectangular fit) ---------- */
function bounds(){let mnx=1e9,mny=1e9,mxx=-1e9,mxy=-1e9;
 GEO.features.forEach(f=>eachCoord(f.geometry,(x,y)=>{if(x<mnx)mnx=x;if(x>mxx)mxx=x;if(y<mny)mny=y;if(y>mxy)mxy=y;}));
 return [mnx,mny,mxx,mxy];}
function eachCoord(g,cb){const c=g.coordinates;
 const walk=a=>{if(typeof a[0]==='number'){cb(a[0],a[1]);}else a.forEach(walk);}; walk(c);}
const W=760,H=560,PAD=26;
const [mnx,mny,mxx,mxy]=bounds();
const midLat=(mny+mxy)/2, kx=Math.cos(midLat*Math.PI/180);
const bw=(mxx-mnx)*kx, bh=(mxy-mny);
const sc=Math.min((W-2*PAD)/bw,(H-2*PAD)/bh);
const ox=(W-bw*sc)/2, oy=(H-bh*sc)/2;
const px=x=>ox+((x-mnx)*kx)*sc;
const py=y=>oy+(mxy-y)*sc;
function pathFor(g){let d='';
 const ring=r=>{r.forEach((pt,i)=>{d+=(i?'L':'M')+px(pt[0]).toFixed(1)+' '+py(pt[1]).toFixed(1);});d+='Z';};
 if(g.type==='Polygon')g.coordinates.forEach(ring);
 else g.coordinates.forEach(poly=>poly.forEach(ring));
 return d;}
function centroid(g){let sx=0,sy=0,n=0;eachCoord(g,(x,y)=>{sx+=x;sy+=y;n++;});return [px(sx/n),py(sy/n)];}

/* ---------- color scales ---------- */
const seq=['#eaf1f7','#cfe0ee','#a7c7e0','#6fa3cc','#3f7cb0','#1f5a8f','#0d3c6b']; // blue seq
function seqColor(v,max){if(!max||v<=0)return '#f1f5fa'; const t=v/max; const i=Math.min(seq.length-1,Math.floor(t*(seq.length-1)+0.001)); return seq[Math.max(1,i)];}
const themePalette={}; const TP=['#0d6e8c','#c2410c','#4d7c2f','#7c3a86','#b45309','#1f5a8f','#0e8074','#a1344b','#5b6bbf','#8a6d1a','#2b8a3e','#9a3412'];
THEMES.forEach((t,i)=>themePalette[t]=TP[i%TP.length]);

/* ---------- lenses ---------- */
const maxP=Math.max(...CANON.map(d=>D[d].partners.length));
const maxCSR=Math.max(...CANON.map(d=>D[d].csr[Y0]||0));
const maxT=Math.max(...CANON.map(d=>D[d].themes.length));
const lenses={
 partners:{label:'Partner density',fill:d=>seqColor(D[d].partners.length,maxP),
   legend:()=>gradLegend('# partners',maxP)},
 themes:{label:'Theme breadth',fill:d=>seqColor(D[d].themes.length,maxT),
   legend:()=>gradLegend('# themes',maxT)},
 csr:{label:'CSR spend '+Y0,fill:d=>seqColor(D[d].csr[Y0]||0,maxCSR),
   legend:()=>gradLegend('CSR (₹)',maxCSR,true)},
 dom:{label:'Dominant theme',fill:d=>{const t=domTheme(d);return t?themePalette[t]:'#f1f5fa';},
   legend:()=>themeLegend()},
 gap:{label:'Coverage gap',fill:d=>{const v=D[d];if(v.partners.length===0&&v.aspirational)return '#c2410c';
     if(v.partners.length===0)return '#e79a6a'; if(v.aspirational&&v.partners.length<=1)return '#f0c088'; return '#cfe0d8';},
   legend:()=>gapLegend()}
};
function domTheme(d){const f={};PARTNERS.forEach(p=>{if(p.districts.includes(d))p.themes.forEach(t=>f[t]=(f[t]||0)+1);});
 let best=null,bv=0;for(const k in f)if(f[k]>bv){bv=f[k];best=k;}return best;}
let curLens='partners', selD=null;

/* legends */
function gradLegend(title,max,money){const w=el('div');w.appendChild(el('span','legtitle',title));
 const grad=el('div'); grad.style.cssText='display:flex;gap:0;border-radius:4px;overflow:hidden';
 seq.forEach(c=>{const b=el('div');b.style.cssText='width:24px;height:12px;background:'+c;grad.appendChild(b);});
 w.appendChild(grad);
 w.appendChild(el('span','',money?('0 → '+fmtCr(max)):('0 → '+max)));
 w.style.cssText='display:flex;align-items:center;gap:8px;flex-wrap:wrap';return w;}
function themeLegend(){const w=el('div');w.style.cssText='display:flex;gap:10px;flex-wrap:wrap';
 const used=[...new Set(CANON.map(domTheme).filter(Boolean))];
 used.forEach(t=>{const s=el('span','sw');const b=el('span','box');b.style.background=themePalette[t];s.appendChild(b);s.appendChild(el('span','',t));w.appendChild(s);});return w;}
function gapLegend(){const items=[['#c2410c','Whitespace + aspirational'],['#e79a6a','Whitespace'],['#f0c088','Aspirational, thin (≤1)'],['#cfe0d8','Covered']];
 const w=el('div');w.style.cssText='display:flex;gap:12px;flex-wrap:wrap';
 items.forEach(i=>{const s=el('span','sw');const b=el('span','box');b.style.background=i[0];s.appendChild(b);s.appendChild(el('span','',i[1]));w.appendChild(s);});return w;}

/* build map */
const mapbox=document.getElementById('mapbox');
const svgNS='http://www.w3.org/2000/svg';
const svg=document.createElementNS(svgNS,'svg');
svg.setAttribute('viewBox','0 0 '+W+' '+H); svg.setAttribute('class','map');
const paths={},labels={};
GEO.features.forEach(f=>{const name=f.properties.district;
 const p=document.createElementNS(svgNS,'path');
 p.setAttribute('d',pathFor(f.geometry)); p.setAttribute('class','dist'); p.dataset.d=name;
 p.addEventListener('click',()=>selectDist(name));
 p.addEventListener('mousemove',ev=>showTip(ev,name));
 p.addEventListener('mouseleave',hideTip);
 svg.appendChild(p); paths[name]=p;
 const [cx,cy]=centroid(f.geometry);
 const tx=document.createElementNS(svgNS,'text'); tx.setAttribute('x',cx); tx.setAttribute('y',cy);
 tx.setAttribute('class','dlabel'); tx.textContent=name.replace('-Kharsawan','').replace(' Singhbhum','.S');
 svg.appendChild(tx); labels[name]=tx;
});
mapbox.appendChild(svg);

/* tooltip */
const tip=el('div'); tip.style.cssText='position:fixed;pointer-events:none;background:#0f2440;color:#fff;padding:7px 10px;border-radius:8px;font-size:12px;box-shadow:0 6px 20px rgba(0,0,0,.25);z-index:99;display:none;max-width:230px';
document.body.appendChild(tip);
function showTip(ev,name){const v=D[name];
 tip.innerHTML='<b>'+name+'</b><br>'+v.partners.length+' partner'+(v.partners.length!=1?'s':'')+' · '+v.themes.length+' themes<br>CSR '+Y0+': '+fmtCr(v.csr[Y0]||0)+(v.aspirational?' · <span style="color:#f0a878">Aspirational</span>':'');
 tip.style.display='block'; tip.style.left=Math.min(ev.clientX+14,innerWidth-240)+'px'; tip.style.top=(ev.clientY+14)+'px';}
function hideTip(){tip.style.display='none';}

/* lens buttons */
const lensBox=document.getElementById('lens');
Object.entries(lenses).forEach(([k,v])=>{const b=el('button',k===curLens?'on':'',v.label);b.onclick=()=>{curLens=k;paint();};lensBox.appendChild(b);});
function paint(){
 [...lensBox.children].forEach(b=>b.classList.toggle('on',b.textContent===lenses[curLens].label));
 CANON.forEach(d=>{const f=lenses[curLens].fill(d); paths[d].setAttribute('fill',f);
   // label contrast
   const dark=isDark(f); labels[d].classList.toggle('lite',dark);});
 const lg=document.getElementById('legend'); lg.innerHTML=''; lg.appendChild(lenses[curLens].legend());
}
function isDark(hex){if(!hex||hex[0]!=='#'||hex.length<7)return false;const r=parseInt(hex.slice(1,3),16),g=parseInt(hex.slice(3,5),16),b=parseInt(hex.slice(5,7),16);return (0.299*r+0.587*g+0.114*b)<140;}

/* detail */
function selectDist(name){selD=name;
 Object.values(paths).forEach(p=>p.classList.remove('sel')); paths[name].classList.add('sel');
 const v=D[name]; document.getElementById('detEmpty').style.display='none';
 const body=document.getElementById('detBody'); body.style.display='block';
 const dp=PARTNERS.filter(p=>p.districts.includes(name));
 let h='<div class="dh"><span class="name">'+name+'</span><span>';
 if(v.aspirational)h+='<span class="badge asp">Aspirational</span> ';
 if(v.tri)h+='<span class="badge tri">TRI</span>';
 h+='</span></div>';
 h+='<div class="kv"><div><div class="k">Partners</div><div class="v">'+v.partners.length+'</div></div>'
   +'<div><div class="k">Themes</div><div class="v">'+v.themes.length+'</div></div>'
   +'<div><div class="k">CSR '+Y0+'</div><div class="v">'+fmtCr(v.csr[Y0]||0)+'</div></div></div>';
 h+='<div class="sec"><div class="t">Partners here</div>';
 if(dp.length){h+='<ul class="plist">';dp.forEach(p=>{h+='<li><b>'+p.name+'</b><br><span class="mini">'+p.themes.join(' · ')+'</span></li>';});h+='</ul>';}
 else h+='<div class="mini">No mapped partner. '+(v.aspirational?'Aspirational district — whitespace.':'')+'</div>';
 h+='</div>';
 if(v.themes.length){h+='<div class="sec"><div class="t">Themes active</div><div class="chips">'+v.themes.map(t=>'<span class="chip" style="border-left:3px solid '+(themePalette[t]||'#ccc')+'">'+t+'</span>').join('')+'</div></div>';}
 if(v.tri&&v.tri.blocks){h+='<div class="sec"><div class="t">TRI community action lab</div><div class="blk">'+v.tri.blocks+'</div></div>';}
 if(v.cg&&v.cg.blocks){h+='<div class="sec"><div class="t">Common Ground blocks</div><div class="blk">'+v.cg.blocks+'</div></div>';}
 // CSR sparkline
 const yr=[...YEARS].reverse(); const vals=yr.map(y=>v.csr[y]||0); const mx=Math.max(...vals,1);
 h+='<div class="sec"><div class="t">CSR spend trend (₹ Cr)</div><div class="spark">';
 vals.forEach(val=>{h+='<div class="bar" style="height:'+(val/mx*100)+'%" title="'+fmtCr(val)+'"></div>';});
 h+='</div><div class="sparkx"><span>'+yr[0].slice(0,4)+'</span><span>'+yr[yr.length-1].slice(2)+'</span></div></div>';
 body.innerHTML=h;
 body.scrollIntoView&&window.matchMedia('(max-width:960px)').matches&&body.scrollIntoView({behavior:'smooth',block:'nearest'});
}

/* ---------- matrix ---------- */
const THSHORT={'Health & Nutrition':'Health','Women & Gender':'Women','Climate Action':'Climate','Livelihoods & Rural Dev':'Livelihoods','Natural Resource Mgmt':'NRM','Water & Sanitation':'WASH','Skill Development':'Skills','Clean Energy':'Energy','Child Protection':'Child Prot.'};
const shortT=t=>THSHORT[t]||t;
function buildMatrix(){
 const rows=[...PARTNERS].sort((a,b)=>b.themes.length-a.themes.length);
 let h='<table><thead><tr><th>Partner</th>';
 THEMES.forEach(t=>h+='<th class="rot" title="'+t+'"><div>'+shortT(t)+'</div></th>');
 h+='<th class="tot">n</th></tr></thead><tbody>';
 rows.forEach(p=>{h+='<tr><td class="name">'+p.name+'</td>';
   THEMES.forEach(t=>{const on=p.themes.includes(t);
     const shade=on?0.35+0.65*(themeFreq[t]/maxTF):0;
     const bg=on?'rgba(13,110,140,'+shade.toFixed(2)+')':'#fff';
     h+='<td><div class="cell" style="background:'+bg+'">'+(on?'●':'')+'</div></td>';});
   h+='<td class="tot">'+p.themes.length+'</td></tr>';});
 // footer totals
 h+='<tr><td class="name" style="font-weight:700">Partners / theme</td>';
 THEMES.forEach(t=>h+='<td class="tot">'+themeFreq[t]+'</td>');
 h+='<td class="tot"></td></tr>';
 h+='</tbody></table>';
 document.getElementById('matrix').innerHTML=h;
}

/* ---------- partner directory ---------- */
let dirSort={k:'name',asc:true};
function buildDir(){
 const box=document.getElementById('dirtbl');
 const cols=[['name','Partner'],['districts','Districts'],['themes','Themes'],['nd','#Dist']];
 let rows=PARTNERS.map(p=>({name:p.name,districts:p.districts,themes:p.themes,nd:p.districts.length}));
 rows.sort((a,b)=>{let x=a[dirSort.k],y=b[dirSort.k];if(Array.isArray(x)){x=x.length;y=y.length;}if(typeof x==='string')return dirSort.asc?x.localeCompare(y):y.localeCompare(x);return dirSort.asc?x-y:y-x;});
 let h='<table><thead><tr>';cols.forEach(c=>h+='<th data-k="'+c[0]+'">'+c[1]+(dirSort.k===c[0]?(dirSort.asc?' ▲':' ▼'):'')+'</th>');h+='</tr></thead><tbody>';
 rows.forEach(p=>{h+='<tr><td><b>'+p.name+'</b></td><td>'+
   (p.districts.length?p.districts.map(d=>'<span class="tag pill" data-d="'+d+'">'+d.replace('-Kharsawan','-K.')+'</span>').join(''):'<span class="mini">—</span>')+
   '</td><td>'+p.themes.map(t=>'<span class="tag" style="border-left:3px solid '+(themePalette[t]||'#ccc')+'">'+t+'</span>').join('')+
   '</td><td class="num">'+p.nd+'</td></tr>';});
 h+='</tbody></table>'; box.innerHTML=h;
 box.querySelectorAll('th').forEach(th=>th.onclick=()=>{const k=th.dataset.k;dirSort.asc=dirSort.k===k?!dirSort.asc:true;dirSort.k=k;buildDir();});
 box.querySelectorAll('.pill').forEach(s=>s.onclick=()=>{selectDist(s.dataset.d);document.getElementById('mapbox').scrollIntoView({behavior:'smooth',block:'center'});});
}

/* ---------- district table ---------- */
let disSort={k:'partners',asc:false};
function buildDisTbl(){
 const box=document.getElementById('distbl');
 let rows=CANON.map(d=>({d,partners:D[d].partners.length,themes:D[d].themes.length,
   asp:D[d].aspirational?1:0,tri:D[d].tri?1:0,csr:D[d].csr[Y0]||0,plist:D[d].partners}));
 rows.sort((a,b)=>{let x=a[disSort.k],y=b[disSort.k];if(typeof x==='string')return disSort.asc?x.localeCompare(y):y.localeCompare(x);return disSort.asc?x-y:y-x;});
 const cols=[['d','District'],['partners','Partners'],['themes','Themes'],['asp','Asp.'],['tri','TRI'],['csr','CSR '+Y0]];
 let h='<table><thead><tr>';cols.forEach(c=>h+='<th data-k="'+c[0]+'"'+(c[0]!=='d'?' class="num"':'')+'>'+c[1]+(disSort.k===c[0]?(disSort.asc?' ▲':' ▼'):'')+'</th>');h+='<th>Who</th></tr></thead><tbody>';
 rows.forEach(r=>{const bg=r.partners===0?'background:#fdf3ee':'';
   h+='<tr style="'+bg+'"><td><span class="dot" style="background:'+seqColor(r.partners,maxP)+'"></span><b class="pill" data-d="'+r.d+'">'+r.d+'</b></td>'
    +'<td class="num">'+r.partners+'</td><td class="num">'+r.themes+'</td>'
    +'<td class="num">'+(r.asp?'<span style="color:#c2410c">●</span>':'–')+'</td>'
    +'<td class="num">'+(r.tri?'<span style="color:#0d6e8c">●</span>':'–')+'</td>'
    +'<td class="num">'+fmtCr(r.csr)+'</td>'
    +'<td class="mini">'+(r.plist.join(', ')||'—')+'</td></tr>';});
 h+='</tbody></table>'; box.innerHTML=h;
 box.querySelectorAll('th').forEach(th=>th.onclick=()=>{const k=th.dataset.k;disSort.asc=disSort.k===k?!disSort.asc:(k==='d');disSort.k=k;buildDisTbl();});
 box.querySelectorAll('.pill').forEach(s=>s.onclick=()=>{selectDist(s.dataset.d);document.getElementById('mapbox').scrollIntoView({behavior:'smooth',block:'center'});});
}

document.getElementById('foot').innerHTML='Fully self-contained (offline) · '+PARTNERS.length+' partners across '+covered+'/24 districts · Whitespace: <b>'+white.join(', ')+'</b> (all aspirational). Anchors: '+MODEL.anchors.map(a=>a.name).join(', ')+'.';

/* ---------- ecosystem + place health ---------- */
const BAND={strong:['#2b8a3e','#e7f3ea','Strong'],mod:['#b45309','#fdf0e2','Moderate'],weak:['#c2410c','#fdece3','Weak']};
function band(s){return s>=75?'strong':s>=50?'mod':'weak';}
function pearson(xs,ys){const n=xs.length,mx=xs.reduce((a,b)=>a+b,0)/n,my=ys.reduce((a,b)=>a+b,0)/n;
 let c=0,sx=0,sy=0;for(let i=0;i<n;i++){c+=(xs[i]-mx)*(ys[i]-my);sx+=(xs[i]-mx)**2;sy+=(ys[i]-my)**2;}
 return (sx&&sy)?c/Math.sqrt(sx*sy):0;}

function buildHealth(){
 const cov=CANON.filter(d=>D[d].partners.length);
 const asp=CANON.filter(d=>D[d].aspirational);
 const aspCov=asp.filter(d=>D[d].partners.length);
 const single=CANON.filter(d=>D[d].partners.length===1);
 const wht=CANON.filter(d=>!D[d].partners.length);
 const tf={};THEMES.forEach(t=>tf[t]=0);PARTNERS.forEach(p=>p.themes.forEach(t=>{if(t in tf)tf[t]++;}));
 const fragile=THEMES.filter(t=>tf[t]>0&&tf[t]<=2);
 const hubs=CANON.filter(d=>D[d].partners.length>=3);
 const avgP=cov.reduce((s,d)=>s+D[d].partners.length,0)/cov.length;
 const r=pearson(CANON.map(d=>D[d].csr[Y0]||0),CANON.map(d=>D[d].partners.length));
 const csrCov=CANON.reduce((s,d)=>s+(D[d].partners.length?(D[d].csr[Y0]||0):0),0)/csrTot*100;
 const dims=[
  {n:'Geographic coverage',v:cov.length+'/24',s:cov.length/24*100,d:Math.round(cov.length/24*100)+'% of districts have ≥1 mapped partner.'},
  {n:'Aspirational reach',v:aspCov.length+'/'+asp.length,s:aspCov.length/asp.length*100,d:(asp.length-aspCov.length)+' priority districts still unserved: '+asp.filter(d=>!D[d].partners.length).join(', ')+'.'},
  {n:'Resilience',v:(24-wht.length-single.length)+'/24',s:(24-wht.length-single.length)/24*100,d:single.length+' single-partner + '+wht.length+' zero-partner districts = key-person risk.'},
  {n:'Thematic balance',v:(THEMES.length-fragile.length)+'/'+THEMES.length,s:(THEMES.length-fragile.length)/THEMES.length*100,d:'Thin themes (≤2 partners): '+fragile.join(', ')+'.'},
  {n:'Network depth',v:hubs.length+' hubs',s:hubs.length/24*100,d:hubs.length+' districts with ≥3 partners; avg '+avgP.toFixed(1)+' where present.'},
  {n:'Resource alignment',v:'r = '+r.toFixed(2),s:(r+1)/2*100,d:Math.round(csrCov)+'% of CSR lands in covered districts, but flow barely tracks partner effort — deliberate co-location is untapped.'}
 ];
 const W={0:.15,1:.25,2:.20,3:.15,4:.15,5:.10};
 const idx=Math.round(dims.reduce((s,dm,i)=>s+dm.s*W[i],0));
 const b=BAND[band(idx)];
 document.getElementById('hindex').innerHTML=
  '<div class="big">'+idx+'<small>/100</small></div><div class="lbl">Ecosystem Health Index</div>'
  +'<span class="band" style="background:'+b[1]+';color:'+b[0]+'">'+b[2]+'</span>'
  +'<div class="desc">Solid footprint ('+cov.length+'/24 districts, '+aspCov.length+'/'+asp.length+' aspirational) held back by <b>thin depth</b> ('+hubs.length+' hubs, '+(single.length+wht.length)+' fragile/empty districts) and <b>weak resource alignment</b>. Widen into whitespace, thicken single-partner districts, and co-locate CSR.</div>';
 document.getElementById('hcards').innerHTML=dims.map(dm=>{const bb=BAND[band(dm.s)];
  return '<div class="hc"><span class="band" style="background:'+bb[1]+';color:'+bb[0]+'">'+bb[2]+'</span>'
   +'<div class="m">'+dm.v+'</div><div class="nm">'+dm.n+'</div>'
   +'<div class="bar"><i style="width:'+Math.round(dm.s)+'%;background:'+bb[0]+'"></i></div>'
   +'<div class="d">'+dm.d+'</div></div>';}).join('');
}

function placeScore(d){const p=D[d].partners.length,t=D[d].themes.length;
 const sp=Math.min(p/3,1)*45, st=Math.min(t/10,1)*30, sr=(p>=2?1:p===1?.4:0)*25;
 return Math.round(sp+st+sr);}
function buildPlaceHealth(){
 const rows=CANON.map(d=>{const p=D[d].partners.length,s=placeScore(d),asp=D[d].aspirational;
  let tag,tc,tb,need;
  if(p===0&&asp){tag='Whitespace';tc='#c2410c';tb='#fdece3';need=0;}
  else if(p===0){tag='Uncovered';tc='#b45309';tb='#fdf0e2';need=1;}
  else if(asp&&s<55){tag='Priority';tc='#b45309';tb='#fdf0e2';need=2;}
  else if(p===1){tag='Fragile';tc='#b45309';tb='#fdf0e2';need=3;}
  else{tag='Served';tc='#2b8a3e';tb='#e7f3ea';need=4;}
  return {d,s,asp,tag,tc,tb,need};});
 rows.sort((a,b)=>a.need-b.need||a.s-b.s);
 document.getElementById('placehealth').innerHTML=rows.map(r=>{const bc=BAND[band(r.s)][0];
  return '<div class="phrow"><span class="pn" data-d="'+r.d+'">'
   +(r.asp?'<span class="dot" style="background:#c2410c" title="Aspirational"></span>':'<span class="dot" style="background:#cdd7e6"></span>')+r.d+'</span>'
   +'<span class="track"><i style="width:'+Math.max(r.s,2)+'%;background:'+bc+'"></i></span>'
   +'<span class="right"><span class="tagp" style="background:'+r.tb+';color:'+r.tc+'">'+r.tag+'</span><span class="sc">'+r.s+'</span></span></div>';}).join('');
 document.querySelectorAll('#placehealth .pn').forEach(s=>s.onclick=()=>{selectDist(s.dataset.d);document.getElementById('mapbox').scrollIntoView({behavior:'smooth',block:'center'});});
}

paint(); buildHealth(); buildMatrix(); buildPlaceHealth(); buildDir(); buildDisTbl();
</script></body></html>'''

HTML = HTML.replace('__MODEL__', MODEL).replace('__GEO__', GEO)
open("index.html","w").write(HTML)
print("wrote index.html", len(HTML), "bytes")
