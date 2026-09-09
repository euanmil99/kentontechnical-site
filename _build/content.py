# Editorial content for the Kenton Technical Products site.
# Product specifications come from data/products.json (scraped from kentons.biz); this file is copy only.

MATERIALS = {
  'Mild Steel': dict(
    slug='mild-steel', short='Mild steel', density=7.85, image='/assets/img/perforated-metal-3mmhole-5mmpitch.webp',
    blurb='The economical general-purpose choice: strong, easy to weld, fold and powder coat. Supplied uncoated (self-colour) for painting or coating after fabrication.',
    intro="""<p>Perforated mild steel sheet is the workhorse of the range: cold-rolled low-carbon steel punched to a regular pattern of round, square or slotted holes. It is the most economical perforated material, easy to cut, fold, roll and weld, and takes powder coating or paint well. Supplied self-colour (uncoated) it will rust if left bare outdoors, so it is normally finished after fabrication or specified in <a href="/perforated-metal/pre-galvanised-steel/">pre-galvanised steel</a> for exterior use.</p>
<p>Typical uses include machine guards and enclosures, ventilation grilles, radiator and speaker covers, sieves and screens, shop fittings, acoustic panels (with a backing) and infill panels that will be powder coated. Standard stock sheets are 2000 × 1000mm and 2500 × 1250mm in thicknesses from 1mm to 3mm; other thicknesses and cut sizes are made to order.</p>""",
    faqs=[
      ('Does perforated mild steel rust?', 'Yes, mild steel is supplied self-colour and will corrode if left unprotected outdoors or in damp conditions. For exterior use either specify <a href="/perforated-metal/pre-galvanised-steel/">pre-galvanised steel</a> or have the finished panel powder coated or hot-dip galvanised. Our <a href="/fabrication-and-coating/">fabrication and coating</a> service covers the full RAL range.'),
      ('Can you cut mild steel perforated sheet to size?', 'Yes. We cut, fold, roll and edge to your drawing, and can leave unperforated margins for fixing or welding. Shearing and bending are best done through unperforated areas for the neatest finish.'),
      ('What thickness should I use?', '1mm to 1.5mm suits grilles, covers and light guards; 2mm is the usual choice for machine guarding and panels up to about a metre span; 3mm for walkways, heavy screens and larger unsupported panels. The <a href="/guides/open-area-calculator/">weight calculator</a> shows how thickness and open area affect panel weight.'),
    ]),
  'Pre-Galvanised Steel': dict(
    slug='pre-galvanised-steel', short='Pre-galvanised', density=7.85, image='/assets/img/perforated-metal-6mmhole-9mmpitch.webp',
    blurb='Zinc-coated steel perforated after galvanising. Good corrosion resistance for exterior and agricultural use without the cost of stainless.',
    intro="""<p>Pre-galvanised perforated sheet is mild steel that was hot-dip zinc coated as a coil before being perforated. The zinc coating gives good corrosion resistance for exterior, agricultural and damp-environment applications at a fraction of the cost of stainless steel. Because the holes are punched after coating, the hole edges are bare steel; in practice the surrounding zinc provides sacrificial protection and the sheet performs well outdoors, but for the most demanding environments consider stainless or post-fabrication hot-dip galvanising.</p>
<p>Pre-galvanised sheet is popular for fencing infill, security screens, ventilation louvres, grain and feed screens, drying trays, drainage covers and any application where a painted mild steel finish would need too much maintenance. It can be powder coated for colour, provided the surface is suitably prepared.</p>""",
    faqs=[
      ('Is pre-galvanised the same as hot-dip galvanised?', 'No. Pre-galvanised sheet is coated as a coil before perforating, so the coating is thinner and uniform and the hole edges are uncoated. Hot-dip galvanising is done to a finished component after fabrication and coats everything, including cut edges, with a thicker layer. We can arrange hot-dip galvanising of fabricated panels on request.'),
      ('Can pre-galvanised perforated sheet be welded?', 'Yes, but the zinc coating burns off around the weld and gives off fumes, so welding needs good extraction and the weld area should be treated with zinc-rich paint afterwards. Where possible we design panels with unperforated margins so they can be bolted or riveted instead.'),
      ('Can I powder coat pre-galvanised sheet?', 'Yes, with the correct pre-treatment. We powder coat in the full RAL colour range as part of our <a href="/fabrication-and-coating/">fabrication and coating</a> service.'),
    ]),
  'Stainless Steel': dict(
    slug='stainless-steel', short='Stainless', density=7.9, image='/assets/img/perforated-metal-2mmhole-3mmpitch.webp',
    blurb='Grade 304 from stock, 316 to order. Hygienic, corrosion resistant and attractive, for food, marine, architectural and chemical environments.',
    intro="""<p>Perforated stainless steel sheet combines corrosion resistance, hygiene and a clean appearance, which is why it is the default for food processing, pharmaceutical, marine, catering and high-specification architectural work. Our stock range is grade 304 (1.4301) with a mill (2B) finish; grade 316 (1.4401), which adds molybdenum for better resistance to chlorides and marine atmospheres, is available to order, as are polished and brushed finishes. Several patterns can also be supplied polished to 240 grit.</p>
<p>Stainless perforated sheet is used for sieves and filters, drainage and drying trays, splash-backs and kitchen fittings, balustrade and lift-car infill, facade and column cladding, sunscreens, speaker grilles and anywhere a bare metal finish must stay bright without maintenance.</p>""",
    faqs=[
      ('Should I use 304 or 316 stainless?', 'Grade 304 is suitable for most interior, food and general exterior use. Choose 316 for coastal and marine locations, swimming pools, chemical or chloride exposure and de-icing salt splash zones. Both grades are available in all our stock patterns; 316 is made to order.'),
      ('What finish does stock stainless perforated sheet have?', 'Stock sheet is a standard mill (2B) finish. Where noted on the product page, patterns can be supplied polished to 240 grit; brushed, bright-polished and electropolished finishes are available through our <a href="/fabrication-and-coating/">finishing service</a>.'),
      ('Can stainless perforated sheet be used outdoors without coating?', 'Yes. That is one of its main advantages: 304 and 316 stainless keep their appearance outdoors without paint or galvanising, needing only occasional washing to remove surface deposits.'),
    ]),
  'Aluminium': dict(
    slug='aluminium', short='Aluminium', density=2.70, image='/assets/img/perforated-metal-8mmhole-12mmpitch.webp',
    blurb='About a third of the weight of steel, naturally corrosion resistant and ideal for anodising or powder coating. The architectural favourite.',
    intro="""<p>Perforated aluminium sheet weighs roughly one third as much as steel of the same thickness, forms a self-protecting oxide layer so it does not rust, and takes anodised and powder-coated finishes beautifully. That combination makes it the first choice for architectural facades, sunscreens, ceiling and wall panels, signage, vehicle and marine fittings, lighting and any application where weight or a coloured finish matters.</p>
<p>Our stock range covers thicknesses from 1mm to 3mm, in round, square and slotted hole patterns. It is easy to cut and fold, and we can supply panels powder coated in any RAL colour or anodised in silver, black or bronze.</p>""",
    faqs=[
      ('How much lighter is aluminium perforated sheet than steel?', 'Aluminium has a density of about 2.7 g/cm³ against 7.85 g/cm³ for steel, so a panel of the same size, thickness and pattern weighs around 34% of its steel equivalent. Use the <a href="/guides/open-area-calculator/">weight calculator</a> to compare.'),
      ('Can aluminium perforated sheet be anodised?', 'Yes. Anodising gives a hard, weather-resistant decorative finish in silver, black, bronze and other colours, to BS standards, in thicknesses from AA5 to AA25. Powder coating is the alternative where a specific RAL colour is needed.'),
      ('Is aluminium strong enough for guarding?', 'For light guards, covers and grilles, yes, particularly in 2mm and 3mm. For heavy machine guarding where impact resistance matters, mild or stainless steel is usually the better choice.'),
    ]),
  'Copper': dict(
    slug='copper', short='Copper', density=8.96, image='/assets/img/perforated-metal-8mmhole-10mmpitch.webp',
    blurb='Warm decorative metal that develops a natural patina. Stocked in a small range of round and slotted patterns for architectural and interior work.',
    intro="""<p>Perforated copper sheet is chosen for its appearance: a warm metallic colour that slowly develops a natural patina, from bright salmon through brown to green depending on exposure. It is used for decorative screens, feature cladding, fireplace and radiator covers, light fittings, bar fronts and restaurant interiors, as well as some specialist electrical and heat-exchange applications.</p>
<p>We hold a small range of round and slotted hole copper perforations from stock in 2000 × 1000mm sheets, and can perforate other patterns to order. Copper can be lacquered to hold its bright finish, or left to age.</p>""",
    faqs=[
      ('Will copper perforated sheet change colour?', 'Yes. Untreated copper tarnishes to brown within months and, outdoors, develops a green patina over years. If you want to keep the bright finish, panels can be clear lacquered after fabrication.'),
      ('Can you make other copper patterns?', 'Yes. The stock range is small, but we can perforate copper sheet to any of our standard patterns, or to your own hole size and pitch, to order.'),
    ]),
}

HOLES = {
  'round-staggered': dict(slug='round-hole-staggered-pitch', name='Round hole, staggered pitch', short='Round staggered', letter='R', pitch_letter='T',
    blurb='The standard perforated pattern: round holes on a 60° triangular pitch. Highest open area and strength for a given hole size.',
    desc='round holes on a 60° staggered (triangular) pitch',
    intro="""<p>Round hole staggered pitch (DIN 24041 "Rv", pattern code R&nbsp;<em>hole</em> T&nbsp;<em>pitch</em>) is the most widely used perforated metal pattern. Holes are arranged on the points of equilateral triangles so each hole has six equally spaced neighbours. That layout packs the holes as closely as possible, giving the highest open area of any pattern for a given hole diameter and bar width, and because the bars between holes run in three directions the sheet stays stiff and flat.</p>
<p>Use it for anything where airflow, drainage, screening or acoustic performance matters: machine guards, ventilation grilles, speaker covers, sieves, drying trays, acoustic panel facings and general-purpose screens. Open area runs from about 23% in the finer patterns to over 60% in the coarse ones.</p>"""),
  'round-square': dict(slug='round-hole-square-pitch', name='Round hole, square pitch', short='Round square pitch', letter='R', pitch_letter='U',
    blurb='Round holes in straight rows and columns. Lower open area than staggered, but a neat rectilinear look that aligns with panel edges and fixings.',
    desc='round holes on a straight (square) pitch',
    intro="""<p>Round hole square pitch (DIN 24041 "Rg", pattern code R&nbsp;<em>hole</em> U&nbsp;<em>pitch</em>) sets the holes in straight rows and columns at 90° to each other. For the same hole size and pitch it gives about 13% less open area than the staggered layout, but the pattern reads as a clean grid, lines up with panel edges and fixing holes, and is easier to align across adjacent panels. It is often chosen for architectural screens, shop fittings and decorative panels where the pattern itself is on show.</p>
<p>Because the bars between holes run only in two directions, square-pitch sheet is slightly less stiff than staggered sheet of the same specification, which is rarely an issue at the open areas involved.</p>"""),
  'square': dict(slug='square-hole', name='Square hole', short='Square hole', letter='C', pitch_letter='U',
    blurb='Square holes on a straight pitch. Very high open areas, up to 64%, with a crisp modern appearance for screens and guards.',
    desc='square holes on a straight (square) pitch',
    intro="""<p>Square hole perforated sheet (DIN 24041 "Qg", pattern code C&nbsp;<em>hole</em> U&nbsp;<em>pitch</em>) punches square openings in straight rows. A square hole has 27% more area than a round hole of the same width, so this pattern achieves the highest open areas in the catalogue, up to 64% in our C8 U10, with correspondingly low resistance to air and light. The straight bars give a strong, contemporary grid appearance that suits guards, screens, ceilings and facade panels.</p>
<p>Square patterns are slightly less stiff than round staggered patterns of similar open area, and the sharp internal corners concentrate stress, so for heavy-duty guarding we usually recommend 2mm or thicker material.</p>"""),
  'slotted': dict(slug='slotted-hole', name='Slotted hole', short='Slotted', letter='LR', pitch_letter='',
    blurb='Rounded-end slots for directional screening, grading and drainage. Slots let long particles through while blocking wide ones, and clear more easily than round holes.',
    desc='rounded-end slots in a staggered layout',
    intro="""<p>Slotted hole perforated sheet (DIN 24041 "Lv", pattern code LR&nbsp;<em>width</em>×<em>length</em>) has rounded-end slots, usually arranged in staggered rows with the slots parallel. Slots are the pattern of choice for grading and sizing, because they pass long, thin material while holding back anything wider than the slot, and for drainage and de-watering, where the long opening resists blinding by fibres and flat particles far better than a round hole. They are also widely used for decorative screens and for grain, seed and potato graders.</p>
<p>Our stock slotted patterns are 5mm wide by 20mm long in mild steel, stainless, aluminium and copper; other slot widths and lengths are available to order.</p>"""),
}

PERFORATED_FAQS = [
  ('What do the pattern codes like R5 T8 mean?', 'They follow DIN 24041. The first letter is the hole shape: <strong>R</strong> round, <strong>C</strong> square, <strong>LR</strong> slot. The number after it is the hole size in millimetres. The second letter is the pitch arrangement: <strong>T</strong> for a 60° staggered (triangular) pitch, <strong>U</strong> for a straight (square) pitch, followed by the centre-to-centre pitch in millimetres. R5 T8 is therefore a 5mm round hole on an 8mm staggered pitch. See the <a href="/guides/perforated-metal-hole-patterns/">hole pattern guide</a>.'),
  ('What is open area and why does it matter?', 'Open area is the percentage of the sheet that is hole rather than metal. It governs airflow, light transmission, drainage rate and acoustic transparency, and also strength and weight: a 60% open sheet is much lighter and more flexible than a 25% one. Round staggered patterns give the highest open area for a given hole size. Calculate it for any pattern with the <a href="/guides/open-area-calculator/">open area calculator</a>.'),
  ('What sheet sizes do you stock?', 'Most patterns are held in 2000 × 1000mm and/or 2500 × 1250mm sheets. Each product page shows exactly which sizes and thicknesses are in stock. We cut to size and can produce other sheet sizes to order.'),
  ('How quickly can you deliver?', 'Stock sheets ship next working day to mainland UK. Made-to-order items, including cut-to-size, non-stock thicknesses and bespoke perforations, are typically 5 to 7 working days; fabrication and coating add to this depending on the work.'),
  ('Can you perforate a pattern that is not in the catalogue?', 'Yes. We perforate in-house and can produce specific hole sizes, pitches and patterns, unperforated margins and areas, and architectural or visual panels to your drawing. <a href="/contact/">Send us the details</a> for a quote.'),
  ('Do you supply small quantities?', 'Yes. Single sheets and cut pieces are welcome alongside trade and production quantities.'),
  ('What are margins on a perforated sheet?', 'Margins are the unperforated strips along the sheet edges. Stock sheet is supplied with small side margins and no end margins (the pattern runs off the sheet ends). For fabricated panels we can leave specified margins on any edge so you have solid metal for folding, welding or fixing.'),
]

GUIDES = [
  dict(slug='perforated-metal-hole-patterns', short='Hole pattern guide', title='Perforated metal hole patterns explained',
    summary='R, C, LR, T and U: how DIN 24041 pattern codes work, what staggered and square pitch mean, and how to pick a pattern.',
    description='How perforated metal patterns are specified: DIN 24041 codes (R, C, LR, T, U), hole size, pitch, bar width, open area and how to choose between round, square and slotted holes.',
    body="""<p>Perforated metal is described by four things: the shape of the hole, its size, the way the holes are arranged, and the distance between hole centres (the pitch). Most UK and European suppliers, Kenton included, use the notation from the German standard DIN 24041, which packs all four into a short code such as <strong>R5 T8</strong> or <strong>C10 U15</strong>. Once you can read the code you can compare any two patterns at a glance.</p>
<h2>Reading a pattern code</h2>
<p>The first group gives the hole shape and size. <strong>R</strong> is a round hole followed by its diameter in millimetres, so R5 is a 5mm round hole. <strong>C</strong> is a square hole followed by the side length (C10 is a 10mm square). <strong>LR</strong> is a slot with rounded ends followed by its width and length, so LR5×20 is a slot 5mm wide and 20mm long.</p>
<p>The second group gives the arrangement and pitch. <strong>T</strong> means a staggered, or triangular, layout in which the holes sit on the points of equilateral triangles at 60° to each other. <strong>U</strong> means a straight, square layout with holes in rows and columns at 90°. The number after the letter is the pitch, the centre-to-centre distance between neighbouring holes, in millimetres. R5 T8 is a 5mm round hole on an 8mm staggered pitch; R10 U15 is a 10mm round hole on a 15mm square pitch.</p>
<p>Some suppliers describe the same patterns with the older Rv/Rg/Qg/Lv abbreviations (Rv = round staggered, Rg = round square pitch, Qg = square straight, Lv = slot staggered); the numbers mean the same thing.</p>
<h2>Bar width and open area</h2>
<p>Subtract the hole size from the pitch and you get the bar (or bridge) width, the solid metal between holes. R5 T8 has 3mm bars; R10 U15 has 5mm bars. Bar width is what gives a sheet its strength and stiffness, and it is also the practical limit on how fine a pattern can be punched in a given thickness: as a rule the hole should not be smaller than the sheet thickness, and the bar should not be much narrower than the thickness either.</p>
<p>Open area is the percentage of the sheet that is hole. For round holes on a staggered pitch it is 90.7 × (d/p)²; on a square pitch 78.5 × (d/p)²; for square holes 100 × (d/p)². The <a href="/guides/open-area-calculator/">calculator</a> does the arithmetic. Open area drives airflow, light, drainage and sound transmission, and inversely drives strength and weight, so it is usually the number to fix first.</p>
<h2>Choosing a pattern</h2>
<p><a href="/perforated-metal/round-hole-staggered-pitch/">Round hole, staggered pitch</a> is the default. It gives the highest open area and strength for a given hole size, is the most economical to punch and is available in the widest range. Choose it unless you have a reason not to.</p>
<p><a href="/perforated-metal/round-hole-square-pitch/">Round hole, square pitch</a> is chosen for its appearance: the holes read as a neat grid that aligns with panel edges and fixings. Open area is about 13% lower than the equivalent staggered pattern.</p>
<p><a href="/perforated-metal/square-hole/">Square holes</a> give the highest possible open area, up to about 64% from stock, with a crisp modern look. They are popular for guards, screens and architectural panels where maximum transparency matters.</p>
<p><a href="/perforated-metal/slotted-hole/">Slotted holes</a> are directional: they pass long, thin material and block wide material, and the long opening resists blinding by fibres and flat particles. They are the choice for grading, sizing, de-watering and drainage screens, and are also used decoratively.</p>
<h2>Margins and pattern orientation</h2>
<p>Stock sheet is supplied with small unperforated margins along the long sides and the pattern running off the short ends. On staggered patterns the rows of holes run parallel to the long side of the sheet; if you need the pattern oriented differently, or specific blank margins for fixing and welding, say so when ordering. We can perforate to a drawing with margins on any edge and blank areas anywhere in the panel.</p>
<h2>Thickness and sheet size</h2>
<p>Our stock thicknesses run from 0.5mm to 10mm depending on pattern and material, in 2000 × 1000mm and 2500 × 1250mm sheets. Thinner sheet suits fine patterns and decorative work; 2mm is the usual choice for guards and panels; 3mm for walkways and heavy screens. Every stock combination is listed on the product pages, which you can filter in the <a href="/perforated-metal/finder/">perforation finder</a>.</p>""",
    faqs=[
      ('What is the difference between pitch and bar width?', 'Pitch is the distance between hole centres; bar width is the solid metal between hole edges, which is the pitch minus the hole size. An R5 T8 pattern has a 5mm hole, an 8mm pitch and 3mm bars.'),
      ('Which pattern is strongest?', 'For the same hole size and open area, round holes on a staggered pitch give the stiffest, strongest sheet because the bars run in three directions. Square holes concentrate stress at their corners and square-pitch patterns have bars in only two directions.'),
      ('What is the smallest hole you can punch?', 'As a rule the hole diameter should be at least equal to the sheet thickness, so 1mm holes need sheet of 1mm or thinner. Our finest stock pattern is R1.1 T2 in 1mm sheet.'),
    ]),
  dict(slug='open-area-calculator', short='Open area & weight calculator', title='Perforated metal open area and weight calculator',
    summary='Work out the open area of any round, square or slotted pattern, and the weight of a sheet or panel in any of our five materials.',
    description='Free calculator for perforated metal open area (round staggered, round square pitch, square and slotted holes) and sheet weight in mild steel, galvanised, stainless, aluminium and copper.',
    calculator=True,
    body="""<h2>How the calculations work</h2>
<p>Open area depends only on the hole size, shape and pitch. For round holes on a 60° staggered pitch the open area is 90.69 × (d ÷ p)² per cent, where d is the hole diameter and p the pitch. For round holes on a square (straight) pitch it is 78.54 × (d ÷ p)². For square holes on a straight pitch it is 100 × (d ÷ p)². For rounded-end slots of width w and length l on pitches p (along the slot) and p₂ (across the slot), the open area is the slot area, w × l − 0.215 × w², divided by p × p₂.</p>
<p>Sheet weight is the solid-sheet weight reduced by the open area: length × width × thickness × density × (1 − open area). We use nominal densities of 7.85 g/cm³ for mild and pre-galvanised steel, 7.9 for stainless steel, 2.7 for aluminium and 8.96 for copper. Real sheets vary slightly with rolling tolerance and margins, so treat the result as a close estimate for handling and transport rather than a certified weight.</p>
<h2>Why open area matters</h2>
<p>Open area sets how much air, light, water or sound passes through the sheet, and how much material is left to carry load. A 3mm hole on a 5mm staggered pitch has about 33% open area; the same hole on a 4mm pitch gives 51%, but with 1mm bars it is far more flexible and weaker. When a specification needs both high open area and strength, the answer is usually a coarser pattern in thicker sheet rather than a fine pattern with narrow bars.</p>
<p>For machine guarding, safety distances in BS EN ISO 13857 relate the permitted opening size to the distance from the hazard, so the hole size, not the open area, governs. For acoustic facings, open area above about 20 to 25% makes the sheet effectively transparent to sound so the absorber behind it does the work. For sunscreens and facades, open area sets the balance between shading and view.</p>""",
    faqs=[
      ('How do I convert open area to airflow?', 'Open area gives the free area of the sheet. Airflow through a perforated sheet is roughly proportional to free area at a given pressure drop, but the discharge coefficient of the holes (typically 0.6 to 0.8) also matters. For ventilation sizing, use the free area with the appropriate coefficient from your design guide.'),
      ('Does the calculator include margins?', 'No. Margins are unperforated and add weight while reducing the overall open area of a finished panel. For a panel with substantial blank areas, calculate the perforated region and the blank region separately.'),
    ]),
  dict(slug='how-to-specify-perforated-metal', short='How to specify perforated metal', title='How to specify and order perforated metal',
    summary='The seven things a supplier needs to quote accurately, with worked examples, and the mistakes that cause re-work.',
    description='A practical checklist for specifying perforated metal sheet: material, pattern, thickness, sheet or panel size, margins, quantity, finish and tolerances, with worked examples.',
    body="""<p>A complete perforated metal specification has seven parts. Give a supplier all seven and you will get an accurate quote first time and a panel that fits; leave one out and someone has to guess. The checklist below is what we ask for at Kenton, and it works for any manufacturer.</p>
<h2>1. Material and grade</h2>
<p>Say which metal and, where it matters, which grade: mild steel, pre-galvanised steel, stainless 304 or 316, aluminium, copper. If you are not sure, describe the environment (interior, exterior, coastal, food contact, chemical) and let the supplier advise. Our <a href="/perforated-metal/">material pages</a> summarise the trade-offs.</p>
<h2>2. Pattern</h2>
<p>Give the DIN code if you know it (R5 T8, C10 U15, LR5×20), or describe the hole shape, hole size and pitch. State the pitch arrangement, staggered or square, because the same hole and pitch give quite different open areas in each. If you have an open area target instead of a pattern, say so; there may be several patterns that achieve it. The <a href="/guides/perforated-metal-hole-patterns/">hole pattern guide</a> explains the notation.</p>
<h2>3. Thickness</h2>
<p>Specify sheet thickness in millimetres. Remember that the hole should be no smaller than the thickness, and that bar width limits the finest pattern for a given thickness. If you are unsure, tell us what the panel has to do and its unsupported span.</p>
<h2>4. Sheet or panel size, and orientation</h2>
<p>Either order stock sheets (2000 × 1000mm or 2500 × 1250mm) or give the finished panel dimensions. On staggered patterns the rows of holes normally run along the long edge; if the pattern must run a particular way relative to the panel, say which. Give tolerances only where they matter; our standard cutting tolerance suits most applications.</p>
<h2>5. Margins and blank areas</h2>
<p>Stock sheet has small side margins and no end margins. For a fabricated panel state the unperforated margin required on each edge, and mark any blank areas needed for fixings, hinges, handles or welding. Margins of 30mm or more make folding and fixing straightforward. Send a sketch: a photo of a hand drawing is fine.</p>
<h2>6. Quantity</h2>
<p>Number of sheets or panels. If it is a repeat or production requirement, say so; call-off scheduling and stockholding can be arranged.</p>
<h2>7. Fabrication and finish</h2>
<p>List any cutting, folding, rolling, edging, fixing holes, welding, and the finish: self-colour, powder coated (RAL number and gloss level), hot-dip galvanised, polished, anodised (colour and thickness). See <a href="/fabrication-and-coating/">fabrication and coating</a>.</p>
<h2>Worked examples</h2>
<p><em>Machine guard panel:</em> "Mild steel, R5 T8, 2mm, 6 off panels 1200 × 800mm, 30mm blank margin all round, 4 off 9mm fixing holes in corners, powder coated RAL 7035 semi-gloss." Everything the fabricator needs is there.</p>
<p><em>Acoustic ceiling facing:</em> "Aluminium, R3 T5, 1.5mm, 40 off 600 × 600mm, pattern centred with equal margins, powder coated RAL 9010 matt, holes to run parallel to panel edge." Centring the pattern and stating orientation avoids a visibly off-centre panel.</p>
<p><em>Sieve tray:</em> "Stainless 304, LR5×20 slots, 1.5mm, cut to 900 × 450mm, slots running along the 900 dimension, 4 sides folded up 40mm, de-burred." Slot direction matters for a grader and has been stated.</p>
<h2>Common mistakes</h2>
<p>Ordering by open area alone, without a hole size, when the hole size governs (guarding, screening). Forgetting margins, then having nowhere to fold or fix. Specifying a hole smaller than the sheet thickness. Not stating pitch arrangement, so staggered and square-pitch quotes are compared as if they were the same product. And quoting a finished size without saying whether it is before or after folding. Any of these is easily fixed at the enquiry stage: <a href="/contact/">call or email</a> and we will check the specification with you before we quote.</p>""",
    faqs=[
      ('Can I send a drawing instead of a written specification?', 'Yes, a dimensioned drawing or even a clear sketch with the material, pattern and thickness noted is ideal. Email it to holes@kentons.biz.'),
      ('What tolerances should I expect?', 'Perforated sheet is a punched product. Hole size and pitch are held closely; overall sheet size, flatness and margin width follow normal sheet-metal tolerances. Where a dimension is critical, tell us and we will confirm what we can hold.'),
      ('Do I have to buy a whole sheet?', 'No. We cut to size and supply single pieces, though a whole stock sheet is often the most economical way to buy a moderate quantity.'),
    ]),
]

APPLICATIONS = [
  dict(slug='machine-guarding', short='Machine guarding', title='Perforated metal for machine guarding and enclosures',
    summary='Guards that keep hands out and let operators see in. Hole size by safety distance, material by environment.',
    description='Perforated metal sheet for machine guards, safety enclosures and equipment covers: choosing hole size to BS EN ISO 13857 safety distances, thickness, material and finish, with stock patterns.',
    image='/assets/img/perforated-metal-5mmhole-8mmpitch.webp',
    patterns=[('Mild Steel','R5 T8'),('Mild Steel','R6 T9'),('Mild Steel','R8 T12'),('Mild Steel','C8 U10'),('Stainless Steel','R5 T8'),('Pre-Galvanised Steel','R6 T8'),('Aluminium','R5 T8')],
    body="""<p>Perforated sheet is the standard infill for fixed machine guards and safety enclosures because it does three jobs at once: it stops fingers, hands and tools reaching a hazard, it lets operators and maintenance staff see what is happening inside, and it lets heat and air out. Compared with welded mesh it gives a flat, easily cleaned surface with no wire ends, and it can be folded and fixed without a frame.</p>
<h2>Choosing the hole size</h2>
<p>The governing standard is BS EN ISO 13857, which sets the minimum distance from a guard opening to a hazard according to the size of the opening. Broadly, openings up to 4mm can be almost at the hazard, openings of 6mm need at least 10mm to the hazard for fingertips, and by 8mm to 10mm the required distance grows quickly because a finger can enter. For most guards mounted close to moving parts, a 5mm or 6mm round hole (R5 T8, R6 T9) is the usual compromise between safety, visibility and airflow. Where the guard stands further back, 8mm or 10mm holes give better vision and ventilation. Always check the standard for the specific hazard and distance; we are happy to help with the calculation.</p>
<h2>Material and thickness</h2>
<p>Mild steel in 2mm is the default for workshop guards, powder coated after fabrication in a safety colour. Pre-galvanised steel suits outdoor plant and washdown areas, stainless steel food and pharmaceutical machinery, and aluminium light-weight hinged or removable panels. For panels over about a metre unsupported, or where impact from ejected parts is possible, go to 3mm or add stiffening folds.</p>
<h2>Fabrication</h2>
<p>Guards are usually supplied as finished panels: cut to size with unperforated margins of 25 to 40mm for folding and fixing, folded returns for stiffness, fixing holes to drawing, and powder coated. Keeping the shearing and bending within the blank margins gives the cleanest edges. Tell us the frame or fixing detail and we will design the margins to suit.</p>
<h2>Visibility and light</h2>
<p>Open area is a good proxy for how well an operator can see through the guard; 40% or more reads as almost transparent from a normal working distance, while below 25% the sheet looks solid. Darker coatings improve see-through, which is one reason guards are often finished in dark grey or black with yellow frames.</p>""",
    faqs=[
      ('What hole size do I need for a machine guard?', 'It depends on the distance from the guard to the hazard, set out in BS EN ISO 13857. As a rule of thumb, 5mm to 6mm round holes suit guards close to the hazard, and 8mm to 10mm holes suit guards 40mm or more away. Check the standard for your case.'),
      ('Is perforated sheet better than welded mesh for guards?', 'Perforated sheet gives a flat, snag-free, easily cleaned panel that can be folded and fixed without a separate frame, and its smaller openings meet safety distances more easily. Welded mesh gives higher open area and is cheaper for very large panels. Many guards use both.'),
    ]),
  dict(slug='acoustic-panels', short='Acoustic panels', title='Perforated metal for acoustic panels and sound absorption',
    summary='Perforated facings that let sound reach the absorber behind. Open area, hole size and thickness for ceilings, walls and enclosures.',
    description='Perforated metal for acoustic panels: how open area and hole size affect sound absorption, recommended patterns and materials for acoustic ceilings, wall panels and equipment enclosures.',
    image='/assets/img/perforated-metal-2mmhole-3.5mmpitch.webp',
    patterns=[('Aluminium','R2 T3.5'),('Aluminium','R3 T5'),('Mild Steel','R2.5 T4'),('Mild Steel','R3 T5'),('Stainless Steel','R2 T3.5'),('Pre-Galvanised Steel','R3 T5'),('Aluminium','R1.5 T2.5')],
    body="""<p>Perforated metal does not absorb sound on its own; it is the facing that protects and conceals an absorbent core, mineral wool, acoustic foam or a fabric-wrapped layer, while letting sound pass through to it. Get the perforation right and the panel performs almost as if the facing were not there. Get it wrong and the facing reflects sound back into the room.</p>
<h2>Open area is the key figure</h2>
<p>Once the open area exceeds roughly 20 to 25%, a perforated facing is acoustically transparent across the speech and music range and the absorber behind does the work. Below about 15% the facing starts to act as a Helmholtz resonator, which can be useful for tuned low-frequency absorption but needs designing. For general-purpose acoustic ceilings, wall panels and enclosures we recommend patterns in the 30 to 50% range: R2 T3.5 (30%), R2.5 T4 (35%), R3 T5 (33%) and R3 T4 (51%) are all popular.</p>
<h2>Hole size and appearance</h2>
<p>Small holes, 1.5mm to 3mm, read as a fine texture from a distance and hide the absorber and any backing fabric. They also keep fingers and debris out and are easier to clean. Larger holes, 5mm and up, show the core and give a more industrial look, and are used for plant-room enclosures and outdoor barriers where appearance is secondary.</p>
<h2>Material and thickness</h2>
<p>Aluminium in 1mm to 1.5mm is the usual choice for ceiling tiles and wall panels because of its weight and finish options; powder coating in any RAL colour or anodising gives a durable decorative surface. Mild steel in 1mm to 1.5mm, powder coated, is more economical for larger panels and enclosures. Stainless suits kitchens, pools and exterior barriers. Thin sheet keeps weight down and, provided the panel is framed or folded, stiffness is rarely a problem.</p>
<h2>Panel construction</h2>
<p>Typical panels are a perforated face folded into a shallow tray, 20 to 50mm deep, with the absorber inside and a fabric or tissue facing between the two to stop fibre migration. We supply the faces cut, folded and coated, with the pattern centred and equal margins so panels line up across a ceiling or wall. Ask for the pattern to be centred when you order; stock sheet has the pattern running off one end.</p>""",
    faqs=[
      ('What open area do I need for an acoustic panel?', 'At least 20 to 25% for the facing to be acoustically transparent; 30 to 50% is typical. Higher open area does not improve absorption further, but it does reduce strength and increase the visibility of the core.'),
      ('Can perforated metal absorb sound on its own?', 'Only slightly. A perforated sheet with a sealed air gap behind it acts as a tuned resonant absorber at low frequencies, which is a specialist design. For broadband absorption you need an absorbent core behind the sheet.'),
    ]),
  dict(slug='architectural-facades-and-screens', short='Facades & screens', title='Perforated metal facades, cladding and architectural screens',
    summary='Rainscreens, sunscreens, balustrade infill and feature panels in aluminium, stainless, galvanised and copper.',
    description='Perforated metal for architectural facades, rainscreen cladding, brise soleil sunscreens, balustrade infill and decorative screens: materials, patterns, open area, finishes and panel fabrication.',
    image='/assets/img/istock-172765798.webp',
    patterns=[('Aluminium','R10 T15'),('Aluminium','R5 T8'),('Aluminium','C10 U15'),('Stainless Steel','R8 T12'),('Stainless Steel','R10 U26'),('Pre-Galvanised Steel','R10 T15'),('Copper','R8 T10'),('Aluminium','LR5x20')],
    body="""<p>Perforated metal gives architects a material that is solid and transparent at the same time. As a rainscreen or over-cladding it hides services, plant and car park structures while letting them breathe. As a brise soleil it cuts solar gain without blocking the view. As balustrade infill, lift-car lining or a feature wall it provides pattern, shadow and texture in a durable, non-combustible material. Because we perforate in-house, we can produce custom hole sizes, graduated patterns and blank areas as well as the standard catalogue.</p>
<h2>Materials</h2>
<p><a href="/perforated-metal/aluminium/">Aluminium</a> is the most common facade material: light, corrosion resistant, and available powder coated in any RAL colour or anodised. <a href="/perforated-metal/stainless-steel/">Stainless steel</a>, in 316 for coastal sites, gives a bright self-finished surface with the longest life. <a href="/perforated-metal/pre-galvanised-steel/">Pre-galvanised steel</a> is the economical choice for car parks, plant screens and industrial buildings, especially when powder coated. <a href="/perforated-metal/copper/">Copper</a> is used for feature panels that will weather to a patina.</p>
<h2>Open area and pattern</h2>
<p>Sunscreens usually sit between 30 and 50% open area, balancing shade against daylight and view; rainscreens and plant screens can be anywhere from 20 to 60% depending on ventilation requirements. Larger holes, 8mm to 20mm, read well at building scale and are easier to keep clean; square pitch and square hole patterns give a crisp grid that lines up with panel joints. Slots and graduated patterns are available to order for more expressive facades.</p>
<h2>Panel design</h2>
<p>Facade panels are typically 2mm or 3mm aluminium, folded into trays with returns of 40 to 60mm for stiffness and fixing, with unperforated margins so the pattern does not run into the fold. Panel sizes up to 2500 × 1250mm are available from stock sheet; larger panels are made to order. We can supply flat perforated sheet for your fabricator, or finished, folded and coated panels ready for installation.</p>
<h2>Fire performance</h2>
<p>Perforated aluminium, steel and stainless sheet are non-combustible (A1 or A2-s1,d0 depending on coating), which makes them suitable for external wall systems on buildings where combustible cladding is restricted. Coatings should be specified with fire classification in mind; we can advise.</p>""",
    faqs=[
      ('What open area should a sunscreen have?', 'Typically 30 to 50%. Lower open areas give more shade but darken the interior and block the view; higher ones look transparent but do less for solar gain. Orientation and the angle of the screen to the glazing matter as much as open area.'),
      ('Can you make custom or graduated patterns for facades?', 'Yes. We perforate to order and can produce specific hole sizes and pitches, patterns that fade across a panel, blank areas and logo or image perforation from your artwork.'),
    ]),
  dict(slug='screening-sieving-and-drainage', short='Screening & sieving', title='Perforated metal for screening, sieving, grading and drainage',
    summary='Sizing screens, sieve trays, drying trays, drainage covers and filters: choosing hole size, shape and material for the product.',
    description='Perforated sheet for sieves, sizing and grading screens, drying and drainage trays and filter backing in mild steel, galvanised and stainless: hole size and shape selection, slotted versus round, and stock patterns.',
    image='/assets/img/perforated-metal-5x20mmhole-lr5x20.webp',
    patterns=[('Stainless Steel','LR5x20'),('Mild Steel','LR5x20'),('Stainless Steel','R2 T3.5'),('Stainless Steel','R3 T5'),('Mild Steel','R1.5 T2.5'),('Pre-Galvanised Steel','R3 T5'),('Stainless Steel','R1.1 T2'),('Mild Steel','R10 T14')],
    body="""<p>Screening is the original job of perforated metal. A punched plate with accurately sized holes separates material by size, drains liquid from solids, supports a filter medium or dries product on a tray. Compared with woven mesh, perforated plate holds its aperture under load, does not stretch or unravel, is easier to clean and lasts longer; compared with wedge wire it is cheaper and available in far more patterns.</p>
<h2>Round or slotted?</h2>
<p>Round holes size particles by their second-largest dimension and are the right choice for roughly spherical or cubic product: grain, pellets, aggregates, coffee, pulses, pharmaceuticals. Slotted holes size by the smallest dimension and pass long, thin material while retaining anything wider than the slot; they are used for grading potatoes, carrots and other elongated produce, for de-watering fibrous slurries, and wherever round holes would blind with flat or stringy material. Slots also give more open area for a given screening width, so they drain faster.</p>
<h2>Hole size and open area</h2>
<p>Pick the hole size from the cut point you need, allowing for material passing at an angle. Then choose the finest pitch that keeps the bars strong enough: a fine pitch gives more open area and throughput, but narrower bars wear faster. Our stock screening patterns run from R1.1 T2 (1.1mm holes) up to R30 T40, and LR5×20 slots; other sizes are made to order.</p>
<h2>Materials</h2>
<p><a href="/perforated-metal/stainless-steel/">Stainless steel</a> 304 or 316 is standard for food, pharmaceutical and wet processes: hygienic, corrosion resistant and easily cleaned. <a href="/perforated-metal/pre-galvanised-steel/">Pre-galvanised steel</a> suits agricultural graders, drying floors and drainage covers. <a href="/perforated-metal/mild-steel/">Mild steel</a> is used for aggregate screens and dry industrial sieving where wear, not corrosion, is the issue, often in 3mm or heavier plate.</p>
<h2>Trays and screens</h2>
<p>Drying trays and sieve trays are usually perforated sheet folded up on four sides, with a blank margin so the fold is in solid metal, and corners welded or clipped. We supply them cut, folded and de-burred to your sizes. For vibrating screens and larger decks, tell us the frame and tensioning arrangement and we will leave the appropriate margins and fixing holes.</p>""",
    faqs=[
      ('Which is better for sieving, perforated plate or woven mesh?', 'Perforated plate for apertures of about 1mm and above where accuracy, durability and cleanability matter, and for anything under load. Woven wire mesh for finer apertures, where perforating is impractical, and where maximum open area at small aperture is needed. We stock both: see <a href="/woven-wire-mesh/">woven wire mesh</a>.'),
      ('Can you supply food-grade perforated sheet?', 'Yes. Stainless 304 and 316 perforated sheet is widely used in food contact applications. Specify the grade, and let us know if you need a polished finish or de-burred edges.'),
    ]),
  dict(slug='ventilation-grilles-and-covers', short='Ventilation & grilles', title='Perforated metal ventilation grilles, radiator covers and speaker grilles',
    summary='Airflow with a finished appearance: patterns and materials for grilles, louvres, plinths, enclosure vents and cabinet panels.',
    description='Perforated metal for ventilation grilles, radiator cabinet fronts, speaker grilles, kitchen plinth vents and enclosure cooling panels: open area, hole size, materials and finishes with stock patterns.',
    image='/assets/img/perforated-metal-3mmhole-4mmpitch.webp',
    patterns=[('Mild Steel','R3 T4'),('Mild Steel','R3 T5'),('Aluminium','R4 T6'),('Aluminium','R2 T3.5'),('Stainless Steel','R3 T5'),('Mild Steel','R4 T6'),('Aluminium','C5 U8'),('Mild Steel','R1.5 T2.5')],
    body="""<p>Wherever air has to pass through a surface that is on show, perforated metal is the neat answer: radiator cabinet fronts, kitchen plinth and cupboard vents, electrical and server enclosure panels, boiler-room doors, air-handling unit grilles, speaker and hi-fi fronts, lighting diffusers. It gives a flat, rigid, paintable panel with a regular pattern that reads as a designed finish rather than a hole in the wall.</p>
<h2>Open area and airflow</h2>
<p>Free area is what the ventilation designer needs, and open area is the starting point. For passive ventilation and radiator covers, 40% or more keeps the resistance low; R3 T4 (51%), R4 T6 (40%) and C5 U8 (39%) are popular. For forced cooling of enclosures, the fan curve and the discharge coefficient of the holes (0.6 to 0.8) set the actual flow; we can supply patterns up to 64% open for the least restriction. Small holes with high open area, such as R3 T4, give the best combination of airflow and finger safety.</p>
<h2>Appearance</h2>
<p>Fine patterns, 1.5mm to 3mm holes, look like a texture and hide what is behind; they suit radiator covers, speaker grilles and furniture. Larger holes suit industrial enclosures and plant-room doors. Square pitch patterns give a grid that aligns with panel edges; staggered patterns look more uniform at a distance. Powder coating to match joinery or a RAL colour, or anodised aluminium, finishes the panel; for speaker grilles, black powder coat on 1mm steel or aluminium is standard.</p>
<h2>Material and thickness</h2>
<p>1mm to 1.5mm mild steel, powder coated, is the economical choice for interior grilles and covers. Aluminium in the same thicknesses is lighter and does not rust if the coating is scratched, so it suits bathrooms, kitchens and exterior vents. Stainless is used for commercial kitchens and exterior louvres. Folding a return on each edge stiffens thin sheet considerably and gives a clean fixing flange.</p>""",
    faqs=[
      ('What is the best pattern for a radiator cover?', 'A fine, high-open-area pattern such as R3 T4 (51%) or R3 T5 (33%) in 1mm or 1.5mm mild steel or aluminium, powder coated. Keep open area at 40% or more so the radiator output is not restricted.'),
      ('Which pattern is used for speaker grilles?', 'Typically 1.5mm to 3mm round holes on a staggered pitch with 30 to 50% open area, in 1mm steel or aluminium, powder coated black. R2 T3.5 and R3 T5 are common choices.'),
    ]),
  dict(slug='balustrade-and-security-infill', short='Balustrade & security', title='Perforated metal balustrade infill, fencing and security screens',
    summary='Infill panels for stairs, balconies and mezzanines, plus security screens and fencing where you need to see through but not climb or reach through.',
    description='Perforated metal panels for balustrade and handrail infill, mezzanine edge protection, security screens, window guards and fencing: hole size for safety, materials for exterior use and fabrication with margins.',
    image='/assets/img/perforated-metal-10mmhole-15mmpitch.webp',
    patterns=[('Pre-Galvanised Steel','R10 T15'),('Pre-Galvanised Steel','R8 T12'),('Stainless Steel','R10 T15'),('Aluminium','R10 T15'),('Mild Steel','R10 T15'),('Stainless Steel','C10 U15'),('Aluminium','R8 T12')],
    body="""<p>Perforated sheet makes an excellent infill for balustrades, stair guarding, mezzanine edge protection, balcony screens and security fencing. It is unclimbable when the holes are small, it will not pass a 100mm sphere (the usual building-regulation test), it cannot be reached through, and it gives privacy and wind protection while still letting light through. Fixed into a steel or aluminium frame, or folded into a self-supporting tray, it is a durable alternative to glass or bar infill.</p>
<h2>Hole size and safety</h2>
<p>For balustrades and stair guarding, Approved Document K requires that a 100mm sphere cannot pass through the infill, which any of our patterns satisfies, and for stairs that the infill is not readily climbable. Small holes (under 12mm) give nothing for a toe to grip. For security screens the same logic applies: holes under about 12mm prevent reach-through with tools, and 6mm or under stop most objects being posted through. Choose patterns such as R8 T12, R10 T15 or C10 U15 for a good balance of view, strength and safety.</p>
<h2>Materials</h2>
<p>For interior balustrades, mild steel powder coated or stainless 304. For balconies, external stairs and fencing, pre-galvanised steel powder coated, aluminium powder coated or stainless 316. Aluminium keeps the weight of large balcony panels manageable; stainless gives the longest life at the coast.</p>
<h2>Panel fabrication</h2>
<p>Infill panels are normally 2mm or 3mm, cut to size with blank margins of 30 to 50mm for fixing into the frame or for folded returns. Where the panel is self-supporting, folding all four edges into a tray makes even 2mm sheet very stiff. We supply panels cut, folded, drilled and coated to your schedule, or flat sheet for your fabricator; see <a href="/fabrication-and-coating/">fabrication and coating</a>.</p>""",
    faqs=[
      ('Does perforated infill meet building regulations for balustrades?', 'Perforated sheet with holes under 100mm satisfies the sphere test in Approved Document K, and small-hole patterns are not readily climbable. The frame, fixings and overall barrier still have to be designed for the required line load; your structural engineer or fabricator will confirm this.'),
      ('What is the best material for an exterior balcony screen?', 'Powder-coated aluminium for weight and colour, or 316 stainless for coastal sites. Powder-coated pre-galvanised steel is a good economical option for fencing and industrial stairs.'),
    ]),
]

SERVICES = dict(
  walkways=dict(title='Kenway raised perforated walkway treadplate', h1='Perforated walkways and anti-slip treadplate',
    description='Kenway raised perforated treadplate: 3mm mild steel, aluminium or stainless 304 with a raised, slip-resistant perforation. Stock 2500 × 1250mm sheets, cut to size and folded into walkway sections.',
    body="""<p><strong>Kenway</strong> raised perforated treadplate is manufactured from 3mm thick material with a raised perforation that forms a slip-resistant surface. Every hole is punched upwards into a raised crescent, so the plate grips in both directions underfoot, sheds water, oil and debris through the perforation, and stays clean. It is supplied in sheet form or cut to size and folded into walkway, step and platform sections ready to fit.</p>
<h2>Materials and stock</h2>
<div class="table-wrap"><table><thead><tr><th>Material</th><th>Thickness</th><th>Stock sheet</th><th>Availability</th></tr></thead><tbody>
<tr><td>Mild steel</td><td>3mm</td><td>2500 × 1250mm</td><td><span class="badge badge-ok">In stock</span></td></tr>
<tr><td>Aluminium</td><td>3mm</td><td>2500 × 1250mm</td><td><span class="badge badge-ok">In stock</span></td></tr>
<tr><td>Stainless 304</td><td>3mm</td><td>2500 × 1250mm</td><td><span class="badge badge-ok">In stock</span></td></tr>
</tbody></table></div>
<p>Mild steel treadplate is normally hot-dip galvanised or powder coated after fabrication for exterior use. Aluminium suits lightweight platforms, vehicle and marine applications. Stainless 304 is used in food, chemical and washdown plants.</p>
<h2>Fabricated walkway sections</h2>
<p>We fold treadplate into channel sections with upstands (toe boards) on one or both sides, which makes a rigid, self-supporting walkway or step. If fabrication is required, confirm the V, W, X, Y and Z dimensions shown in the drawing below; the X, V and W measurements should be 30mm or more. We recommend that bending and shearing take place between the perforated areas to maintain the quality of finish.</p>
<figure><img src="/assets/img/t1-1.webp" alt="Diagram of a folded Kenway walkway section showing dimensions V, W, X, Y and Z" width="582" height="328" style="max-width:480px;border:1px solid #e3e6ea;border-radius:8px"><figcaption class="small">Folded walkway section: overall width Y, length Z, upstand heights V and W, and blank margin X.</figcaption></figure>
<figure><img src="/assets/img/perforation-detail.webp" alt="Detail of the raised, slip-resistant Kenway perforation" width="600" height="400" style="max-width:420px;border:1px solid #e3e6ea;border-radius:8px"><figcaption class="small">Kenway raised perforation detail.</figcaption></figure>
<h2>Typical uses</h2>
<p>Access walkways on plant and rooftops, mezzanine and platform decking, stair treads and landings, vehicle steps and ramps, gantries, loading bays, agricultural and food-plant floors, and anywhere a self-draining, non-slip surface is needed. Sections can be supplied drilled for fixing and finished to your specification.</p>""",
    faqs=[('Is the walkway treadplate slip resistant when wet?','Yes. The raised crescents around each hole give a mechanical grip in all directions, and liquids drain through the perforation rather than pooling on the surface.'),
          ('What span can 3mm treadplate cover?','Folded channel sections are much stiffer than flat plate. The safe span depends on the section depth, width and the load; tell us the application and we will advise, or provide the section properties for your engineer.'),
          ('Can you supply stair treads?','Yes. Treads are folded from the same treadplate with a nosing and fixing flanges, cut to your going and width.')]),
  edging=dict(title='Profile edging for perforated and expanded metal panels', h1='Profile edging',
    description='Rolled metal edging profiles (U, channel, C and T sections) in 3m lengths to finish and stiffen perforated and expanded metal panels, in mild steel, pre-galvanised, aluminium and stainless 304.',
    body="""<p>Profile edging is a rolled channel or trim that slides over or wraps around the cut edge of a perforated or expanded metal panel. It hides the sheared edge, protects hands from burrs, stiffens the panel and gives a neat frame without welding. We hold five profiles in 3m and 3.81m lengths in mild steel, pre-galvanised steel, aluminium and stainless 304, all available on a 5–7 day lead time.</p>
<p>Edging is fitted by crimping or riveting onto the panel edge; the panel is cut slightly under the finished size to allow for the profile. Tell us the panel thickness and we will match the profile opening. Our <a href="/fabrication-and-coating/">fabrication service</a> can supply panels edged and finished ready to install.</p>"""),
  fabrication=dict(title='Perforated metal fabrication and coating services', h1='Fabrication and coating',
    description='Cutting, bending, rolling, edging and fixing holes for perforated and expanded metal, plus powder coating in all RAL colours, anodising, polishing and electropolishing. Finished panels ready to fit, from Bristol.',
    body="""<p>All our products can be cut and fabricated to your own specifications. Sending us a drawing and getting back finished panels, rather than flat sheet, saves you a fabrication step and guarantees that folds, margins and fixing holes land in solid metal where they should. The same team perforates, fabricates and arranges finishing, so there is one point of responsibility for the whole panel.</p>
<h2>Fabrication</h2>
<h3>Cutting</h3><p>Our experienced technical team are qualified to cut to your specifications, from single pieces to production batches, in any of our stock materials.</p>
<h3>Bending</h3><p>Our metal bending technology will shape your metal with accuracy and precision: single folds, returns, trays, channels and boxes. We recommend folds are placed in unperforated margins for the cleanest result.</p>
<h3>Rolling</h3><p>Our rolling expertise means you get the precise shapes you need: curved panels, cylinders and drums for screens, guards, light fittings and architectural features.</p>
<h3>Edging</h3><p>For a smart finish to your product: <a href="/profile-edging/">profile edging</a> crimped or riveted to the panel edge, or folded safety edges.</p>
<h3>Fixing holes</h3><p>We drill fixing holes to your requirements, so panels arrive ready to fit.</p>
<h2>Finishing</h2>
<h3>Powder coating</h3><p>Full range of RAL colours, excellent adhesion and durability, conforms to BS standards. The usual finish for mild steel, pre-galvanised and aluminium panels, in gloss, satin or matt.</p>
<h3>Electropolishing</h3><p>Bright decorative finish, improved corrosion resistance and greater durability for stainless steel, including hygienic applications where a smooth passive surface matters.</p>
<h3>Polishing</h3><p>From dull to highly polished, with a protective coating, single or double sided. Several stainless patterns are available polished to 240 grit from stock.</p>
<h3>Anodising</h3><p>Conforms to BS standards, in a variety of colours including silver, black and bronze. Excellent weather resistance and high durability, available from AA5 to AA25 thickness, for aluminium panels.</p>
<h2>How to order fabricated panels</h2>
<p>Send a dimensioned drawing or sketch with the material, pattern, thickness, finished sizes, margins, folds, fixing holes and finish. Our <a href="/guides/how-to-specify-perforated-metal/">specification guide</a> lists everything we need. We will check the design for manufacturability and quote, typically the same working day.</p>""",
    faqs=[('Can you supply panels fully finished?','Yes. Cut, folded, rolled, edged, drilled and powder coated, anodised or polished, ready to install.'),
          ('What RAL colours are available for powder coating?','The full RAL range, in gloss, satin or matt, plus textured and metallic finishes on request.'),
          ('Do you fabricate expanded metal and mesh as well?','Yes. Expanded metal, welded mesh and woven mesh panels can be cut, framed, edged and coated in the same way.')]),
)

FAMILY_PAGES = dict(
  expanded=dict(path='/expanded-metal/', title='Expanded metal mesh sheets, raised and flattened, from stock', h1='Expanded metal', kicker='Expanded metal',
    description='Expanded metal mesh in mild steel, raised and flattened, from 6mm to 60mm diamond. Stock sheets for next-day delivery; other patterns and materials to order. Bristol, UK-wide delivery.',
    lede='Expanded metal is made by slitting and stretching a single sheet into a diamond mesh, so there are no welds or joints to fail. We hold a wide selection of raised and flattened expanded metal from stock and can supply all types to order.',
    body="""<h2>Raised or flattened?</h2>
<p><strong>Raised</strong> (standard) expanded metal keeps the angled strands produced by the expanding process. The strands stand proud of the sheet plane, which gives excellent grip underfoot and a three-dimensional appearance, and makes the sheet stiff for its weight. It is used for walkways, stair treads, security fencing, machine guards and screens.</p>
<p><strong>Flattened</strong> expanded metal is passed through rollers after expanding so the strands lie flat, giving a smooth sheet of uniform thickness. It is easier to fold, frame and paint, and is used for guards, grilles, shelving, filters, ceilings, decorative panels and rendering lath.</p>
<h2>Reading the pattern</h2>
<p>Expanded metal is described by the long way of the diamond (LWD), the short way of the diamond (SWD), the strand width and the strand thickness. A 43 × 18mm diamond with a 2.5mm strand in 1.2mm sheet, for example, is a light general-purpose mesh; 60 × 25mm with heavier strands is a walkway or security grade. Open area and weight per square metre follow from these dimensions. Our pattern codes (for example 5121MF) are the manufacturer's references; the diamond size is given alongside each.</p>
<h2>Materials and fabrication</h2>
<p>Stock is mild steel, supplied self-colour for painting, powder coating or hot-dip galvanising after fabrication. Aluminium, pre-galvanised and stainless expanded metal are available to order. Sheets can be cut, folded, framed with <a href="/profile-edging/">profile edging</a> and coated through our <a href="/fabrication-and-coating/">fabrication service</a>.</p>""",
    faqs=[('What is the difference between expanded metal and perforated metal?','Perforated metal is punched, removing material to make holes in a flat sheet. Expanded metal is slit and stretched, so nothing is removed and the sheet becomes larger, lighter and, in raised form, three-dimensional. Perforated sheet gives a flat surface and precise hole sizes; expanded metal gives more open area per kilogram and a strong, rigid mesh.'),
          ('Which way should expanded metal be fitted?','Raised expanded metal has a grain: fitted with the long way of the diamond horizontal and the strands angled downward and outward, it sheds water and resists climbing. For walkways, run the long way of the diamond across the direction of travel for the best grip.'),
          ('Can expanded metal be cut to size?','Yes. We cut to size and can fold, frame and coat panels to your drawing.')]),
  woven=dict(path='/woven-wire-mesh/', title='Stainless steel woven wire mesh, 2 to 100 mesh, from stock', h1='Woven wire mesh', kicker='Woven wire',
    description='Stainless steel 304 woven wire mesh from 2 mesh to 100 mesh, plus heavy crimped mesh, in 1m wide rolls from stock. Precision apertures, high open area, cut pieces and panels to order. Bristol, UK-wide delivery.',
    lede='Our woven wire mesh is a high-quality precision product. It offers very high pressure, temperature and corrosion tolerance, accurate apertures, high open areas and good durability.',
    body="""<h2>Mesh count, wire and aperture</h2>
<p>Woven wire mesh is specified by the mesh count (the number of openings per linear inch), the wire diameter and the resulting aperture. A 10 mesh with 0.45mm wire, for example, has ten openings per inch and an aperture of about 2.09mm; a 100 mesh with 0.1mm wire has an aperture of 0.154mm. Finer wire gives a larger aperture and higher open area at the same mesh count, but less strength. Our stock range runs from 2 mesh to 100 mesh in stainless steel 304, in 1m wide rolls, plus heavy crimped meshes in 2.6mm and 4.1mm wire for guards and screens.</p>
<h2>Uses</h2>
<p>Fine meshes (30 to 100) are used for sieving, filtration, insect and vermin screens, laboratory and food processing. Medium meshes (6 to 20) for sieves, strainers, drying and drainage, speaker and vent covers, and decorative infill. Coarse and crimped meshes (2 to 4 mesh and heavier crimped) for machine guards, security screens, animal enclosures, trays and architectural panels.</p>
<h2>Cutting and fabrication</h2>
<p>We supply by the roll, by the metre, or cut to size, and can frame, edge and fold mesh into panels and trays. For apertures above about 1mm where a flat, rigid, easily cleaned surface is wanted, consider <a href="/perforated-metal/">perforated sheet</a> instead; we are happy to advise which suits your application.</p>""",
    faqs=[('What does "mesh" mean in woven wire?','The mesh count is the number of openings per linear inch, counted from the centre of one wire to a point one inch away. Higher numbers mean finer mesh. The actual hole size, the aperture, depends on both the mesh count and the wire diameter.'),
          ('Is your woven mesh food grade?','Stock mesh is stainless steel 304, which is widely used in food processing. Grade 316 is available to order.'),
          ('Can I get woven mesh in other materials?','Yes: 316 stainless, galvanised steel, brass, copper and aluminium mesh are available to order.')]),
  welded=dict(path='/welded-wire-mesh/', title='Welded wire mesh panels, ½" to 3" centres, from stock', h1='Welded wire mesh', kicker='Welded wire',
    description='Welded wire mesh panels in ½", 1", 2" and 3" × ½" centres, 2440 × 1220mm sheets from stock, stainless and galvanised options. Competitive prices and quick delivery; cut to size and fabricated to order.',
    lede='We have competitive prices and quick delivery on all specifications, whether standard stock panels or mesh manufactured to your requirements.',
    body="""<h2>Specification</h2>
<p>Welded mesh is made from straight wires welded at every intersection into a rigid grid. It is specified by the aperture (centre-to-centre spacing of the wires, quoted here in inches), the wire gauge or diameter, the sheet size and the material. Our stock panels are 2440 × 1220mm in ½" × ½", 1" × 1", 2" × 2" and 3" × ½" centres, with grade 316 stainless available for several patterns.</p>
<h2>Uses</h2>
<p>Machine guards and enclosures, storage cages and partitions, shelving and racking decks, animal cages and aviaries, gabions, reinforcing, security screens, trays and baskets, and garden and agricultural fencing. The welded construction gives a flat, rigid panel that can be cut and framed without unravelling.</p>
<h2>Cutting and fabrication</h2>
<p>Panels can be cut to size, folded, framed with <a href="/profile-edging/">profile edging</a> and powder coated or galvanised through our <a href="/fabrication-and-coating/">fabrication service</a>.</p>""",
    faqs=[('What is the difference between welded and woven mesh?','Welded mesh has straight wires welded at each crossing, giving a rigid flat panel with square apertures, usually 6mm and larger. Woven mesh interlaces the wires, is flexible, and is available in much finer apertures.'),
          ('Do you stock galvanised welded mesh?','Stock panels are listed on this page; galvanised and stainless 316 options are available to order for most patterns.')]),
)

GUIDES += [
  dict(slug='perforated-metal-vs-expanded-metal', short='Perforated vs expanded metal', title='Perforated metal vs expanded metal: which should you use?',
    summary='The two are often confused. Here is how they are made, where each wins on strength, weight, cost, appearance and cleanability, and which to pick for common jobs.',
    description='Perforated metal versus expanded metal compared: manufacturing, strength, weight, open area, cost, appearance, cleanability and the best choice for guards, walkways, screens, facades and filters.',
    body="""<p><strong>Short answer:</strong> perforated metal is a flat sheet with holes punched out of it; expanded metal is a sheet slit and stretched into a diamond mesh with nothing removed. Perforated sheet gives a smooth, flat surface, precise hole sizes and the widest choice of patterns and materials, so it wins for guards that need exact openings, screens and sieves, acoustic and architectural panels, and anything that must be cleaned or painted. Expanded metal gives more open area and rigidity per kilogram at lower cost, so it wins for walkways, heavy security fencing, large-span guards and reinforcement where a flat surface does not matter.</p>
<h2>How each is made</h2>
<p>Perforated metal is produced by punching a regular pattern of holes through flat sheet with a die. The material inside each hole is removed as scrap, the sheet stays the same size and thickness, and any hole shape, size and layout that can be tooled is possible. Because the sheet is flattened after punching, the result is a flat, dimensionally stable panel.</p>
<p>Expanded metal is produced by slitting the sheet in a staggered pattern and stretching it, so each slit opens into a diamond. Nothing is removed: the sheet grows in size and the strands twist out of plane, which is what gives raised expanded metal its grip and stiffness. Flattened expanded metal is rolled after expanding to bring the strands back into one plane.</p>
<h2>Where perforated metal is the better choice</h2>
<p><em>Exact openings.</em> Machine guarding to BS EN ISO 13857, sieves, graders and any job where the opening size is specified all need the precise, repeatable holes that punching gives. Expanded diamonds are less consistent and harder to measure against a standard.</p>
<p><em>Flat, cleanable surfaces.</em> Food, pharmaceutical and catering equipment, drying trays, kitchen and ventilation grilles and anything that will be wiped down favour a smooth perforated sheet. Raised expanded metal traps dirt in its strands.</p>
<p><em>Appearance and finish.</em> Architectural facades, sunscreens, balustrades, acoustic ceilings and shop fittings use perforated sheet for its regular, controllable pattern and the way it takes powder coating and anodising evenly. Custom patterns, graduated holes and blank areas are only possible with perforating.</p>
<p><em>Material choice.</em> We stock perforated sheet in <a href="/perforated-metal/mild-steel/">mild steel</a>, <a href="/perforated-metal/pre-galvanised-steel/">pre-galvanised</a>, <a href="/perforated-metal/stainless-steel/">stainless</a>, <a href="/perforated-metal/aluminium/">aluminium</a> and <a href="/perforated-metal/copper/">copper</a>, in 115 patterns; expanded metal is stocked in mild steel with other materials to order.</p>
<h2>Where expanded metal is the better choice</h2>
<p><em>Walkways and grip.</em> Raised expanded metal is self-draining and slip resistant in every direction, and its stiffness lets it span further than flat sheet of the same weight. For a flat but still non-slip surface, our <a href="/walkways/">Kenway raised perforated treadplate</a> is the perforated alternative.</p>
<p><em>Strength and rigidity per kilogram.</em> Because nothing is removed and the strands are angled, expanded metal is stiffer and stronger for its weight than a perforated sheet of similar open area. Large guards, security fencing, gabions and reinforcing lath all favour it.</p>
<p><em>Cost.</em> Expanded metal uses all of the parent sheet and is quick to produce, so for a given coverage it is usually the cheaper product, particularly in heavier gauges.</p>
<h2>Quick comparison</h2>
<div class="table-wrap"><table><thead><tr><th>Property</th><th>Perforated metal</th><th>Expanded metal</th></tr></thead><tbody>
<tr><td>Surface</td><td>Flat, smooth</td><td>Raised strands (or rolled flat)</td></tr>
<tr><td>Opening accuracy</td><td>Precise, to standard</td><td>Approximate</td></tr>
<tr><td>Open area range (stock)</td><td>7% to 69%</td><td>Typically 40% to 80%</td></tr>
<tr><td>Strength per kg</td><td>Good</td><td>Very good</td></tr>
<tr><td>Cost for coverage</td><td>Moderate</td><td>Low</td></tr>
<tr><td>Pattern choice</td><td>Round, square, slot, custom</td><td>Diamond, hexagonal to order</td></tr>
<tr><td>Cleanability</td><td>Excellent</td><td>Fair (raised), good (flattened)</td></tr>
<tr><td>Finish quality</td><td>Excellent for coating</td><td>Good for galvanising, fair for coating</td></tr>
<tr><td>Typical uses</td><td>Guards, screens, sieves, acoustic and architectural panels, grilles</td><td>Walkways, fencing, large guards, gabions, lath</td></tr>
</tbody></table></div>
<h2>Still not sure?</h2>
<p>Tell us what the panel has to do, its size and where it will be used, and we will suggest the right product from stock. Both can be cut, folded, framed and coated through our <a href="/fabrication-and-coating/">fabrication service</a>.</p>""",
    faqs=[
      ('Is perforated metal stronger than expanded metal?', 'Weight for weight, expanded metal is usually stiffer and stronger because no material is removed and the angled strands act like small beams. Perforated sheet of the same thickness can be stronger in absolute terms at low open areas, and it keeps a flat surface.'),
      ('Which is cheaper, perforated or expanded metal?', 'Expanded metal is generally cheaper per square metre of coverage because it uses the whole parent sheet and is fast to produce. Perforated sheet costs more per sheet but offers precise openings, flat surfaces and more materials.'),
      ('Can I get expanded metal in stainless or aluminium?', 'Yes, to order. Stock expanded metal is mild steel; stainless, aluminium and pre-galvanised expanded mesh are available with a lead time.'),
    ]),
  dict(slug='perforated-metal-prices', short='What affects the price', title='Perforated metal prices: what affects the cost of a sheet',
    summary='Why two sheets that look similar can be priced very differently, and how to specify for the best value.',
    description='What determines perforated metal sheet prices: material, thickness, hole size and open area, sheet size, quantity, cutting, margins, finishing and lead time, with practical tips for getting a better quote.',
    body="""<p>Perforated metal is quoted per sheet or per panel rather than from a fixed price list, because the cost depends on far more than the material. Understanding the factors below will help you read a quote, compare suppliers on a like-for-like basis and, often, save money by adjusting a specification slightly. For a quote on any pattern, <a href="/contact/">send us the details</a>; stock sheets are priced quickly and bespoke work is estimated from your drawing.</p>
<h2>Material</h2>
<p>Material is the largest single factor. Mild steel is the baseline; pre-galvanised steel costs a little more; aluminium is priced per sheet at a similar level to galvanised despite being lighter; stainless steel 304 is several times the price of mild steel and 316 more again; copper is the most expensive. If corrosion resistance is the only reason you are considering stainless, powder-coated galvanised or aluminium sheet may do the job for less.</p>
<h2>Thickness</h2>
<p>Cost rises roughly in proportion to thickness because you are buying metal by weight, but thicker sheet also needs heavier tooling and slower punching. Use the <a href="/guides/open-area-calculator/">weight calculator</a> to see how thickness and open area change the weight of a sheet, and specify the thinnest sheet that does the job, stiffened with folds if necessary.</p>
<h2>Hole size and open area</h2>
<p>Fine patterns with small holes on a close pitch take far more punching strokes per sheet than coarse patterns, so they cost more to make. A 1.5mm hole on a 2.5mm pitch has roughly forty times as many holes per square metre as a 10mm hole on a 15mm pitch. High open areas also produce more scrap. Where the pattern is not critical, choosing a standard stock pattern with a larger hole will usually be cheaper.</p>
<h2>Stock pattern or bespoke</h2>
<p>Stock patterns are perforated in volume and held on the shelf, so they are the most economical option and ship next working day. A non-standard hole size, pitch, margin arrangement or a pattern with blank areas is perforated to order; the cost includes setting up and, for unusual hole sizes, tooling. For a one-off panel it is usually cheaper to adapt a stock pattern than to specify a bespoke one.</p>
<h2>Sheet size and cutting</h2>
<p>Whole stock sheets (2000 × 1000mm and 2500 × 1250mm) give the lowest cost per square metre. Cut pieces are priced on the sheet they are cut from plus the cutting, and the off-cut may or may not be usable, so a panel just over half a sheet can cost nearly as much as a whole one. Where you have flexibility, size panels to divide a stock sheet efficiently.</p>
<h2>Quantity</h2>
<p>Unit prices fall with quantity because setting up, handling and delivery are spread across more sheets. For repeat requirements, ask about scheduled call-off from a bulk order.</p>
<h2>Fabrication and finishing</h2>
<p>Folding, rolling, drilling, edging, powder coating, galvanising, anodising and polishing are each priced on the work involved. A finished panel is more expensive than a flat sheet, but it saves a fabrication step and the risk of a fold landing in the perforated area. See <a href="/fabrication-and-coating/">fabrication and coating</a>.</p>
<h2>Delivery</h2>
<p>Stock sheet is delivered next working day to mainland UK; sheets are large and heavy, so pallet delivery is charged on the consignment rather than per sheet, and consolidating an order into one delivery saves money. Collection from Bristol is available.</p>
<h2>Tips for a better quote</h2>
<p>Choose a stock material and pattern where you can. Specify thickness by what the panel has to do rather than by habit. Size panels to fit stock sheets. Order all the sheets for a job together. Send a drawing so we can quote once, accurately, rather than revising. And tell us your budget or target; there is often a stock alternative that meets it.</p>""",
    faqs=[
      ('How much does a sheet of perforated steel cost?', 'It depends on material, thickness, pattern and sheet size, so we quote each requirement individually. Mild steel stock patterns in 2000 × 1000mm are the most economical; stainless and fine patterns cost more. Contact us with the specification for a same-day quote.'),
      ('Is there a minimum order?', 'No. We supply single sheets and cut pieces as well as production quantities.'),
      ('Do you offer trade or bulk pricing?', 'Yes. Quantity and repeat business are reflected in our quotes, and scheduled call-off can be arranged for ongoing requirements.'),
    ]),
]

PERFORATED_STEEL = dict(
  title='Perforated Steel Sheet: Mild, Galvanised & Stainless from Stock | Kenton',
  description='Perforated steel sheet from a UK manufacturer: mild steel, pre-galvanised and stainless in round, square and slotted hole patterns, 1mm to 30mm holes, 1mm to 5mm thick. Cut to size, next-day delivery from Bristol.',
  h1='Perforated steel sheet',
  lede='Three steels, one catalogue. Choose mild steel for economy and coating, pre-galvanised for exterior use, or stainless for hygiene and corrosion resistance, then pick from round, square and slotted hole patterns held in stock.',
  body="""<h2>Which perforated steel do you need?</h2>
<div class="table-wrap"><table><thead><tr><th>Steel</th><th>Best for</th><th>Corrosion resistance</th><th>Finish</th><th>Relative cost</th></tr></thead><tbody>
<tr><td><a href="/perforated-metal/mild-steel/">Mild steel</a></td><td>Guards, grilles, screens and panels that will be painted or powder coated; general fabrication</td><td>Low uncoated; good once powder coated or galvanised</td><td>Self-colour (uncoated)</td><td>Lowest</td></tr>
<tr><td><a href="/perforated-metal/pre-galvanised-steel/">Pre-galvanised steel</a></td><td>Exterior fencing and screens, agricultural, drainage, plant enclosures</td><td>Good; zinc coating on both faces</td><td>Spangled zinc, can be powder coated</td><td>Low to medium</td></tr>
<tr><td><a href="/perforated-metal/stainless-steel/">Stainless steel</a></td><td>Food, pharmaceutical, marine, architectural and any bare-metal finish</td><td>Excellent (304); superior in marine and chloride environments (316)</td><td>Mill 2B, polished or brushed</td><td>Highest</td></tr>
</tbody></table></div>
<h2>Patterns and sizes</h2>
<p>Perforated steel is punched to the DIN 24041 convention: R for round holes, C for square, LR for slots, with T for a staggered pitch and U for a straight pitch. Across the three steels we stock round hole staggered patterns from R1.1 T2 (1.1mm holes, 27% open) to R30 T40 (30mm holes, 53% open), square pitch patterns for a grid appearance, square hole patterns up to 69% open area, and 5 × 20mm slots for grading and drainage. Standard sheets are 2000 × 1000mm and 2500 × 1250mm (3000 × 1500mm for some patterns) in 0.75mm to 3mm, with mild steel up to 10mm in the coarser patterns, and every pattern can be cut to size, folded, rolled and coated.</p>
<h2>Perforated steel for common jobs</h2>
<p><a href="/applications/machine-guarding/">Machine guarding</a> normally uses 2mm mild steel in R5 T8 or R6 T9, powder coated after folding. <a href="/applications/ventilation-grilles-and-covers/">Ventilation grilles and radiator covers</a> use 1mm to 1.5mm mild steel in fine, high-open-area patterns such as R3 T4. <a href="/applications/balustrade-and-security-infill/">Balustrade and security infill</a> uses 2mm to 3mm galvanised or stainless in R8 T12 or R10 T15. <a href="/applications/screening-sieving-and-drainage/">Screening and sieving</a> uses stainless in small round holes or slots. <a href="/applications/architectural-facades-and-screens/">Facades and screens</a> use galvanised or stainless in larger holes and square-pitch patterns.</p>
<h2>Why buy perforated steel from Kenton</h2>
<p>We manufacture as well as stock, so we can supply a standard sheet tomorrow or a bespoke pattern with your margins and blank areas next week. Every stock pattern has full specifications on its own page, the <a href="/perforated-metal/finder/">perforation finder</a> filters the whole range by hole size, open area and thickness, and our team in Bristol has been advising on perforated steel since 1986. Stock sheets ship next working day across the UK.</p>""",
  faqs=[
    ('What thickness is perforated steel sheet available in?', 'Stock perforated mild steel runs from 0.75mm to 10mm depending on pattern, pre-galvanised 0.75mm to 3mm, and stainless 0.5mm to 3mm. Other thicknesses can be perforated to order.'),
    ('Is perforated steel sheet suitable for outdoor use?', 'Pre-galvanised and stainless steel are. Mild steel should be powder coated or hot-dip galvanised after fabrication if it will be outdoors or in damp conditions.'),
    ('Can perforated steel be cut to size?', 'Yes. We cut, fold, roll and drill perforated steel to your drawing and can leave unperforated margins for fixing and welding.'),
    ('What is the largest perforated steel sheet you stock?', '2500 × 1250mm in most patterns, and 3000 × 1500mm for a number of patterns in each steel. Larger panels are made to order.'),
  ])

BRISTOL = dict(
  title='Perforated Metal & Mesh Supplier in Bristol, Bath & the South West | Kenton',
  description='Perforated metal, expanded metal and wire mesh manufactured and stocked in Bristol. Same-day collection from BS3, next-day delivery across Bath, Gloucester, Swindon, Cardiff, Exeter and the South West.',
  h1='Perforated metal supplier in Bristol and the South West',
  lede='Made and stocked at Novers Hill, Bristol, since 1986. Collect from the works or have stock sheets delivered next working day across the South West and the rest of the UK.',
  body="""<h2>Collection and delivery</h2>
<p>Our works and stock are at 25/26 Barnack Trading Centre, Novers Hill, Bristol BS3 5QE, a few minutes from the A38 and the A4174 ring road, with easy access from the M5 (junction 18 or 19) and the M32. Trade customers, fabricators and one-off buyers can collect by arrangement, or we deliver: stock sheets ordered before the daily cut-off ship on a next-working-day service to Bristol, Bath, Weston-super-Mare, Gloucester, Cheltenham, Swindon, Taunton, Exeter, Cardiff, Newport and the rest of mainland Britain.</p>
<h2>What we stock in Bristol</h2>
<p>115 <a href="/perforated-metal/">perforated metal</a> patterns in mild steel, pre-galvanised steel, stainless steel, aluminium and copper; raised and flattened <a href="/expanded-metal/">expanded metal</a>; <a href="/welded-wire-mesh/">welded wire mesh</a> panels; stainless <a href="/woven-wire-mesh/">woven wire mesh</a> from 2 to 100 mesh; <a href="/walkways/">Kenway perforated walkway treadplate</a>; and <a href="/profile-edging/">profile edging</a>. Everything can be cut, folded, rolled and finished on site or through our <a href="/fabrication-and-coating/">fabrication and coating</a> partners.</p>
<h2>Who we supply</h2>
<p>Sheet-metal fabricators and engineering shops across the South West; architects, contractors and joinery firms on Bristol and Bath projects; food, pharmaceutical and aerospace manufacturers in the region; agricultural and equestrian suppliers; shopfitters, exhibition and set builders; and makers, restorers and homeowners who need a single sheet. Whatever the quantity, the same team quotes and advises.</p>
<h2>Talk to us</h2>
<p>Call <a href="tel:+441179634579">0117 963 4579</a> or email <a href="mailto:holes@kentons.biz">holes@kentons.biz</a> with a drawing, a photo or a description, or use the <a href="/contact/">enquiry form</a>. If you are local, you are welcome to bring a sample in and we will match it.</p>""",
  faqs=[
    ('Can I collect perforated metal from your Bristol works?', 'Yes. Collection from Novers Hill, BS3, is available by arrangement, Monday to Friday. Call ahead so the sheets are ready.'),
    ('Do you deliver to Bath, Gloucester and Cardiff?', 'Yes. Stock orders ship next working day to those areas and to the rest of mainland Britain.'),
    ('Can you cut sheets to size before I collect?', 'Yes. Tell us the sizes when you order and the pieces will be cut, and folded if required, ready for collection.'),
  ])
