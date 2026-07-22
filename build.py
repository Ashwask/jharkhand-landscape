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
.grid.hero{margin-top:20px}
.grid.hero .card h2{font-size:14px}
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
.mtx thead th{border-bottom:2px solid var(--line); vertical-align:bottom}
.mtx thead th.tot{padding-bottom:8px; font-size:12px; text-align:center}
.mtx thead th:first-child{padding-bottom:8px}
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
.collapser{cursor:pointer; user-select:none; display:block}
.collapser .caret{display:inline-block; font-size:12px; color:var(--mut); margin-left:7px; transition:transform .15s}
.collapser.closed .caret{transform:rotate(-90deg)}
.collapsed{display:none}
.srcgrid{display:grid; grid-template-columns:repeat(3,1fr); gap:18px 22px}
@media(max-width:760px){.srcgrid{grid-template-columns:1fr 1fr}}
.srch{font-size:11px; text-transform:uppercase; letter-spacing:.05em; color:var(--ink2); font-weight:700; margin-bottom:6px}
.srcs ul{margin:0; padding:0; list-style:none}
.srcs li{font-size:12px; color:var(--mut); padding:3px 0; line-height:1.35}
.srcs a{color:var(--accent); text-decoration:none}
.srcs a:hover{text-decoration:underline}
.exttoggle{display:inline-flex; align-items:center; gap:8px; margin:0 0 12px; padding:8px 13px; border:1px solid var(--line); border-radius:9px; background:#fff; font-size:12.5px; color:var(--ink2); cursor:pointer; box-shadow:var(--shadow)}
.exttoggle input{width:15px; height:15px; accent-color:var(--gold); cursor:pointer}
.exttoggle:hover{border-color:var(--gold)}
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

<div class="grid hero">
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

<div class="strip" id="strip"></div>

<div class="section-title">Ecosystem health</div>
<p class="section-sub">A funder-facing read on the state of the partner ecosystem — coverage, reach into priority districts, resilience, thematic balance, network depth and how well resources track effort.</p>
<label class="exttoggle"><input type="checkbox" id="extToggle"> Include <span style="color:#b07a1f">✳ indicative</span> orgs (PRADAN, CInI, CEED…) in the scoring, map &amp; tables</label>
<div class="card cardpad"><div class="health"><div class="hindex" id="hindex"></div><div class="hcards" id="hcards"></div></div></div>

<div class="section-title">Partner × Theme matrix</div>
<p class="section-sub">Where thematic energy concentrates. <span style="color:#0d6e8c">●</span> teal = source-file partner · <span style="color:#b07a1f">●</span> gold = ✳ indicative org (theme keyword-mapped from its focus). Footer = orgs per theme (source + indicative, with source-only in grey).</p>
<div class="card cardpad mtx" id="matrix"></div>

<div class="section-title collapser closed" id="dirToggle" data-wrap="dirwrap">Partner directory <span class="caret">▾</span> <span class="mini" style="font-weight:400" id="dircount"></span></div>
<div id="dirwrap" class="collapsed">
<p class="section-sub">All implementing organisations — your source-file partners plus <span style="color:#b07a1f">✳ indicative</span> orgs compiled from public sources (PRADAN, CInI, CEED, Tata Steel Foundation…). Click a column header to sort; click a district tag to focus the map.</p>
<div class="card tbl" id="dirtbl"></div>
</div>

<div class="section-title collapser closed" data-wrap="phwrap">Place health — where attention is needed <span class="caret">▾</span></div>
<div id="phwrap" class="collapsed">
<p class="section-sub">Each district scored 0–100 on how well it is served (partner presence 45% · thematic breadth 30% · resilience/no single-point-of-failure 25%), ranked neediest-first. Priority = aspirational &amp; weakly served.</p>
<div class="card">
 <div class="phhead"><span>District</span><span>Coverage strength</span><span style="text-align:right">Score</span></div>
 <div class="ph" id="placehealth"></div>
</div>
</div>

<div class="section-title collapser closed" data-wrap="dcwrap">District coverage table <span class="caret">▾</span></div>
<div id="dcwrap" class="collapsed">
<p class="section-sub">The full grid: partners, themes, aspirational status (per TRI), TRI presence and latest-year CSR.</p>
<div class="card tbl" id="distbl"></div>
</div>

<div class="section-title">Funders &amp; philanthropies present <span style="color:#b07a1f">✳ indicative</span></div>
<p class="section-sub">Who funds whom in Jharkhand. The <b>“Supports in Jharkhand”</b> column links each funder to the implementing org(s) it backs here (gold tags match the Partner directory); where a funder's local grantees aren't public, that's stated plainly. Compiled from public sources, kept out of the health scores.</p>
<div class="card"><div class="tbl" id="extfund"></div></div>

<div class="section-title">Government spend &amp; allocation <span style="color:#8a4fbf">✳ indicative</span></div>
<p class="section-sub">The largest place-based public money in Jharkhand. <b>DMF (District Mineral Foundation)</b> is district-specific and concentrated in the coal/iron belt — see the <b>“DMF mining fund ✳”</b> map lens. State &amp; central schemes are largely statewide. Figures from public sources (CSE, state budget, press); DMF district split is cumulative to Mar-2018 and total has since grown well beyond ₹12,000 Cr.</p>
<div class="grid">
 <div class="card"><h2>DMF (mining fund) — top districts</h2><div class="tbl" id="govtdmf"></div></div>
 <div class="card"><h2>Major schemes &amp; outlays</h2><div class="tbl" id="govtsch"></div></div>
</div>
<div class="card cardpad" style="margin-top:14px"><b>On CSR currency &amp; “live scraping”:</b> <span class="mini">The dashboard's CSR layer already holds the latest <b>complete</b> year (FY2023-24) from the MCA National CSR Portal (csr.gov.in). MCA publishes company/state/district/sector-wise data for the last 5 years, but there is <b>no open API</b> for reliable client-side (in-browser) scraping, and FY2024-25 district aggregates are not yet fully published. A refresh means a one-time manual pull from csr.gov.in / data.gov.in and re-running the build — I can wire that when the new year lands.</span></div>

<div class="section-title">Sources</div>
<p class="section-sub">Everything above is traceable. Source spreadsheets are the spine; ✳ indicative orgs, funders and government figures are compiled from the public links below and kept out of the health scores.</p>
<div class="card cardpad srcs">
 <div class="srcgrid">
  <div><div class="srch">Source files (provided)</div>
   <ul><li>Partners — Geography &amp; Thematic focus</li><li>TRI Geographic Presence (Jul 2026)</li><li>Common Ground — block list</li><li>SOTH places list</li></ul></div>
  <div><div class="srch">Boundaries &amp; CSR</div>
   <ul><li><a href="https://github.com/udit-001/india-maps-data" target="_blank" rel="noopener">udit-001/india-maps-data</a> — district boundaries (2011 census)</li><li><a href="https://www.csr.gov.in/" target="_blank" rel="noopener">MCA National CSR Portal</a> — district CSR</li><li><a href="https://www.data.gov.in/resource/development-sector-wise-details-corporate-social-responsibility-csr-expenditure-jharkhand" target="_blank" rel="noopener">data.gov.in</a> — Jharkhand CSR</li></ul></div>
  <div><div class="srch">Implementing orgs ✳</div>
   <ul><li><a href="https://www.pradan.net/" target="_blank" rel="noopener">PRADAN</a></li><li><a href="https://cinicell.org/" target="_blank" rel="noopener">CInI (Tata Trusts)</a></li><li><a href="https://www.vikasbharti.in/" target="_blank" rel="noopener">Vikas Bharti Bishunpur</a></li><li><a href="https://ceedindia.org/" target="_blank" rel="noopener">CEED</a></li><li><a href="https://www.jslps.org/" target="_blank" rel="noopener">JSLPS</a></li><li><a href="https://www.tatasteelfoundation.org/" target="_blank" rel="noopener">Tata Steel Foundation</a></li></ul></div>
  <div><div class="srch">Funders ✳</div>
   <ul><li><a href="https://www.brlf.in/cso-partners/" target="_blank" rel="noopener">BRLF</a></li><li><a href="https://azimpremjifoundation.org/who-we-are/where-we-work/jharkhand/" target="_blank" rel="noopener">Azim Premji Foundation (Jharkhand)</a> · <a href="https://phia.org.in/partner/azim-premji-foundation/" target="_blank" rel="noopener">PHIA partner page</a></li><li><a href="https://rainmatter.org/" target="_blank" rel="noopener">Rainmatter Foundation</a></li><li><a href="https://www.edelgive.org/" target="_blank" rel="noopener">EdelGive GROW Fund</a></li><li><a href="https://rohininilekaniphilanthropies.org/" target="_blank" rel="noopener">Rohini Nilekani Philanthropies</a></li><li><a href="https://www.tatatrusts.org/" target="_blank" rel="noopener">Tata Trusts</a></li></ul></div>
  <div><div class="srch">Government spend</div>
   <ul><li><a href="https://www.cseindia.org/district-mineral-foundation-dmf-in-jharkhand-is-failing-to-fulfil-its-objectives-cse-8888" target="_blank" rel="noopener">CSE</a> — DMF Jharkhand (district split)</li><li><a href="https://csep.org/discussion-note/district-mineral-foundation-funds-evaluating-the-performance/" target="_blank" rel="noopener">CSEP</a> — DMF performance</li><li><a href="https://theindianawaaz.com/jharkhand-budget-2026-27-%E2%82%B91-58-lakh-crore-abua-dishom-outlay-focuses-on-social-justice-infrastructure/" target="_blank" rel="noopener">Jharkhand Budget 2026-27</a> — schemes &amp; outlays</li></ul></div>
 </div>
</div>

<div class="foot" id="foot"></div>
</div>

<script>
const MODEL=__MODEL__;
const GEO=__GEO__;
const D=MODEL.districts, CANON=MODEL.canon, THEMES=MODEL.themes, YEARS=MODEL.years, PARTNERS=MODEL.partners;
const Y0=YEARS[0];
/* ---- WIDER ECOSYSTEM: external to the source files, compiled from public sources (INDICATIVE) ---- */
const EXT_IMPL=[
 {name:'PRADAN',districts:['Khunti','Gumla','Godda','Hazaribagh','Dumka','Koderma','Ranchi','West Singhbhum'],focus:'Livelihoods · Women/SHGs · NRM',src:'https://www.pradan.net/'},
 {name:'CInI (Tata Trusts)',districts:['West Singhbhum','East Singhbhum','Saraikela-Kharsawan','Khunti','Gumla','Simdega'],focus:'Agriculture · forest livelihoods · water',src:'https://cinicell.org/'},
 {name:'Vikas Bharti Bishunpur',districts:['Gumla'],focus:'NRM · health · education · KVK (HQ Gumla, projects statewide)',src:'https://www.vikasbharti.in/'},
 {name:'Ekjut',districts:['West Singhbhum','Saraikela-Kharsawan'],focus:'Maternal & newborn health (participatory learning)',src:''},
 {name:'CINI (Child In Need Institute)',districts:['Ranchi'],focus:'Child health & nutrition (+ statewide)',src:''},
 {name:'NEEDS',districts:['Deoghar','Dumka','Godda'],focus:'WASH · livelihoods (Santhal Pargana)',src:''},
 {name:'CEED (Centre for Environment & Energy Dev.)',districts:['Ranchi','Dhanbad','Bokaro'],focus:'Climate · clean energy · air quality — technical partner to Govt of Jharkhand',src:'https://ceedindia.org/'},
 {name:'Lok Prerna',districts:['Deoghar','Dumka'],focus:'WASH · NRM · livelihoods · women & child rights',src:''},
 {name:'Tata Steel Foundation',districts:['East Singhbhum','West Singhbhum','Saraikela-Kharsawan'],focus:'Tribal development — 4,500 villages (JH + Odisha)',src:'https://www.tatasteelfoundation.org/'},
 {name:'JSLPS (Govt of Jharkhand)',districts:[],focus:'SHG / livelihoods mission — all 24 districts',src:'https://www.jslps.org/'}
];
const EXT_FUND=[
 {name:'BRLF (Bharat Rural Livelihoods Foundation)',orgs:[],supports:'57 tribal/PVTG-district CSOs across 10 states — JH grantee names not public',amt:'₹113 Cr',amtn:'CSO grants to Mar-2021',src:'https://www.brlf.in/cso-partners/'},
 {name:'Tata Trusts',orgs:['CInI (Tata Trusts)'],supports:'CInI (associate org) — Lakhpati Kisan, Kolhan',amt:'n/a',amtn:'JH share not public',src:'https://www.tatatrusts.org/'},
 {name:'HDFC Bank (Parivartan)',orgs:['CInI (Tata Trusts)'],supports:'CInI — co-funds Lakhpati Kisan',amt:'₹1,068 Cr',amtn:'total CSR FY2024-25, all-India',src:'https://v.hdfc.bank.in/csr/index.html'},
 {name:'Azim Premji Foundation',orgs:['PHIA'],supports:'PHIA + own field ops (Gumla, Ranchi, Simdega); early-stage CSO grants',amt:'₹1,774 Cr',amtn:'annual giving, all-India (Hurun 2023)',src:'https://phia.org.in/partner/azim-premji-foundation/'},
 {name:'Rainmatter Foundation',orgs:[],supports:'Source-file partners on this board (ecosystem funder)',amt:'~₹1,660 Cr',amtn:'$200M committed to climate, all-India',src:'https://rainmatter.org/'},
 {name:'Tata Steel Foundation',orgs:[],supports:'Direct ops — 4,500 villages across Kolhan (+ local partners)',amt:'₹511 Cr',amtn:'CSR FY2023, Jharkhand + Odisha',src:'https://www.tatasteelfoundation.org/'},
 {name:'EdelGive Foundation (GROW Fund)',orgs:[],supports:'GROW-cohort Jharkhand NGOs (names not individually public)',amt:'₹100 Cr',amtn:'GROW Fund size, 100 NGOs pan-India',src:'https://www.edelgive.org/'},
 {name:'Rohini Nilekani Philanthropies',orgs:[],supports:'Jharkhand NGOs via EdelGive GROW; direct grants',amt:'₹204 Cr',amtn:'2024 giving, all-India',src:'https://rohininilekaniphilanthropies.org/'},
 {name:'A.T.E. Chandra Foundation',orgs:[],supports:'Jharkhand NGOs via EdelGive GROW',amt:'n/a',amtn:'',src:''},
 {name:'Bill & Melinda Gates Foundation',orgs:[],supports:'Health/nutrition via EdelGive GROW & partners',amt:'global',amtn:'India programme; JH share n/a',src:''},
 {name:'Corporate CSR (see CSR lens)',orgs:[],supports:'Direct district CSR — Adani (Godda) · CCL/Coal India (coal belt) · NTPC · SBI',amt:'see CSR',amtn:'district CSR in the map lens',src:''}
];
/* ---- GOVERNMENT SPEND & ALLOCATION (indicative) ---- */
const GOVT_DMF={'Dhanbad':715,'Chatra':425.8,'West Singhbhum':424,'Ramgarh':414,'Bokaro':265,'Godda':200}; // ₹Cr cumulative to Mar-2018, CSE
const maxDMF=Math.max(...Object.values(GOVT_DMF));
const GOVT_SCHEMES=[
 {name:'Maiyan Samman Yojana',outlay:'₹13,363 Cr',yr:'2025-26',focus:'Women DBT — ₹2,500/mo to ~50 lakh women',foot:'Statewide'},
 {name:'Abua Awas Yojana',outlay:'₹16,320 Cr',yr:'3 phases',focus:'Housing — 8 lakh pucca houses',foot:'₹4,100 Cr/yr proposed'},
 {name:'MGNREGA (state 60:40 share)',outlay:'₹5,640 Cr',yr:'annual',focus:'Wage employment · NRM assets',foot:'Statewide'},
 {name:'PM-JANMAN',outlay:'₹1,360 Cr+',yr:'central',focus:'PVTG habitations — housing, roads, water',foot:'PVTG-heavy districts'},
 {name:'State Budget “Abua Dishom”',outlay:'₹1.58 lakh Cr',yr:'FY2026-27',focus:'Social justice + infrastructure',foot:'Total state outlay'}
];
const extCount={}; CANON.forEach(d=>extCount[d]=0);
EXT_IMPL.forEach(o=>o.districts.forEach(d=>{if(d in extCount)extCount[d]++;}));
const maxExt=Math.max(...Object.values(extCount),1);
const extByDist=d=>EXT_IMPL.filter(o=>o.districts.includes(d)).map(o=>o.name);
const fmtCr=v=>'₹'+(v/1e7).toFixed(v/1e7<10?1:0)+' Cr';
const el=(t,c,h)=>{const e=document.createElement(t); if(c)e.className=c; if(h!=null)e.innerHTML=h; return e;};

/* ---------- theme frequency (for matrix shading + dominant) ---------- */
const themeFreq={}; THEMES.forEach(t=>themeFreq[t]=0);
PARTNERS.forEach(p=>p.themes.forEach(t=>{if(t in themeFreq)themeFreq[t]++;}));
const maxTF=Math.max(...Object.values(themeFreq),1);

/* ---------- effective data (toggle: include ✳ indicative orgs in scoring) ---------- */
let INCLUDE_EXT=false;
function extThemesOf(focus){const t=focus.toLowerCase();const s=new Set();const has=(...w)=>w.some(x=>t.includes(x));
 if(has('education','educat'))s.add('Education');
 if(has('health','nutrition'))s.add('Health & Nutrition');
 if(has('women','gender','shg'))s.add('Women & Gender');
 if(has('climate'))s.add('Climate Action');
 if(has('livelihood','rural dev','community'))s.add('Livelihoods & Rural Dev');
 if(has('agricultur','farming','horticultur'))s.add('Agriculture');
 if(has('nrm','natural resource','watershed','forest','water bod'))s.add('Natural Resource Mgmt');
 if(has('wash','sanitation','drinking water'))s.add('Water & Sanitation');
 if(has('governance','citizenship'))s.add('Governance');
 if(has('skill','vocational'))s.add('Skill Development');
 if(has('energy'))s.add('Clean Energy');
 if(has('child'))s.add('Child Protection');
 return [...s];}
function effPList(d){if(!INCLUDE_EXT)return D[d].partners.slice();const s=new Set(D[d].partners);extByDist(d).forEach(n=>s.add(n));return [...s];}
function effP(d){return effPList(d).length;}
function effTList(d){if(!INCLUDE_EXT)return D[d].themes.slice();const s=new Set(D[d].themes);EXT_IMPL.forEach(o=>{if(o.districts.includes(d))extThemesOf(o.focus).forEach(t=>s.add(t));});return [...s];}
function effT(d){return effTList(d).length;}
const coveredList=()=>CANON.filter(d=>effP(d)>0);
const whiteList=()=>CANON.filter(d=>effP(d)===0);
const csrTot=CANON.reduce((s,d)=>s+(D[d].csr[Y0]||0),0);

/* ---------- summary strip ---------- */
function renderStrip(){const strip=document.getElementById('strip'); strip.innerHTML='';
 const covered=coveredList().length, white=whiteList().length;
 const stats=[
  ['24','Districts'],
  [INCLUDE_EXT?(PARTNERS.length+EXT_IMPL.length):PARTNERS.length, INCLUDE_EXT?'Orgs (incl. ✳)':'Partners mapped'],
  [covered,'Districts covered'],
  [white,'Whitespace (0 orgs)','warn'],
  [CANON.filter(d=>D[d].aspirational).length,'Aspirational (TRI)'],
  [fmtCr(csrTot),'CSR '+Y0]
 ];
 stats.forEach(s=>{const c=el('div','stat'+(s[2]?' '+s[2]:'')); c.appendChild(el('div','n',s[0])); c.appendChild(el('div','l',s[1])); strip.appendChild(c);});
}

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
let maxP,maxCSR,maxT;
function refreshScales(){maxP=Math.max(1,...CANON.map(effP));maxCSR=Math.max(...CANON.map(d=>D[d].csr[Y0]||0));maxT=Math.max(1,...CANON.map(effT));}
refreshScales();
const lenses={
 partners:{label:'Partner density',fill:d=>seqColor(effP(d),maxP),
   legend:()=>gradLegend(INCLUDE_EXT?'# orgs (incl. ✳)':'# partners',maxP)},
 themes:{label:'Theme breadth',fill:d=>seqColor(effT(d),maxT),
   legend:()=>gradLegend('# themes',maxT)},
 csr:{label:'CSR spend '+Y0,fill:d=>seqColor(D[d].csr[Y0]||0,maxCSR),
   legend:()=>gradLegend('CSR (₹)',maxCSR,true)},
 dom:{label:'Dominant theme',fill:d=>{const t=domTheme(d);return t?themePalette[t]:'#f1f5fa';},
   legend:()=>themeLegend()},
 gap:{label:'Coverage gap',fill:d=>{const n=effP(d),a=D[d].aspirational;if(n===0&&a)return '#c2410c';
     if(n===0)return '#e79a6a'; if(a&&n<=1)return '#f0c088'; return '#cfe0d8';},
   legend:()=>gapLegend()},
 placehealth:{label:'Place health score',fill:d=>{const pal=['#c2410c','#e0762f','#e6b84d','#8bbf5a','#2b8a3e'];return pal[Math.min(4,Math.floor(placeScore(d)/20.0001))];},
   legend:()=>gradLegendC('Place health 0 → 100',['#c2410c','#e0762f','#e6b84d','#8bbf5a','#2b8a3e'],'weak → strong')},
 external:{label:'External orgs ✳',fill:d=>{const c=extCount[d];return c?['#f1f5fa','#e6ddc9','#d8c48f','#c79a4e','#b07a1f'][Math.min(c,4)]:'#f1f5fa';},
   legend:()=>gradLegendC('Other orgs present (indicative)',['#f4efe3','#e6ddc9','#d8c48f','#c79a4e','#b07a1f'],'0 → '+maxExt+'+')},
 dmf:{label:'DMF mining fund ✳',fill:d=>{const v=GOVT_DMF[d]||0;if(!v)return '#f2eef6';const t=v/maxDMF;const p=['#e7dcf0','#c9b0e0','#a97fce','#8a4fbf','#6b2fa0'];return p[Math.min(p.length-1,Math.floor(t*(p.length-1)+0.001))];},
   legend:()=>gradLegendC('DMF collected ₹Cr (to Mar-2018, CSE)',['#f2eef6','#c9b0e0','#a97fce','#8a4fbf','#6b2fa0'],'0 → ₹'+maxDMF+' Cr')}
};
function domTheme(d){const f={};PARTNERS.forEach(p=>{if(p.districts.includes(d))p.themes.forEach(t=>f[t]=(f[t]||0)+1);});
 let best=null,bv=0;for(const k in f)if(f[k]>bv){bv=f[k];best=k;}return best;}
let curLens='placehealth', selD=null;

/* legends */
function gradLegend(title,max,money){const w=el('div');w.appendChild(el('span','legtitle',title));
 const grad=el('div'); grad.style.cssText='display:flex;gap:0;border-radius:4px;overflow:hidden';
 seq.forEach(c=>{const b=el('div');b.style.cssText='width:24px;height:12px;background:'+c;grad.appendChild(b);});
 w.appendChild(grad);
 w.appendChild(el('span','',money?('0 → '+fmtCr(max)):('0 → '+max)));
 w.style.cssText='display:flex;align-items:center;gap:8px;flex-wrap:wrap';return w;}
function gradLegendC(title,cols,rng){const w=el('div');w.style.cssText='display:flex;align-items:center;gap:8px;flex-wrap:wrap';
 w.appendChild(el('span','legtitle',title));
 const grad=el('div'); grad.style.cssText='display:flex;gap:0;border-radius:4px;overflow:hidden';
 cols.forEach(c=>{const b=el('div');b.style.cssText='width:24px;height:12px;background:'+c;grad.appendChild(b);});
 w.appendChild(grad); w.appendChild(el('span','',rng)); return w;}
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
 tx.setAttribute('class','dlabel'); tx.dataset.base=name.replace('-Kharsawan','').replace(' Singhbhum','.S'); tx.textContent=tx.dataset.base;
 svg.appendChild(tx); labels[name]=tx;
});
mapbox.appendChild(svg);

/* tooltip */
const tip=el('div'); tip.style.cssText='position:fixed;pointer-events:none;background:#0f2440;color:#fff;padding:7px 10px;border-radius:8px;font-size:12px;box-shadow:0 6px 20px rgba(0,0,0,.25);z-index:99;display:none;max-width:230px';
document.body.appendChild(tip);
function showTip(ev,name){const v=D[name];
 tip.innerHTML='<b>'+name+'</b> · health '+placeScore(name)+'/100<br>'+effP(name)+' org'+(effP(name)!=1?'s':'')+' · '+effT(name)+' themes<br>CSR '+Y0+': '+fmtCr(v.csr[Y0]||0)+(v.aspirational?' · <span style="color:#f0a878">Aspirational</span>':'');
 tip.style.display='block'; tip.style.left=Math.min(ev.clientX+14,innerWidth-240)+'px'; tip.style.top=(ev.clientY+14)+'px';}
function hideTip(){tip.style.display='none';}

/* lens buttons */
const lensBox=document.getElementById('lens');
Object.entries(lenses).forEach(([k,v])=>{const b=el('button',k===curLens?'on':'',v.label);b.onclick=()=>{curLens=k;paint();};lensBox.appendChild(b);});
function paint(){
 [...lensBox.children].forEach(b=>b.classList.toggle('on',b.textContent===lenses[curLens].label));
 CANON.forEach(d=>{const f=lenses[curLens].fill(d); paths[d].setAttribute('fill',f);
   // label contrast + place-health score on map
   const dark=isDark(f); labels[d].classList.toggle('lite',dark);
   labels[d].textContent = curLens==='placehealth' ? labels[d].dataset.base+' · '+placeScore(d) : labels[d].dataset.base;});
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
 h+='<div class="kv"><div><div class="k">'+(INCLUDE_EXT?'Orgs':'Partners')+'</div><div class="v">'+effP(name)+'</div></div>'
   +'<div><div class="k">Themes</div><div class="v">'+effT(name)+'</div></div>'
   +'<div><div class="k">CSR '+Y0+'</div><div class="v">'+fmtCr(v.csr[Y0]||0)+'</div></div></div>';
 // place health readout
 const ps=placeScore(name), pb=BAND[band(ps)], pt=placeTag(name);
 h+='<div class="sec"><div class="t">Place health score</div>'
  +'<div style="display:flex;align-items:center;gap:11px">'
  +'<div style="font-size:28px;font-weight:800;color:'+pb[0]+';line-height:1">'+ps+'<span style="font-size:13px;opacity:.55;font-weight:600">/100</span></div>'
  +'<span class="tagp" style="background:'+pt.tb+';color:'+pt.tc+'">'+pt.tag+'</span>'
  +'<span class="mini">'+pb[2]+'</span></div>'
  +'<div class="track" style="height:8px;background:var(--line2);border-radius:5px;overflow:hidden;margin-top:7px"><i style="display:block;height:100%;width:'+Math.max(ps,2)+'%;background:'+pb[0]+'"></i></div>'
  +'<div class="mini" style="margin-top:5px">'+effP(name)+' org'+(effP(name)!=1?'s':'')+' (45%) · '+effT(name)+' themes (30%) · resilience (25%)'+(INCLUDE_EXT?' · incl. ✳ indicative':'')+'</div></div>';
 h+='<div class="sec"><div class="t">Partners here</div>';
 if(dp.length){h+='<ul class="plist">';dp.forEach(p=>{h+='<li><b>'+p.name+'</b><br><span class="mini">'+p.themes.join(' · ')+'</span></li>';});h+='</ul>';}
 else h+='<div class="mini">No mapped partner. '+(v.aspirational?'Aspirational district — whitespace.':'')+'</div>';
 h+='</div>';
 if(v.themes.length){h+='<div class="sec"><div class="t">Themes active</div><div class="chips">'+v.themes.map(t=>'<span class="chip" style="border-left:3px solid '+(themePalette[t]||'#ccc')+'">'+t+'</span>').join('')+'</div></div>';}
 if(v.tri&&v.tri.blocks){h+='<div class="sec"><div class="t">TRI community action lab</div><div class="blk">'+v.tri.blocks+'</div></div>';}
 if(v.cg&&v.cg.blocks){h+='<div class="sec"><div class="t">Common Ground blocks</div><div class="blk">'+v.cg.blocks+'</div></div>';}
 const ext=extByDist(name);
 if(ext.length){h+='<div class="sec"><div class="t">Other orgs — indicative ✳</div><div class="chips">'+ext.map(o=>'<span class="chip" style="border-left:3px solid #b07a1f">'+o+'</span>').join('')+'</div></div>';}
 if(GOVT_DMF[name]){h+='<div class="sec"><div class="t">DMF mining fund ✳</div><div class="blk">₹'+GOVT_DMF[name]+' Cr collected (cumulative to Mar-2018, CSE) — mining-affected-area fund.</div></div>';}
 // CSR sparkline
 const yr=[...YEARS].reverse(); const vals=yr.map(y=>v.csr[y]||0); const mx=Math.max(...vals,1);
 h+='<div class="sec"><div class="t">CSR spend trend (₹ Cr)</div><div class="spark">';
 vals.forEach(val=>{h+='<div class="bar" style="height:'+(val/mx*100)+'%" title="'+fmtCr(val)+'"></div>';});
 h+='</div><div class="sparkx"><span>'+yr[0].slice(0,4)+'</span><span>'+yr[yr.length-1].slice(2)+'</span></div></div>';
 body.innerHTML=h;
 body.scrollIntoView&&window.matchMedia('(max-width:960px)').matches&&body.scrollIntoView({behavior:'smooth',block:'nearest'});
}

/* ---------- matrix ---------- */
const THSHORT={'Health & Nutrition':'Health','Women & Gender':'Women','Climate Action':'Climate','Livelihoods & Rural Dev':'Livelihoods','Natural Resource Mgmt':'NRM','Water & Sanitation':'WASH','Skill Development':'Skills','Clean Energy':'Energy','Child Protection':'Child Ptn'};
const shortT=t=>THSHORT[t]||t;
function buildMatrix(){
 const src=PARTNERS.map(p=>({name:p.name,themes:p.themes,ext:false}));
 const ext=EXT_IMPL.map(o=>({name:o.name,themes:extThemesOf(o.focus),ext:true}));
 const rows=src.concat(ext).sort((a,b)=>b.themes.length-a.themes.length);
 // combined totals per theme (source + indicative)
 const totAll={},totSrc={}; THEMES.forEach(t=>{totSrc[t]=themeFreq[t];totAll[t]=0;});
 rows.forEach(r=>r.themes.forEach(t=>{if(t in totAll)totAll[t]++;}));
 let h='<table><thead><tr><th>Partner</th>';
 THEMES.forEach(t=>h+='<th class="rot" title="'+t+'"><div>'+shortT(t)+'</div></th>');
 h+='</tr></thead><tbody>';
 rows.forEach(p=>{h+='<tr'+(p.ext?' style="background:#fcfaf5"':'')+'><td class="name">'+p.name+(p.ext?' <span class="tag" style="background:#f4efe3;color:#b07a1f;border-color:#e6d9bf;font-size:9px;padding:0 5px">✳</span>':'')+'</td>';
   THEMES.forEach(t=>{const on=p.themes.includes(t);
     let bg='#fff',dot='';
     if(on){ if(p.ext){bg='rgba(176,122,31,0.55)';} else {const shade=0.35+0.65*(themeFreq[t]/maxTF);bg='rgba(13,110,140,'+shade.toFixed(2)+')';} dot='●'; }
     h+='<td><div class="cell" style="background:'+bg+'">'+dot+'</div></td>';});
   h+='</tr>';});
 // footer totals (source + indicative)
 h+='<tr><td class="name" style="font-weight:700">Orgs / theme <span class="mini">(src + ✳)</span></td>';
 THEMES.forEach(t=>h+='<td class="tot">'+totAll[t]+'<br><span class="mini" style="font-weight:400">'+totSrc[t]+'</span></td>');
 h+='</tbody></table>';
 document.getElementById('matrix').innerHTML=h;
}

/* ---------- partner directory ---------- */
let dirSort={k:'nd',asc:false};
function buildDir(){
 const box=document.getElementById('dirtbl');
 const cols=[['name','Partner'],['districts','Districts'],['themes','Themes / focus'],['nd','#Dist']];
 let rows=PARTNERS.map(p=>({name:p.name,districts:p.districts,themes:p.themes,themesN:p.themes.length,nd:p.districts.length,ext:false}));
 rows=rows.concat(EXT_IMPL.map(o=>{const segs=o.focus.split(' · ');return {name:o.name,districts:o.districts,focus:segs,themesN:segs.length,nd:o.districts.length,ext:true,src:o.src};}));
 rows.sort((a,b)=>{let k=dirSort.k,x,y;
   if(k==='themes'){x=a.themesN;y=b.themesN;} else if(k==='districts'){x=a.nd;y=b.nd;} else {x=a[k];y=b[k];}
   if(typeof x==='string')return dirSort.asc?x.localeCompare(y):y.localeCompare(x);return dirSort.asc?x-y:y-x;});
 let h='<table><thead><tr>';cols.forEach(c=>h+='<th data-k="'+c[0]+'">'+c[1]+(dirSort.k===c[0]?(dirSort.asc?' ▲':' ▼'):'')+'</th>');h+='</tr></thead><tbody>';
 rows.forEach(p=>{
   const badge=p.ext?' <span class="tag" style="background:#f4efe3;color:#b07a1f;border-color:#e6d9bf" title="Compiled from public sources, not the source spreadsheets">✳ indicative</span>'+(p.src?' <a class="mini" href="'+p.src+'" target="_blank" rel="noopener">↗</a>':''):'';
   const dcell=p.districts.length?p.districts.map(d=>'<span class="tag pill" data-d="'+d+'">'+d.replace('-Kharsawan','-K.')+'</span>').join(''):'<span class="tag">Statewide</span>';
   const tcell=p.ext?p.focus.map(t=>'<span class="tag" style="border-left:3px solid #b07a1f">'+t+'</span>').join('')
                    :p.themes.map(t=>'<span class="tag" style="border-left:3px solid '+(themePalette[t]||'#ccc')+'">'+t+'</span>').join('');
   h+='<tr'+(p.ext?' style="background:#fcfaf5"':'')+'><td><b>'+p.name+'</b>'+badge+'</td><td>'+dcell+'</td><td>'+tcell+'</td><td class="num">'+p.nd+'</td></tr>';});
 h+='</tbody></table>'; box.innerHTML=h;
 box.querySelectorAll('th').forEach(th=>th.onclick=()=>{const k=th.dataset.k;dirSort.asc=dirSort.k===k?!dirSort.asc:false;dirSort.k=k;buildDir();});
 box.querySelectorAll('.pill').forEach(s=>s.onclick=()=>{selectDist(s.dataset.d);document.getElementById('mapbox').scrollIntoView({behavior:'smooth',block:'center'});});
}

/* ---------- district table ---------- */
let disSort={k:'partners',asc:false};
function buildDisTbl(){
 const box=document.getElementById('distbl');
 let rows=CANON.map(d=>({d,partners:effP(d),themes:effT(d),
   asp:D[d].aspirational?1:0,tri:D[d].tri?1:0,csr:D[d].csr[Y0]||0,plist:effPList(d)}));
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

function updateFoot(){const wl=whiteList();document.getElementById('foot').innerHTML='Fully self-contained (offline) · '+(INCLUDE_EXT?(PARTNERS.length+EXT_IMPL.length)+' orgs (incl. ✳ indicative)':PARTNERS.length+' source-file partners')+' across '+coveredList().length+'/24 districts · Whitespace: <b>'+(wl.length?wl.join(', '):'none')+'</b>. Anchors: '+MODEL.anchors.map(a=>a.name).join(', ')+'. Scoring '+(INCLUDE_EXT?'<b>includes</b>':'<b>excludes</b>')+' ✳ indicative orgs.<br>MIT licensed · source &amp; issues: <a href="https://github.com/Ashwask/jharkhand-landscape" target="_blank" rel="noopener">github.com/Ashwask/jharkhand-landscape</a>';}

/* ---------- ecosystem + place health ---------- */
const BAND={strong:['#2b8a3e','#e7f3ea','Strong'],mod:['#b45309','#fdf0e2','Moderate'],weak:['#c2410c','#fdece3','Weak']};
function band(s){return s>=75?'strong':s>=50?'mod':'weak';}
function pearson(xs,ys){const n=xs.length,mx=xs.reduce((a,b)=>a+b,0)/n,my=ys.reduce((a,b)=>a+b,0)/n;
 let c=0,sx=0,sy=0;for(let i=0;i<n;i++){c+=(xs[i]-mx)*(ys[i]-my);sx+=(xs[i]-mx)**2;sy+=(ys[i]-my)**2;}
 return (sx&&sy)?c/Math.sqrt(sx*sy):0;}

function buildHealth(){
 const cov=coveredList();
 const asp=CANON.filter(d=>D[d].aspirational);
 const aspCov=asp.filter(d=>effP(d)>0);
 const single=CANON.filter(d=>effP(d)===1);
 const wht=whiteList();
 const tf={};THEMES.forEach(t=>tf[t]=0);PARTNERS.forEach(p=>p.themes.forEach(t=>{if(t in tf)tf[t]++;}));
 if(INCLUDE_EXT)EXT_IMPL.forEach(o=>extThemesOf(o.focus).forEach(t=>{if(t in tf)tf[t]++;}));
 const fragile=THEMES.filter(t=>tf[t]>0&&tf[t]<=2);
 const hubs=CANON.filter(d=>effP(d)>=3);
 const avgP=cov.reduce((s,d)=>s+effP(d),0)/cov.length;
 const r=pearson(CANON.map(d=>D[d].csr[Y0]||0),CANON.map(effP));
 const csrCov=CANON.reduce((s,d)=>s+(effP(d)?(D[d].csr[Y0]||0):0),0)/csrTot*100;
 const lbl=INCLUDE_EXT?'org':'partner';
 const dims=[
  {n:'Geographic coverage',v:cov.length+'/24',s:cov.length/24*100,d:Math.round(cov.length/24*100)+'% of districts have ≥1 '+lbl+'.'},
  {n:'Aspirational reach',v:aspCov.length+'/'+asp.length,s:aspCov.length/asp.length*100,d:(asp.length-aspCov.length)+' priority districts still unserved: '+(asp.filter(d=>!effP(d)).join(', ')||'none')+'.'},
  {n:'Resilience',v:(24-wht.length-single.length)+'/24',s:(24-wht.length-single.length)/24*100,d:single.length+' single-'+lbl+' + '+wht.length+' zero-'+lbl+' districts = key-person risk.'},
  {n:'Thematic balance',v:(THEMES.length-fragile.length)+'/'+THEMES.length,s:(THEMES.length-fragile.length)/THEMES.length*100,d:'Thin themes (≤2 '+lbl+'s): '+(fragile.join(', ')||'none')+'.'},
  {n:'Network depth',v:hubs.length+' hubs',s:hubs.length/24*100,d:hubs.length+' districts with ≥3 '+lbl+'s; avg '+avgP.toFixed(1)+' where present.'},
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

function placeScore(d){const p=effP(d),t=effT(d);
 const sp=Math.min(p/3,1)*45, st=Math.min(t/10,1)*30, sr=(p>=2?1:p===1?.4:0)*25;
 return Math.round(sp+st+sr);}
function placeTag(d){const p=effP(d),s=placeScore(d),asp=D[d].aspirational;
 if(p===0&&asp)return{tag:'Whitespace',tc:'#c2410c',tb:'#fdece3',need:0};
 if(p===0)return{tag:'Uncovered',tc:'#b45309',tb:'#fdf0e2',need:1};
 if(asp&&s<55)return{tag:'Priority',tc:'#b45309',tb:'#fdf0e2',need:2};
 if(p===1)return{tag:'Fragile',tc:'#b45309',tb:'#fdf0e2',need:3};
 return{tag:'Served',tc:'#2b8a3e',tb:'#e7f3ea',need:4};}
function buildPlaceHealth(){
 const rows=CANON.map(d=>{const s=placeScore(d),asp=D[d].aspirational,pt=placeTag(d);
  return {d,s,asp,tag:pt.tag,tc:pt.tc,tb:pt.tb,need:pt.need};});
 rows.sort((a,b)=>a.need-b.need||a.s-b.s);
 document.getElementById('placehealth').innerHTML=rows.map(r=>{const bc=BAND[band(r.s)][0];
  return '<div class="phrow"><span class="pn" data-d="'+r.d+'">'
   +(r.asp?'<span class="dot" style="background:#c2410c" title="Aspirational"></span>':'<span class="dot" style="background:#cdd7e6"></span>')+r.d+'</span>'
   +'<span class="track"><i style="width:'+Math.max(r.s,2)+'%;background:'+bc+'"></i></span>'
   +'<span class="right"><span class="tagp" style="background:'+r.tb+';color:'+r.tc+'">'+r.tag+'</span><span class="sc">'+r.s+'</span></span></div>';}).join('');
 document.querySelectorAll('#placehealth .pn').forEach(s=>s.onclick=()=>{selectDist(s.dataset.d);document.getElementById('mapbox').scrollIntoView({behavior:'smooth',block:'center'});});
}

function buildExt(){
 const srcLink=s=>s?'<a href="'+s+'" target="_blank" rel="noopener">source ↗</a>':'<span class="mini">public sources</span>';
 let f='<table><thead><tr><th>Funder</th><th>Supports in Jharkhand</th><th>Ref</th></tr></thead><tbody>';
 EXT_FUND.forEach(o=>{
   const orgTags=(o.orgs&&o.orgs.length)?o.orgs.map(n=>'<span class="tag" style="border-left:3px solid #b07a1f">'+n+'</span>').join(' '):'';
   f+='<tr><td><b>'+o.name+'</b></td>'
    +'<td>'+orgTags+(orgTags?'<br>':'')+'<span class="mini">'+o.supports+'</span></td>'
    +'<td class="mini">'+srcLink(o.src)+'</td></tr>';});
 f+='</tbody></table>'; document.getElementById('extfund').innerHTML=f;
}

function buildGovt(){
 const dmf=Object.entries(GOVT_DMF).sort((a,b)=>b[1]-a[1]);
 let h='<table><thead><tr><th>District</th><th class="num">DMF ₹Cr</th><th>Share of state DMF</th></tr></thead><tbody>';
 const tot=2696;
 dmf.forEach(([d,v])=>{h+='<tr><td><span class="dot" style="background:#8a4fbf"></span><b class="pill" data-d="'+d+'">'+d+'</b></td><td class="num">₹'+v+'</td><td><span class="track" style="display:inline-block;width:60%;height:8px;background:#efe8f6;border-radius:5px;overflow:hidden;vertical-align:middle"><i style="display:block;height:100%;width:'+(v/maxDMF*100)+'%;background:#8a4fbf"></i></span> <span class="mini">'+(v/tot*100).toFixed(0)+'%</span></td></tr>';});
 h+='</tbody></table>'; const box=document.getElementById('govtdmf'); box.innerHTML=h;
 box.querySelectorAll('.pill').forEach(s=>s.onclick=()=>{selectDist(s.dataset.d);document.getElementById('mapbox').scrollIntoView({behavior:'smooth',block:'center'});});
 let s='<table><thead><tr><th>Scheme</th><th>Outlay</th><th>Focus</th></tr></thead><tbody>';
 GOVT_SCHEMES.forEach(o=>{s+='<tr><td><b>'+o.name+'</b><br><span class="mini">'+o.foot+'</span></td><td class="mini"><b>'+o.outlay+'</b><br>'+o.yr+'</td><td class="mini">'+o.focus+'</td></tr>';});
 s+='</tbody></table>'; document.getElementById('govtsch').innerHTML=s;
}

/* toggle-dependent surfaces */
function renderScored(){refreshScales(); renderStrip(); paint(); buildHealth(); buildPlaceHealth(); buildDisTbl(); updateFoot(); if(selD)selectDist(selD);}
document.getElementById('extToggle').addEventListener('change',e=>{INCLUDE_EXT=e.target.checked; renderScored();});

/* initial render */
renderStrip(); paint(); buildHealth(); buildMatrix(); buildPlaceHealth(); buildDir(); buildDisTbl(); updateFoot(); buildExt(); buildGovt();
/* collapsible sections (directory / place health / district table) */
document.getElementById('dircount').textContent='('+(PARTNERS.length+EXT_IMPL.length)+' organisations)';
document.querySelectorAll('.collapser[data-wrap]').forEach(tg=>{const wrap=document.getElementById(tg.dataset.wrap);
 tg.addEventListener('click',()=>{const hidden=wrap.classList.toggle('collapsed'); tg.classList.toggle('closed',hidden);});});

/* deep-link: #ext opens with indicative scoring on; #lens=<key> selects a map lens */
if(location.hash.toLowerCase().includes('ext')){const t=document.getElementById('extToggle');t.checked=true;INCLUDE_EXT=true;renderScored();}
const hl=location.hash.match(/lens=(\w+)/); if(hl&&lenses[hl[1]]){curLens=hl[1];paint();}
</script></body></html>'''

HTML = HTML.replace('__MODEL__', MODEL).replace('__GEO__', GEO)
open("index.html","w").write(HTML)
print("wrote index.html", len(HTML), "bytes")
