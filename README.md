# Jharkhand Landscape — Who Does What Where

An interactive, fully self-contained (offline, no keys, no CDN) sense-making view of the
development-partner ecosystem in Jharkhand: **partners × districts × themes**, with TRI
presence, Common Ground blocks, block/GP-level coverage, CSR flow, external organisations,
funders and government spend — plus **Ecosystem Health** and **Place Health** scorecards.

**Live:** https://ashwask.github.io/jharkhand-landscape/

The whole app is a single `index.html` (~200 KB) with the data and the 24-district GeoJSON
inlined — open it locally or host it anywhere static. `build.py` regenerates it from
`model.json` + `jh_districts.geojson`; `build_blocks.py` regenerates the block/GP coverage
data in `model.json` from the source spreadsheets.

## What's inside

**Map — 9 lenses** (inline-SVG choropleth, no map tiles):
Partner density · Theme breadth · CSR spend · Dominant theme · Coverage gap ·
Place health score · External orgs ✳ · DMF mining fund ✳ · **Block presence (beta)**.
Click any district for a detail panel (partners, themes, block/GP coverage, other orgs,
DMF, place-health score + breakdown, 10-year CSR trend). Hover for a quick readout.

**Block coverage (beta)** — an optional per-district view of which blocks/GPs have known
partner presence, plus the villages where recorded. **Count-only and deliberately partial:**
block-level presence is known for **Common Ground and TRI only** (39 block/GPs across 13
districts) — the 12 landscape partners are mapped at district level, so this is *known
presence, not total coverage*. There is no "X of Y" ratio because the source files carry no
per-district block/GP totals (denominator); drop in an LGD/Census block-total sheet to
upgrade it to ratios.

**Scorecards**
- **Ecosystem Health index** — composite of coverage, aspirational reach, resilience,
  thematic balance, network depth and resource alignment.
- **Place Health** — every district scored 0–100 (partner presence 45% · theme breadth 30% ·
  resilience 25%), ranked neediest-first, tagged Whitespace / Priority / Fragile / Served.

**Tables**
- **Partner × Theme matrix** — source partners (teal) + ✳ indicative orgs (gold, themes
  keyword-mapped from focus).
- **Partner directory** (collapsible, sortable) — source-file partners + ✳ indicative orgs.
- **District coverage table** — partners, themes, aspirational, TRI, CSR.
- **Funders & philanthropies** — funder → implementing-org links ("Supports in Jharkhand").
- **Government spend & allocation** — DMF (district-wise) + major state/central schemes.

**Toggle** — *Include ✳ indicative orgs in scoring* recomputes the strip, health index,
place health, map lenses and tables on the wider org set.

**Deep-links** — `#ext` opens with indicative scoring on · `#lens=<key>` opens on a given
map lens (e.g. `#lens=placehealth`).

## Provenance & honesty

- **Source spreadsheets** (Partners geography/thematic, TRI Geographic Presence Jul-2026,
  Common Ground blocks, SOTH places) are the spine and drive the health scores.
- **✳ indicative** organisations, funders and government figures are compiled from public
  sources (linked in the in-app **Sources** section) and are **kept out of the health
  scores** unless the toggle is on. District attributions are approximate — treat as leads.
- **Block/GP coverage** reflects only the two sources with block-level resolution (Common
  Ground, TRI); absence of blocks for a district means "not recorded at block level", not
  "no partners". It is a count of known presence, never a coverage ratio.
- Funder ₹ figures, where shown, are **organisation-level** (not Jharkhand-specific).
- The DMF district split is cumulative to Mar-2018 (CSE); the state total has since grown
  well beyond ₹12,000 Cr.
- District labels ("whitespace", "priority") describe **partner-coverage gaps**, not
  judgements of the districts or the partners.

## Data sources

Partner geography/thematic sheets · TRI Geographic Presence (Jul 2026) · Common Ground block
list · SOTH places list · [MCA National CSR Portal](https://www.csr.gov.in/) (district CSR) ·
[CSE](https://www.cseindia.org/) & [CSEP](https://csep.org/) (DMF) · Jharkhand state budget ·
org & funder websites (PRADAN, CInI, Vikas Bharti, CEED, JSLPS, Tata Steel Foundation, BRLF,
Azim Premji Foundation, PHIA, Rainmatter, EdelGive, Rohini Nilekani, Tata Trusts).

District boundaries from [udit-001/india-maps-data](https://github.com/udit-001/india-maps-data)
(2011 census; public government boundary data, curated by the upstream repo).

## Build / regenerate

```bash
python3 build_blocks.py   # (optional) re-parse the source .xlsx → block/GP coverage in model.json
python3 build.py          # reads model.json + jh_districts.geojson → writes index.html
```

`build.py` needs only Python 3 (stdlib) and the output is dependency-free. `build_blocks.py`
additionally needs `openpyxl` and the source spreadsheets present, and only needs re-running
when the block/GP source data changes.

## License

Code and compiled dataset: [MIT](LICENSE) © 2026 Ashwin Kulkarni.
Underlying source data remains under the terms of the respective providers linked above.
Contributions and corrections (especially district attributions and funder→org links)
welcome via issue or PR.
