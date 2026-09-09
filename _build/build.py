#!/usr/bin/env python3
"""Static site generator for kentontechnical.co.uk (staging for kentons.biz)."""
import json, os, re, shutil, datetime, math, html
from jinja2 import Environment, FileSystemLoader
import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
STAGING = os.environ.get('STAGING', '1') == '1'
SITE = dict(name='Kenton Technical Products', url='https://kentontechnical.co.uk')
YEAR = datetime.date.today().year
BUILD_DATE = datetime.date.today().isoformat()
PHONE = '+441179634579'

env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'templates')), autoescape=False, trim_blocks=True, lstrip_blocks=True)
products = json.load(open(os.path.join(ROOT, 'data/products.json')))
imgmap = json.load(open(os.path.join(ROOT, 'data/images.json')))
pages = []  # (path, lastmod, priority)

def img(u):
    return imgmap.get(u) or '/assets/img/istock-172765798.webp'

def fmt(n):
    return ('%g' % n)

def parse_code(code, hole):
    """R5 T8 -> size 5, pitch 8 ; C10 U15 ; LR5x20"""
    c = code.replace('×', 'x')
    if hole == 'slotted':
        m = re.match(r'LR([\d.]+)x([\d.]+)', c)
        w, l = float(m.group(1)), float(m.group(2))
        return dict(size=w, length=l, pitch=None)
    m = re.match(r'([RC])([\d.]+)\s+([TU])([\d.]+)', c)
    return dict(size=float(m.group(2)), pitch=float(m.group(4)), length=None)

def hole_desc(p):
    d = p['dims']
    if p['hole'] == 'slotted':
        return f"{fmt(d['size'])} × {fmt(d['length'])}mm slot"
    return f"{fmt(d['size'])}mm {'square' if p['hole']=='square' else 'round'}"

def pitch_desc(p):
    d = p['dims']
    if p['hole'] == 'slotted':
        return 'staggered'
    return f"{fmt(d['pitch'])}mm {'staggered' if p['hole']=='round-staggered' else 'square'}"

def pattern_svg(p, size=200):
    """Simple SVG diagram of the pattern."""
    d = p['dims']; h = p['hole']
    s = size; parts = [f'<svg class="pattern-svg" viewBox="0 0 {s} {s}" width="{s}" height="{s}" role="img" aria-label="Diagram of {p["code"]} pattern"><rect width="{s}" height="{s}" fill="#d8dce2"/>']
    if h == 'slotted':
        w, l = d['size'], d['length']; px = l + w; py = w * 2
        scale = s / (px * 3.2)
        y = 0; row = 0
        while y < s + py * scale:
            x = -(px * scale / 2 if row % 2 else 0)
            while x < s + px * scale:
                parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{l*scale:.1f}" height="{w*scale:.1f}" rx="{w*scale/2:.1f}" fill="#fff"/>')
                x += px * scale
            y += py * scale; row += 1
    else:
        size_mm, pitch = d['size'], d['pitch']
        scale = s / (pitch * 5)
        r = size_mm * scale / 2
        if h == 'round-staggered':
            dy = pitch * scale * math.sqrt(3) / 2
            y = 0; row = 0
            while y <= s + r:
                x = pitch * scale / 2 if row % 2 else 0
                while x <= s + r:
                    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#fff"/>')
                    x += pitch * scale
                y += dy; row += 1
        else:
            y = pitch * scale / 2
            while y <= s + r:
                x = pitch * scale / 2
                while x <= s + r:
                    if h == 'square':
                        parts.append(f'<rect x="{x-r:.1f}" y="{y-r:.1f}" width="{2*r:.1f}" height="{2*r:.1f}" fill="#fff"/>')
                    else:
                        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#fff"/>')
                    x += pitch * scale
                y += pitch * scale
    parts.append('</svg>')
    return ''.join(parts)

def thick_num(t):
    m = re.search(r'([\d.]+)\s*mm', t)
    return float(m.group(1)) if m else None

# ---------- enrich perforated products ----------
perf = [p for p in products if p['family'] == 'perforated']
for p in perf:
    mat = C.MATERIALS[p['material']]
    hole = C.HOLES[p['hole']]
    p['dims'] = parse_code(p['code'], p['hole'])
    p['oa_num'] = float(p['open_area'].rstrip('%'))
    p['material_short'] = mat['short']
    p['material_lc'] = p['material'].lower() if p['material'] != 'Pre-Galvanised Steel' else 'pre-galvanised steel'
    p['hole_name'] = hole['name']; p['hole_name_lc'] = hole['name'].lower().replace(',', '')
    p['hole_desc'] = hole_desc(p); p['pitch_desc'] = pitch_desc(p)
    p['image_local'] = img(p['image'])
    p['sizes'] = sorted({a['size'] for a in p['availability']}, key=lambda s: -1 * float(re.match(r'([\d.]+)', s).group(1)) if re.match(r'([\d.]+)', s) else 0)
    p['thick_list'] = sorted({a['thickness'] for a in p['availability']}, key=lambda t: thick_num(t) or 0)
    p['in_stock'] = any('stock' in a['status'].lower() for a in p['availability'])
    cs = p['code'].lower().replace(' ', '-').replace('.', '-').replace('×', 'x')
    p['path'] = f"/perforated-metal/{mat['slug']}/{cs}-{fmt(p['dims']['size']).replace('.', '-')}mm-{'slot' if p['hole']=='slotted' else 'hole'}{('-' + fmt(p['dims']['pitch']).replace('.', '-') + 'mm-pitch') if p['dims']['pitch'] else ''}/"
    p['material_path'] = f"/perforated-metal/{mat['slug']}/"
    p['svg'] = pattern_svg(p)
    # bar width
    if p['dims']['pitch']:
        p['bar'] = p['dims']['pitch'] - p['dims']['size']
    # weight per m2 per thickness
    p['weights'] = {t: round(thick_num(t) * mat['density'] * (1 - p['oa_num'] / 100), 2) for t in p['thick_list'] if thick_num(t)}

# uniqueness check
paths = [p['path'] for p in perf]
assert len(paths) == len(set(paths)), [x for x in paths if paths.count(x) > 1]

materials = []
for name, m in C.MATERIALS.items():
    ps = [p for p in perf if p['material'] == name]
    holes_present = [C.HOLES[k]['short'] for k in C.HOLES if any(p['hole'] == k for p in ps)]
    materials.append(dict(name=name, short=m['short'], slug=m['slug'], path=f"/perforated-metal/{m['slug']}/", image=m['image'], blurb=m['blurb'], count=len(ps), holes=holes_present, products=ps, density=m['density']))
holes = []
for key, h in C.HOLES.items():
    ps = [p for p in perf if p['hole'] == key]
    sample = sorted(ps, key=lambda p: p['oa_num'])[len(ps)//2]
    holes.append(dict(key=key, name=h['name'], short=h['short'], slug=h['slug'], path=f"/perforated-metal/{h['slug']}/", blurb=h['blurb'], count=len(ps), svg=pattern_svg(sample, 160), products=ps))
guides = [dict(g, path=f"/guides/{g['slug']}/") for g in C.GUIDES]
applications = [dict(a, path=f"/applications/{a['slug']}/") for a in C.APPLICATIONS]
stats = dict(perf=len(perf), expanded=sum(1 for p in products if p['family']=='expanded'),
             min_hole=fmt(min(p['dims']['size'] for p in perf if p['hole']!='slotted')), max_hole=fmt(max(p['dims']['size'] for p in perf if p['hole']!='slotted')),
             min_oa=fmt(min(p['oa_num'] for p in perf)), max_oa=fmt(max(p['oa_num'] for p in perf)),
             min_thick=fmt(min(thick_num(t) for p in perf for t in p['thick_list'] if thick_num(t))), max_thick=fmt(max(thick_num(t) for p in perf for t in p['thick_list'] if thick_num(t))))
thicknesses = sorted({t for p in perf for t in p['thick_list']}, key=lambda t: thick_num(t) or 0)

GLOBALS = dict(site=SITE, staging=STAGING, year=YEAR, materials=materials, holes=holes, guides=guides, applications=applications, stats=stats, thicknesses=thicknesses)

ORG = {"@type": "LocalBusiness", "@id": SITE['url'] + "/#org", "name": "Kenton Technical Products Ltd", "url": SITE['url'] + "/", "telephone": "+44 117 963 4579", "email": "holes@kentons.biz",
       "image": SITE['url'] + "/assets/img/istock-172765798.webp", "logo": SITE['url'] + "/assets/img/kenton-metal-logo1-1.webp", "foundingDate": "1986",
       "address": {"@type": "PostalAddress", "streetAddress": "25/26 Barnack Trading Centre, Novers Hill", "addressLocality": "Bristol", "postalCode": "BS3 5QE", "addressCountry": "GB"},
       "geo": {"@type": "GeoCoordinates", "latitude": 51.4291, "longitude": -2.6010}, "areaServed": "GB", "priceRange": "££", "sameAs": ["https://kentons.biz/"], "knowsAbout": ["Perforated metal", "Expanded metal", "Welded wire mesh", "Woven wire mesh", "Sheet metal fabrication"],
       "description": "Manufacturer and stockist of perforated metal, expanded metal, welded and woven wire mesh. Established 1986, Bristol."}

def breadcrumb_ld(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c['name'], "item": SITE['url'] + c['path']} for i, c in enumerate(crumbs)]}

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q['q'], "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', q['a'])}} for q in faqs]}

def clip(d, n=158):
    if len(d) <= n: return d
    cut = d[:n]
    for sep in ('. ', '; ', ', '):
        i = cut.rfind(sep)
        if i > 80: return cut[:i].rstrip(',;') + '.'
    return cut.rsplit(' ', 1)[0] + '…'

def render(template, path, page, priority=0.5, **ctx):
    page = dict(page); page['path'] = path
    page['description'] = clip(page['description'])
    if len(page['title']) > 70 and page['title'].endswith(' | Kenton Technical Products'):
        page['title'] = page['title'][:-len(' | Kenton Technical Products')] + ' | Kenton'
    page.setdefault('jsonld', [])
    if page.get('breadcrumbs'):
        page['jsonld'].append(breadcrumb_ld(page['breadcrumbs']))
    if page.get('faqs'):
        page['jsonld'].append(faq_ld(page['faqs']))
    if template == 'listing.html' and ctx.get('groups'):
        items = []
        for g in ctx['groups']:
            for r in g['rows']:
                mm = re.search(r'href="([^"]+)"[^>]*>(?:<strong>)?([^<]+)', r[0] if r[0].startswith('<a') else (r[1] if len(r) > 1 else ''))
                if mm: items.append((mm.group(1), mm.group(2)))
        if items:
            page['jsonld'].append({"@context": "https://schema.org", "@type": "ItemList", "name": page.get('h1'), "numberOfItems": len(items), "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": SITE['url'] + u} for i, (u, n) in enumerate(items)]})
    for ld in page['jsonld']:
        if isinstance(ld, dict) and ld.get('@type') == 'Article':
            ld.setdefault('datePublished', BUILD_DATE); ld['dateModified'] = BUILD_DATE
            ld['image'] = SITE['url'] + (page.get('image') or '/assets/img/istock-172765798.webp')
    out = env.get_template(template).render(page=page, **GLOBALS, **ctx)
    fs = os.path.join(OUT, path.strip('/'), 'index.html') if path != '/' else os.path.join(OUT, 'index.html')
    os.makedirs(os.path.dirname(fs), exist_ok=True)
    open(fs, 'w').write(out)
    pages.append((path, priority))

def faqs(lst):
    return [dict(q=q, a=a) for q, a in lst]

# ---------- clean output (keep assets) ----------
for entry in os.listdir(OUT):
    if entry in ('assets',): continue
    p = os.path.join(OUT, entry)
    shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)

# ---------- home ----------
render('home.html', '/', dict(title='Perforated Metal & Wire Mesh Manufacturer, Bristol | Kenton Technical Products',
    description='UK manufacturer and stockist of perforated metal sheet in mild steel, galvanised, stainless, aluminium and copper, plus expanded metal, welded and woven wire mesh. Next-day delivery on stock. Est. 1986, Bristol.',
    jsonld=[{"@context": "https://schema.org", "@graph": [ORG, {"@type": "WebSite", "url": SITE['url'] + "/", "name": SITE['name'], "publisher": {"@id": SITE['url'] + "/#org"}}]}]), priority=1.0)

# ---------- perforated hub ----------
crumb_home = dict(name='Home', path='/')
crumb_perf = dict(name='Perforated metal', path='/perforated-metal/')
render('perforated.html', '/perforated-metal/', dict(
    title='Perforated Metal Sheet UK Manufacturer & Stockist | Kenton Technical Products',
    description=f'Perforated metal sheet from stock in mild steel, pre-galvanised, stainless, aluminium and copper: {stats["perf"]} round, square and slotted patterns, 1mm–30mm holes, plus bespoke perforating. Next-day UK delivery from Bristol.',
    h1='Perforated metal sheet, manufactured and stocked in the UK',
    lede=f'{stats["perf"]} stock perforations in five materials, each with full specifications, sheet sizes and lead times. Bespoke hole sizes, pitches, margins and fabrication to order.',
    breadcrumbs=[crumb_home, crumb_perf], faqs=faqs(C.PERFORATED_FAQS)), priority=0.9, faqs=faqs(C.PERFORATED_FAQS))

# ---------- finder ----------
rows = sorted(perf, key=lambda p: (p['material'], p['hole'], p['dims']['size'], p['dims']['pitch'] or 0))
render('finder.html', '/perforated-metal/finder/', dict(
    title='Perforation Finder: Search by Hole Size, Open Area & Material | Kenton',
    description=f'Filter all {stats["perf"]} stock perforated metal patterns by material, hole shape, hole size, pitch, open area and thickness. Instant specs, sheet sizes and lead times.',
    breadcrumbs=[crumb_home, crumb_perf, dict(name='Perforation finder', path='/perforated-metal/finder/')]), priority=0.8, rows=rows)

def stock_table_rows(ps):
    out = []
    for p in sorted(ps, key=lambda p: (p['dims']['size'], p['dims']['pitch'] or 0)):
        badge = '<span class="badge badge-ok">In stock</span>' if p['in_stock'] else '<span class="badge badge-warn">5–7 days</span>'
        out.append([f'<a href="{p["path"]}"><strong>{p["code"]}</strong></a>', p['hole_desc'], p['pitch_desc'], p['open_area'], ', '.join(p['thick_list']), ', '.join(p['sizes']), badge])
    return out
COLS = ['Pattern', 'Hole', 'Pitch', 'Open area', 'Thicknesses', 'Sheet sizes', 'Stock']

# ---------- material pages ----------
for m in materials:
    cm = C.MATERIALS[m['name']]
    groups = []
    for h in holes:
        ps = [p for p in m['products'] if p['hole'] == h['key']]
        if not ps: continue
        groups.append(dict(id=h['slug'], title=f"{h['name']} · {m['name'].lower() if m['name']!='Pre-Galvanised Steel' else 'pre-galvanised steel'}", text=h['blurb'], cols=COLS, rows=stock_table_rows(ps), link=dict(name=f"{h['short']} {m['name'].lower()} in detail", path=f"{m['path']}{h['slug']}/")))
    chips = [dict(name=x['name'], path=x['path'], active=x['name']==m['name']) for x in materials]
    tt = {'Mild Steel':'Perforated Mild Steel Sheet','Pre-Galvanised Steel':'Perforated Galvanised Steel Sheet','Stainless Steel':'Perforated Stainless Steel Sheet (304 & 316)','Aluminium':'Perforated Aluminium Sheet','Copper':'Perforated Copper Sheet'}[m['name']]
    sizes = sorted({p['dims']['size'] for p in m['products']})
    render('listing.html', m['path'], dict(
        title=f"{tt} UK Stockist & Manufacturer | Kenton Technical Products",
        description=f"{m['name']} perforated sheet from stock: {m['count']} round, square{' and slotted' if 'Slotted' in m['holes'] else ''} hole patterns, {fmt(min(sizes))}mm to {fmt(max(sizes))}mm holes, 2000×1000 and 2500×1250mm sheets. Cut to size, bespoke perforating and coating. Next-day UK delivery.",
        h1=f"{tt.replace(' (304 & 316)','')}", kicker='Perforated metal', lede=m['blurb'], chips=chips, intro=cm['intro'] + '<p><strong>Browse by thickness:</strong> ' + ' · '.join(f'<a href="{m["path"]}{fmt(t).replace(".", "-")}mm/">{fmt(t)}mm</a>' for t in sorted({thick_num(x) for p in m['products'] for x in p['thick_list'] if thick_num(x)}) if sum(1 for p in m['products'] if any(thick_num(y)==t for y in p['thick_list'])) >= 3) + ('. See also <a href="/perforated-steel/">perforated steel compared</a>.' if 'Steel' in m['name'] else '.') + '</p>',
        breadcrumbs=[crumb_home, crumb_perf, dict(name=m['name'], path=m['path'])], faqs=faqs(cm['faqs']), faq_title=f"{m['name']} perforated sheet FAQs",
        image=m['image']), priority=0.8, groups=groups)

# ---------- hole shape pages ----------
for h in holes:
    ch = C.HOLES[h['key']]
    groups = []
    for m in materials:
        ps = [p for p in h['products'] if p['material'] == m['name']]
        if not ps: continue
        groups.append(dict(id=m['slug'], title=f"{m['name']} · {h['name'].lower()}", text=None, cols=COLS, rows=stock_table_rows(ps), link=dict(name=f"All {m['name'].lower()} patterns", path=m['path'])))
    chips = [dict(name=x['short'], path=x['path'], active=x['key']==h['key']) for x in holes]
    render('listing.html', h['path'], dict(
        title=f"{h['name'].replace(',','')} perforated sheet: {h['count']} patterns | Kenton",
        description=f"{h['name']} perforated metal ({ch['desc']}): {h['count']} stock patterns across mild steel, galvanised, stainless, aluminium and copper with hole size, pitch, open area, thickness and lead time. Bespoke sizes to order.",
        h1=f"{h['name']} perforated sheet", kicker='Perforated metal · hole patterns', lede=h['blurb'], chips=chips, intro=ch['intro'],
        breadcrumbs=[crumb_home, crumb_perf, dict(name=h['name'], path=h['path'])]), priority=0.7, groups=groups)

crumbs = lambda name, path: [crumb_home, dict(name=name, path=path)]
# ---------- material × hole-shape pages ----------
mh_path = {}
for m in materials:
    for h in holes:
        ps = [p for p in m['products'] if p['hole'] == h['key']]
        if not ps: continue
        path = f"{m['path']}{h['slug']}/"
        mh_path[(m['name'], h['key'])] = path
        ml = m['name'].lower() if m['name'] != 'Pre-Galvanised Steel' else 'pre-galvanised steel'
        sizes = sorted({p['dims']['size'] for p in ps}); oas = sorted({p['oa_num'] for p in ps})
        th = sorted({thick_num(t) for p in ps for t in p['thick_list'] if thick_num(t)})
        hs = h['name'].lower().replace(',', '')
        intro = f"""<p>We hold {len(ps)} {hs} pattern{'s' if len(ps)>1 else ''} in {ml} from stock, with {'slot widths' if h['key']=='slotted' else 'hole sizes'} from {fmt(min(sizes))}mm to {fmt(max(sizes))}mm and open areas from {fmt(min(oas))}% to {fmt(max(oas))}%, in thicknesses of {fmt(min(th))}mm to {fmt(max(th))}mm. Every pattern below has its own page with full specifications, sheet sizes and lead times; anything not listed can be perforated to order.</p>
{C.HOLES[h['key']]['intro']}
<p>{C.MATERIALS[m['name']]['blurb']} Read more about <a href="{m['path']}">perforated {ml}</a>, compare with <a href="{h['path']}">{hs} patterns in other materials</a>, or check any specification with the <a href="/guides/open-area-calculator/">open area and weight calculator</a>.</p>"""
        other = [dict(name=x['short'], path=mh_path.get((m['name'], x['key']), x['path']), active=x['key']==h['key']) for x in holes if any(p['hole']==x['key'] for p in m['products'])]
        render('listing.html', path, dict(
            title=f"{h['name'].replace(',','')} perforated {ml} sheet: {len(ps)} patterns | Kenton",
            description=f"{h['name']} perforated {ml} sheet from stock: {len(ps)} patterns, {fmt(min(sizes))}–{fmt(max(sizes))}mm {'slots' if h['key']=='slotted' else 'holes'}, {fmt(min(oas))}–{fmt(max(oas))}% open area, {fmt(min(th))}–{fmt(max(th))}mm thick. Specs, sheet sizes and lead times; cut to size and bespoke perforating.",
            h1=f"{h['name']} perforated {ml} sheet", kicker=f"Perforated {ml}", lede=h['blurb'], chips=other, intro=intro,
            breadcrumbs=[crumb_home, crumb_perf, dict(name=m['name'], path=m['path']), dict(name=h['name'], path=path)], image=m['image']), priority=0.6,
            groups=[dict(id='patterns', title=f"{h['name']} patterns in {ml}", text=None, cols=COLS, rows=stock_table_rows(ps))])
# link material-page groups to these
for m in materials:
    pass

# ---------- material × thickness pages ----------
for m in materials:
    ml = m['name'].lower() if m['name'] != 'Pre-Galvanised Steel' else 'pre-galvanised steel'
    ths = sorted({thick_num(t) for p in m['products'] for t in p['thick_list'] if thick_num(t)})
    for t in ths:
        ps = [p for p in m['products'] if any(thick_num(x)==t for x in p['thick_list'])]
        if len(ps) < 3: continue
        tslug = fmt(t).replace('.', '-') + 'mm'
        path = f"{m['path']}{tslug}/"
        rows = []
        for p in sorted(ps, key=lambda p: (p['hole'], p['dims']['size'])):
            av = [a for a in p['availability'] if thick_num(a['thickness'])==t]
            instock = any('stock' in a['status'].lower() for a in av)
            sizes = ', '.join(sorted({a['size'] for a in av}))
            w = p['weights'].get(next(x for x in p['thick_list'] if thick_num(x)==t))
            rows.append([f'<a href="{p["path"]}"><strong>{p["code"]}</strong></a>', p['hole_name'], p['hole_desc'], p['pitch_desc'], p['open_area'], sizes, f"~{w} kg/m²" if w else '', '<span class="badge badge-ok">In stock</span>' if instock else '<span class="badge badge-warn">5–7 days</span>'])
        n_stock = sum(1 for r in rows if 'badge-ok' in r[-1])
        intro = f"""<p>{fmt(t)}mm is {'the most popular' if t in (1.0, 1.5, 2.0) else 'a'} thickness for perforated {ml}: we hold {len(ps)} patterns in {fmt(t)}mm, {n_stock} of them on the shelf for next-working-day delivery and the rest on a 5–7 day lead time. The table lists every pattern with its open area, the sheet sizes available in this thickness and the approximate weight per square metre.</p>
<p>{'Thin sheet suits fine patterns, decorative panels, grilles and covers, and keeps weight down; stiffen larger panels with a folded return.' if t <= 1.5 else 'This is the usual choice for machine guards, infill panels and general fabrication: stiff enough for panels around a metre across without extra support, and still easy to fold and roll.' if t <= 2.0 else 'Heavier sheet for walkways, large unsupported panels, heavy screens and anywhere impact resistance matters. Hole sizes are limited to roughly the sheet thickness and above.'} Use the <a href="/guides/open-area-calculator/">open area and weight calculator</a> to compare thicknesses, or see all <a href="{m['path']}">perforated {ml}</a> patterns.</p>"""
        chips = [dict(name=f"{fmt(x)}mm", path=f"{m['path']}{fmt(x).replace('.', '-')}mm/", active=x==t) for x in ths if sum(1 for p in m['products'] if any(thick_num(y)==x for y in p['thick_list'])) >= 3]
        render('listing.html', path, dict(
            title=f"{fmt(t)}mm Perforated {m['name'].replace('Pre-Galvanised Steel','Galvanised Steel')} Sheet: {len(ps)} Patterns from Stock | Kenton",
            description=f"{fmt(t)}mm thick perforated {ml} sheet: {len(ps)} round, square and slotted hole patterns with open area, sheet size, weight and stock status. {n_stock} in stock for next-day UK delivery; cut to size available.",
            h1=f"{fmt(t)}mm perforated {ml} sheet", kicker=f"Perforated {ml} by thickness", lede=f"Every {ml} perforation available in {fmt(t)}mm, with sizes, open area and weight.", chips=chips, intro=intro,
            breadcrumbs=[crumb_home, crumb_perf, dict(name=m['name'], path=m['path']), dict(name=f"{fmt(t)}mm", path=path)], image=m['image']), priority=0.5,
            groups=[dict(id='patterns', title=f"Perforated {ml} patterns in {fmt(t)}mm", text=None, cols=['Pattern', 'Type', 'Hole', 'Pitch', 'Open area', f'Sheet sizes in {fmt(t)}mm', 'Approx. weight', 'Stock'], rows=rows)])

# ---------- perforated steel hub ----------
PS = C.PERFORATED_STEEL
steel = [m for m in materials if 'Steel' in m['name']]
render('page.html', '/perforated-steel/', dict(title=PS['title'], description=PS['description'], h1=PS['h1'], kicker='Perforated metal', lede=PS['lede'], body=PS['body'], faqs=faqs(PS['faqs']), hero_image='/assets/img/perforated-metal-5mmhole-8mmpitch.webp', hero_alt='Perforated mild steel sheet with 5mm round holes', image='/assets/img/perforated-metal-5mmhole-8mmpitch.webp',
    breadcrumbs=[crumb_home, crumb_perf, dict(name='Perforated steel', path='/perforated-steel/')], cards_title='Perforated steel by type',
    cards=[dict(path=m['path'], title=f"Perforated {m['name'].lower()}", summary=m['blurb'], image=m['image']) for m in steel]), priority=0.9)

# ---------- Bristol / local page ----------
B = C.BRISTOL
render('page.html', '/perforated-metal-bristol/', dict(title=B['title'], description=B['description'], h1=B['h1'], kicker='Local supply', lede=B['lede'], body=B['body'], faqs=faqs(B['faqs']), breadcrumbs=crumbs('Bristol & South West', '/perforated-metal-bristol/'), jsonld=[{"@context": "https://schema.org", "@graph": [ORG]}]), priority=0.6)

# ---------- product pages ----------
app_for = {}  # (material, code) -> [application]
for a in applications:
    for k in a['patterns']:
        app_for.setdefault(k, []).append(a)
by_code = {}
for p in perf: by_code.setdefault(p['code'], []).append(p)
for p in perf:
    m = C.MATERIALS[p['material']]
    d = p['dims']
    spec = [('Pattern', f"<strong>{p['code']}</strong> (DIN 24041)"), ('Material', p.get('material_detail') or p['material']), ('Hole', p['hole_desc'])]
    if d['pitch']:
        spec.append(('Pitch', p['pitch_desc'] + ' (centre to centre)'))
        spec.append(('Bar width', f"{fmt(round(p['bar'], 2))}mm"))
    spec += [('Open area', p['open_area']), ('Thicknesses from stock', ', '.join(p['thick_list'])), ('Sheet sizes', ', '.join(p['sizes']))]
    if p.get('pattern'): spec.append(('Kenton reference', p['pattern']))
    wts = ', '.join(f"{t}: ~{w} kg/m²" for t, w in p['weights'].items())
    if wts: spec.append(('Approx. weight', wts))
    spec.append(('Margins', 'Small side margins, no end margins on stock sheet; margins to order'))
    spec.append(('Finish', 'Mill finish, without surface treatment; coating and polishing available'))
    # stock rows
    stock_rows = []
    for t in p['thick_list']:
        cells = []
        for s in p['sizes']:
            a = next((x for x in p['availability'] if x['thickness']==t and x['size']==s), None)
            if a:
                ok = 'stock' in a['status'].lower()
                cells.append(dict(label=('In stock' if ok else a['status']) + ('*' if a['note'] else ''), cls='badge-ok' if ok else 'badge-warn'))
            else:
                cells.append(None)
        stock_rows.append(dict(thickness=t, cells=cells))
    notes = ['* ' + n for n in p['notes']]
    # body copy
    hn = C.HOLES[p['hole']]
    oa = p['oa_num']
    uses = {'round-staggered': 'general screening, guarding, ventilation and acoustic facings', 'round-square': 'architectural screens, shop fittings and panels where the grid pattern is on show', 'square': 'guards, screens and ceilings needing maximum open area', 'slotted': 'grading, sizing, de-watering and drainage screens'}[p['hole']]
    if oa >= 55: oa_txt = 'a very high open area, so it offers minimal resistance to air, light and liquid and is among the lightest patterns for its thickness, at the cost of stiffness'
    elif oa >= 40: oa_txt = 'a high open area that suits ventilation, acoustic facings and screens where see-through matters, while keeping useful stiffness'
    elif oa >= 28: oa_txt = 'a moderate open area that balances airflow and visibility against strength, the usual territory for guards and general-purpose screens'
    else: oa_txt = 'a relatively low open area, giving a strong, rigid sheet with a fine, almost solid appearance from a distance'
    mat_txt = {'Mild Steel': 'Mild steel is the economical choice and takes powder coating well after fabrication; it is supplied self-colour and needs a finish for exterior use.',
               'Pre-Galvanised Steel': 'Pre-galvanised steel gives good corrosion resistance for exterior and agricultural use without the cost of stainless.',
               'Stainless Steel': 'Stainless steel gives hygiene, corrosion resistance and a bright self-finish for food, marine, chemical and architectural work; grade 316 is available to order.',
               'Aluminium': 'Aluminium is about a third of the weight of steel, does not rust and takes anodising and powder coating well, which makes it the architectural favourite.',
               'Copper': 'Copper is chosen for its warm colour and natural patina in decorative and interior work.'}[p['material']]
    body = f"""<p>{p['code']} is {'a' if p['hole']!='slotted' else 'a'} {hn['name'].lower()} pattern with {p['hole_desc']}s{(' on a ' + p['pitch_desc'] + ' pitch') if d['pitch'] else ''}{(', leaving ' + fmt(round(p['bar'],2)) + 'mm bars between holes') if d['pitch'] else ''}, giving {p['open_area']} open area. That is {oa_txt}. Patterns of this type are typically used for {uses}.</p>
<p>{mat_txt} This pattern is held in {', '.join(p['thick_list'])} thickness{'es' if len(p['thick_list'])>1 else ''} in {' and '.join(p['sizes'])} sheets{'; items marked in stock ship next working day' if p['in_stock'] else ', made to order on a 5–7 day lead time'}. Stock sheet has small side margins and the pattern runs off the sheet ends; we can cut to size, leave unperforated margins or areas to your drawing, fold, roll and coat: see <a href="/fabrication-and-coating/">fabrication and coating</a>.</p>
<p>Need a different hole size, pitch or thickness? We perforate to order. Use the <a href="/guides/open-area-calculator/">open area and weight calculator</a> to check alternatives, or <a href="/contact/">send us your specification</a>.</p>"""
    same = [dict(path=q['path'], material=q['material'], code=q['code']) for q in by_code[p['code']] if q is not p]
    sibs = [q for q in perf if q['material']==p['material'] and q['hole']==p['hole'] and q is not p]
    sibs = sorted(sibs, key=lambda q: abs(q['dims']['size']-d['size']))[:10]
    mat_t = p['material'].replace('Pre-Galvanised Steel','Galvanised Steel')
    hole_t = f"{fmt(d['size'])} × {fmt(d['length'])}mm Slotted" if p['hole']=='slotted' else f"{fmt(d['size'])}mm {'Square' if p['hole']=='square' else 'Round'} Hole"
    title = f"{hole_t} Perforated {mat_t} Sheet, {p['open_area']} Open ({p['code']}) | Kenton"
    apps = app_for.get((p['material'], p['code']), [])
    if apps:
        body += '<h2>Typical applications for ' + p['code'] + '</h2><p>We recommend this pattern for ' + ', '.join(f'<a href="{a["path"]}">{a["short"].lower()}</a>' for a in apps) + '. Each application page explains how to choose hole size, thickness and finish for the job.</p>'
    else:
        body += '<p>See our <a href="/applications/">application guides</a> for help choosing between patterns for guarding, acoustics, facades, screening and ventilation.</p>'
    desc = f"{p['code']} {p['material_lc']} perforated sheet: {p['hole_desc']} holes{(' on ' + p['pitch_desc'] + ' pitch') if d['pitch'] else ''}, {p['open_area']} open area, {', '.join(p['thick_list'])} thick, {' and '.join(p['sizes'])} sheets. {'In stock for next-day UK delivery' if p['in_stock'] else '5–7 day lead time'}; cut to size and bespoke perforating available."
    ctx = dict(p=dict(p, image=p['image_local'], alt=f"{hole_t} perforated {p['material_lc']} sheet, pattern {p['code']}, {p['open_area']} open area", kicker=f"{p['material']} · {hn['name']}", h1=f"{hole_t[0].upper() + hole_t[1:].lower()} perforated {p['material_lc']} sheet – {p['code']}",
        lede=f"{p['hole_desc'].capitalize()} holes{(' on a ' + p['pitch_desc'] + ' pitch') if d['pitch'] else ''}, {p['open_area']} open area. {'In stock' if p['in_stock'] else 'Made to order'} in {', '.join(p['thick_list'])}.",
        spec=spec, stock_rows=stock_rows, notes=notes, body=body, same_pattern=same, siblings=sibs, pattern_desc=hn['desc']))
    offers = {"@type": "AggregateOffer", "priceCurrency": "GBP", "availability": "https://schema.org/InStock" if p['in_stock'] else "https://schema.org/PreOrder", "offerCount": len(p['availability']), "seller": {"@id": SITE['url'] + "/#org"}}
    prod_ld = {"@context": "https://schema.org", "@type": "Product", "name": f"{p['code']} perforated {p['material_lc']} sheet", "sku": p['code'].replace(' ', '-') + '-' + m['slug'], "brand": {"@type": "Brand", "name": "Kenton Technical Products"},
        "image": SITE['url'] + p['image_local'], "description": desc, "material": p.get('material_detail') or p['material'], "url": SITE['url'] + p['path'],
        "additionalProperty": [{"@type": "PropertyValue", "name": "Hole", "value": p['hole_desc']}, {"@type": "PropertyValue", "name": "Pitch", "value": p['pitch_desc']}, {"@type": "PropertyValue", "name": "Open area", "value": p['open_area']}, {"@type": "PropertyValue", "name": "Thickness", "value": ', '.join(p['thick_list'])}, {"@type": "PropertyValue", "name": "Sheet size", "value": ', '.join(p['sizes'])}],
        "offers": offers, "category": f"Perforated metal > {p['material']} > {hn['name']}", "isRelatedTo": [{"@type": "Product", "name": f"{q['code']} perforated {q['material'].lower()} sheet", "url": SITE['url'] + q['path']} for q in by_code[p['code']] if q is not p][:4]}
    render('product.html', p['path'], dict(title=title, description=desc, image=p['image_local'], og_type='product', jsonld=[prod_ld],
        breadcrumbs=[crumb_home, crumb_perf, dict(name=p['material'], path=p['material_path']), dict(name=p['code'], path=p['path'])]), priority=0.6, **ctx)

# ---------- other families ----------
def family_rows(fam):
    out = []
    for p in sorted([x for x in products if x['family']==fam], key=lambda x: x['name']):
        av = p['availability']
        stock = '<span class="badge badge-ok">In stock</span>' if any('stock' in a['status'].lower() for a in av) else '<span class="badge badge-warn">5–7 days</span>'
        thick = ', '.join(sorted({a['thickness'] for a in av}))
        sizes = ', '.join(sorted({a['size'] for a in av}))
        im = f'<img src="{img(p["image"])}" alt="" width="64" height="43" loading="lazy" style="width:64px;border-radius:4px">' if p['image'] else ''
        notes = '; '.join(p['notes'])
        out.append(dict(p=p, im=im, thick=thick, sizes=sizes, stock=stock, notes=notes))
    return out

# expanded
fp = C.FAMILY_PAGES['expanded']
groups = []
for sub, title in [('raised', 'Raised (standard) expanded metal'), ('flat', 'Flattened expanded metal')]:
    rows = [[r['im'], f"<strong>{r['p']['code']}</strong>", r['p']['name'].split('–')[-1].strip(), r['p'].get('material_detail') or 'Mild steel', r['thick'].replace(' ', ' '), r['sizes'], r['stock']] for r in family_rows('expanded') if r['p']['sub']==sub]
    groups.append(dict(id=sub, title=title, text=None, cols=['', 'Pattern', 'Diamond (LWD × SWD)', 'Material', 'Strand / thickness', 'Sheet size', 'Stock'], rows=rows))
render('listing.html', fp['path'], dict(title=fp['title'], description=fp['description'], h1=fp['h1'], kicker=fp['kicker'], lede=fp['lede'], body=fp['body'], faqs=faqs(fp['faqs']), breadcrumbs=crumbs('Expanded metal', fp['path']), image='/assets/img/istock-1391238185.webp'), priority=0.8, groups=groups)
# woven
fp = C.FAMILY_PAGES['woven']
rows = [[r['im'], f"<strong>{r['p']['code']}</strong>", r['p']['name'].replace(r['p']['code'], '').strip(' –'), r['p'].get('material_detail') or 'Stainless 304', (r['p'].get('pattern') or '').replace(r['p']['code'], '').strip(), r['thick'], r['sizes'], r['stock']] for r in family_rows('woven')]
rows.sort(key=lambda r: (0 if 'mesh' in r[2] else 1, int(re.match(r'(\d+)', r[2]).group(1)) if re.match(r'(\d+)', r[2]) else 999))
render('listing.html', fp['path'], dict(title=fp['title'], description=fp['description'], h1=fp['h1'], kicker=fp['kicker'], lede=fp['lede'], body=fp['body'], faqs=faqs(fp['faqs']), breadcrumbs=crumbs('Woven wire mesh', fp['path']), image='/assets/img/woven-mesh.webp'), priority=0.8,
       groups=[dict(id='stock', title='Stock woven wire mesh', text='Stainless steel 304, 1m wide rolls. Cut lengths and panels to order.', cols=['', 'Code', 'Mesh', 'Material', 'Detail', 'Wire', 'Roll', 'Stock'], rows=rows)])
# welded
fp = C.FAMILY_PAGES['welded']
rows = [[r['im'], f"<strong>{r['p']['code']}</strong>", r['p']['name'].split('–')[0].strip(), (r['p'].get('pattern') or ''), r['thick'], r['sizes'], r['stock'] + (f' <span class="small">{r["notes"]}</span>' if r['notes'] else '')] for r in family_rows('welded')]
render('listing.html', fp['path'], dict(title=fp['title'], description=fp['description'], h1=fp['h1'], kicker=fp['kicker'], lede=fp['lede'], body=fp['body'], faqs=faqs(fp['faqs']), breadcrumbs=crumbs('Welded wire mesh', fp['path']), image='/assets/img/istock-1282054715.webp'), priority=0.8,
       groups=[dict(id='stock', title='Stock welded mesh panels', text=None, cols=['', 'Code', 'Centres', 'Specification', 'Wire', 'Panel size', 'Stock'], rows=rows)])
# edging
sp = C.SERVICES['edging']
rows = [[r['im'], f"<strong>{r['p']['code']}</strong>", r['p']['name'].split('–')[0].strip(), r['thick'], r['sizes'] or 'Mild steel, pre-galvanised, aluminium, stainless 304', r['stock']] for r in family_rows('edging')]
render('listing.html', '/profile-edging/', dict(title=sp['title'] + ' | Kenton Technical Products', description=sp['description'], h1=sp['h1'], kicker='Services', lede='Rolled edging profiles to finish, protect and stiffen the cut edges of perforated and expanded metal panels.', body=sp['body'], breadcrumbs=crumbs('Profile edging', '/profile-edging/')), priority=0.6,
       groups=[dict(id='profiles', title='Stock edging profiles', text='All profiles available in mild steel, pre-galvanised steel, aluminium and stainless 304 on a 5–7 day lead time.', cols=['', 'Profile', 'Length', 'Gauge', 'Materials', 'Lead time'], rows=rows)])

# ---------- service pages ----------
sp = C.SERVICES['walkways']
render('page.html', '/walkways/', dict(title=sp['title'] + ' | Kenton Technical Products', description=sp['description'], h1=sp['h1'], kicker='Services', body=sp['body'], faqs=faqs(sp['faqs']), breadcrumbs=crumbs('Perforated walkways', '/walkways/'), hero_image='/assets/img/t2.webp', hero_alt='Kenway raised perforated walkway treadplate', image='/assets/img/t2.webp'), priority=0.7)
sp = C.SERVICES['fabrication']
render('page.html', '/fabrication-and-coating/', dict(title=sp['title'] + ' | Kenton Technical Products', description=sp['description'], h1=sp['h1'], kicker='Services', body=sp['body'], faqs=faqs(sp['faqs']), breadcrumbs=crumbs('Fabrication & coating', '/fabrication-and-coating/'), lede='Cut, folded, rolled, edged, drilled and finished: perforated and expanded metal panels ready to install, from one supplier.'), priority=0.7)
render('page.html', '/services/', dict(title='Fabrication, Coating, Walkways & Edging Services | Kenton Technical Products', description='Kenton Technical Products services: cutting, folding, rolling and drilling of perforated and expanded metal; powder coating, anodising and polishing; Kenway perforated walkways; profile edging.', h1='Services', kicker='Kenton Technical Products', lede='Everything after the perforating: fabrication, finishing, walkway sections and edging, so panels arrive ready to fit.', body='', cards_title='What we offer', breadcrumbs=crumbs('Services', '/services/'),
    cards=[dict(path='/fabrication-and-coating/', title='Fabrication & coating', summary='Cutting, bending, rolling, edging and fixing holes, plus powder coating, anodising, polishing and electropolishing.'),
           dict(path='/walkways/', title='Perforated walkways', summary='Kenway raised perforated treadplate in 3mm steel, aluminium and stainless, in sheets or folded sections.', image='/assets/img/t2.webp'),
           dict(path='/profile-edging/', title='Profile edging', summary='Rolled channel and trim profiles to finish and stiffen panel edges, in four materials.')]), priority=0.5)

# ---------- guides ----------
render('page.html', '/guides/', dict(title='Perforated Metal Guides, Calculators & Specification Help | Kenton Technical Products', description='Practical guides from a UK perforated metal manufacturer: hole pattern codes explained, open area and weight calculator, and how to specify and order perforated sheet.', h1='Guides and tools', kicker='Knowledge', lede='Straight answers from the people who punch the holes.', body='', cards_title='Guides', breadcrumbs=crumbs('Guides', '/guides/'), cards=[dict(path=g['path'], title=g['title'], summary=g['summary']) for g in guides]), priority=0.6)
for g in guides:
    body = g['body']
    if g.get('calculator'):
        opts = ''.join(f'<option value="{C.MATERIALS[m]["density"]}">{m}</option>' for m in C.MATERIALS)
        body = f"""<div class="calc" id="oaCalc">
<div class="row">
<div><label for="cShape">Hole shape &amp; pitch</label><select id="cShape"><option value="round-staggered">Round, staggered (T)</option><option value="round-square">Round, square pitch (U)</option><option value="square">Square hole (C…U)</option><option value="slot">Slot, rounded ends (LR)</option></select></div>
<div><label for="cHole">Hole size / slot length (mm)</label><input id="cHole" type="number" step="0.1" min="0.1" value="5"></div>
<div><label for="cPitch">Pitch (mm)</label><input id="cPitch" type="number" step="0.1" min="0.1" value="8"></div>
</div>
<div class="row hidden" id="slotRow">
<div><label for="cSlot">Slot width (mm)</label><input id="cSlot" type="number" step="0.1" min="0.1" value="5"></div>
<div><label for="cPitch2">Pitch across slots (mm)</label><input id="cPitch2" type="number" step="0.1" min="0.1" value="10"></div>
</div>
<div class="row">
<div><label for="cMat">Material</label><select id="cMat">{opts}</select></div>
<div><label for="cThick">Thickness (mm)</label><input id="cThick" type="number" step="0.1" min="0.1" value="2"></div>
<div><label for="cLen">Sheet length (mm)</label><input id="cLen" type="number" step="1" min="1" value="2000"></div>
<div><label for="cWid">Sheet width (mm)</label><input id="cWid" type="number" step="1" min="1" value="1000"></div>
</div>
<div class="result">
<div><span>Open area</span><output id="cOut">–</output></div>
<div><span>Weight per m²</span><output id="cWeightM2">–</output></div>
<div><span>Sheet weight</span><output id="cWeight">–</output></div>
</div>
<p class="small" style="margin:0">Estimates from nominal dimensions and densities; margins not included.</p>
</div>
""" + body
    render('page.html', g['path'], dict(title=g['title'] + ' | Kenton Technical Products', description=g['description'], h1=g['title'], kicker='Guide', lede=g['summary'], body=body, faqs=faqs(g['faqs']), breadcrumbs=[crumb_home, dict(name='Guides', path='/guides/'), dict(name=g['short'], path=g['path'])],
        jsonld=[{"@context": "https://schema.org", "@type": "Article", "headline": g['title'], "description": g['description'], "author": {"@id": SITE['url'] + "/#org"}, "publisher": {"@id": SITE['url'] + "/#org"}, "mainEntityOfPage": SITE['url'] + g['path']}]), priority=0.7)

# ---------- applications ----------
render('page.html', '/applications/', dict(title='Perforated Metal Applications: Guarding, Acoustics, Facades & More | Kenton', description='How perforated metal is used and specified for machine guarding, acoustic panels, facades and sunscreens, sieving and drainage, ventilation grilles and balustrade infill, with recommended stock patterns.', h1='Perforated metal applications', kicker='Applications', lede='Which pattern, material and thickness for the job, with the stock perforations we recommend most often.', body='', cards_title='By application', breadcrumbs=crumbs('Applications', '/applications/'), cards=[dict(path=a['path'], title=a['title'], summary=a['summary'], image=a['image']) for a in applications]), priority=0.6)
lookup = {(p['material'], p['code']): p for p in perf}
for a in applications:
    rel = [lookup[k] for k in a['patterns'] if k in lookup]
    missing = [k for k in a['patterns'] if k not in lookup]
    if missing: print('WARN missing related', a['slug'], missing)
    render('page.html', a['path'], dict(title=a['title'] + ' | Kenton Technical Products', description=a['description'], h1=a['title'], kicker='Applications', lede=a['summary'], body=a['body'], faqs=faqs(a['faqs']), related_products=rel, hero_image=a['image'], hero_alt=a['title'], image=a['image'],
        breadcrumbs=[crumb_home, dict(name='Applications', path='/applications/'), dict(name=a['short'], path=a['path'])],
        jsonld=[{"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['description'], "author": {"@id": SITE['url'] + "/#org"}, "publisher": {"@id": SITE['url'] + "/#org"}, "mainEntityOfPage": SITE['url'] + a['path']}]), priority=0.7)

# ---------- contact, about, 404 ----------
render('contact.html', '/contact/', dict(title='Contact Kenton Technical Products, Bristol: Quotes for Perforated Metal & Mesh', description='Request a quote for perforated metal, expanded metal, welded or woven mesh. Kenton Technical Products, Barnack Trading Centre, Novers Hill, Bristol BS3 5QE. Tel 0117 963 4579.', breadcrumbs=crumbs('Contact', '/contact/'), jsonld=[{"@context": "https://schema.org", "@graph": [ORG]}]), priority=0.8)
render('page.html', '/about/', dict(title='About Kenton Technical Products: Perforated Metal Manufacturer Since 1986 | Bristol', description='Kenton Technical Products Ltd has manufactured and supplied perforated and expanded metal, woven and welded wire from Bristol since 1986, serving customers across the UK.', h1='About Kenton Technical Products', kicker='Est. 1986', breadcrumbs=crumbs('About', '/about/'),
    body="""<p>Centred in Bristol, Kenton Technical Products Ltd are the suppliers of perforated and expanded metals, woven and welded wire to people all across the UK. Established in 1986, our success has been based on manufacturing and supplying top quality products at competitive prices with excellent customer service.</p>
<p>We hold a comprehensive range of material in stock, available for next working day delivery, and perforate, cut, fabricate and finish to order. Trade customers, fabricators, architects, engineers and one-off buyers are all welcome; if you don't see what you are looking for, <a href="/contact/">contact us</a> and we will usually be able to make it.</p>
<h2>Find us</h2><p>25/26 Barnack Trading Centre, Novers Hill, Bristol BS3 5QE. Telephone <a href="tel:+441179634579">0117 963 4579</a>, email <a href="mailto:holes@kentons.biz">holes@kentons.biz</a>.</p>"""), priority=0.4)
render('page.html', '/404/', dict(title='Page not found | Kenton Technical Products', description='The page you were looking for could not be found.', h1='Page not found', body='<p>Sorry, that page doesn\'t exist. Try the <a href="/perforated-metal/finder/">perforation finder</a>, <a href="/perforated-metal/">perforated metal</a>, or the <a href="/">home page</a>.</p>'), priority=0.0)
pages.pop()  # don't list 404 in sitemap
shutil.move(os.path.join(OUT, '404/index.html'), os.path.join(OUT, '404.html')); os.rmdir(os.path.join(OUT, '404'))

# ---------- sitemap, robots, CNAME, favicon ----------
today = datetime.date.today().isoformat()
img_for = {p['path']: (p['image_local'], f"{p['code']} perforated {p['material_lc']} sheet") for p in perf}
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
for path, pr in pages:
    im = img_for.get(path)
    imx = f'<image:image><image:loc>{SITE["url"]}{im[0]}</image:loc><image:title>{html.escape(im[1])}</image:title></image:image>' if im else ''
    sm.append(f'  <url><loc>{SITE["url"]}{path}</loc><lastmod>{today}</lastmod><priority>{pr:.1f}</priority>{imx}</url>')
sm.append('</urlset>')
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('\n'.join(sm))
open(os.path.join(OUT, 'robots.txt'), 'w').write(("User-agent: *\nDisallow: /\n" if STAGING else "User-agent: *\nAllow: /\nDisallow: /404.html\n\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n") + f"Sitemap: {SITE['url']}/sitemap.xml\n")
open(os.path.join(OUT, 'CNAME'), 'w').write('kentontechnical.co.uk\n')
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
open(os.path.join(OUT, 'assets/favicon.svg'), 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#0d1b2a"/><g fill="#fff"><circle cx="8" cy="8" r="2.4"/><circle cx="16" cy="8" r="2.4"/><circle cx="24" cy="8" r="2.4"/><circle cx="12" cy="16" r="2.4"/><circle cx="20" cy="16" r="2.4"/><circle cx="8" cy="24" r="2.4"/><circle cx="16" cy="24" r="2.4"/><circle cx="24" cy="24" r="2.4"/></g></svg>')
# redirect map from kentons.biz URLs
red = [('https://kentons.biz/', '/'), ('https://kentons.biz/perforated-metal/', '/perforated-metal/'), ('https://kentons.biz/expanded-metal/', '/expanded-metal/'), ('https://kentons.biz/welded-wire/', '/welded-wire-mesh/'), ('https://kentons.biz/woven-wire/', '/woven-wire-mesh/'), ('https://kentons.biz/walkways/', '/walkways/'), ('https://kentons.biz/profile-edging/', '/profile-edging/'), ('https://kentons.biz/fabrication-coating/', '/fabrication-and-coating/'), ('https://kentons.biz/contact-us/', '/contact/'), ('https://kentons.biz/shop/', '/perforated-metal/finder/'),
       ('https://kentons.biz/perforated-mild-steel/', '/perforated-metal/mild-steel/'), ('https://kentons.biz/perforated-pre-galvanised-steel/', '/perforated-metal/pre-galvanised-steel/'), ('https://kentons.biz/perforated-stainless-steel/', '/perforated-metal/stainless-steel/'), ('https://kentons.biz/perforated-aluminium/', '/perforated-metal/aluminium/'), ('https://kentons.biz/perforated-copper/', '/perforated-metal/copper/')]
for p in products:
    if p['family'] == 'perforated': red.append((p['source'], p['path']))
    else: red.append((p['source'], {'expanded': '/expanded-metal/', 'woven': '/woven-wire-mesh/', 'welded': '/welded-wire-mesh/', 'edging': '/profile-edging/'}.get(p['family'], '/')))
for m in materials:
    red.append((f"https://kentons.biz/product-category/perforated-metal/{m['slug']}/", m['path']))
open(os.path.join(ROOT, 'data/redirects-from-kentons-biz.csv'), 'w').write('old_url,new_path\n' + '\n'.join(f'{a},{b}' for a, b in red))
print(f'Built {len(pages)} pages (staging={STAGING}); {len(red)} redirects mapped')
