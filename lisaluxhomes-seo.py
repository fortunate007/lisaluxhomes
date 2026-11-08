import os
P = 'pb_public/'
if not os.path.isfile(P + 'index.html'):
    raise SystemExit('Run this from your project folder (the one containing pb_public)')

def sub(f, pairs):
    s = open(f, encoding='utf-8').read()
    for a, b in pairs:
        if a in s:
            s = s.replace(a, b); print('ok  ', f, '|', a[:45])
        else:
            print('MISS', f, '|', a[:45])
    open(f, 'w', encoding='utf-8').write(s)

AREAS = 'Muthaiga, Kileleshwa, Kilimani, Runda, Lavington, Kitisuru, Karen, Westlands'
HEAD = r'''<meta name="description" content="Lisaluxhomes: homes for sale, houses to rent, land and Airbnb stays in Muthaiga, Kileleshwa, Kilimani, Runda, Lavington, Kitisuru, Karen and Westlands, Nairobi, Kenya. Verified listings, prices in KSh.">
<meta name="keywords" content="real estate Nairobi, houses for sale Nairobi, apartments for rent Kilimani, Airbnb Nairobi, Karen, Runda, Muthaiga, Kileleshwa, Lavington, Westlands, Kitisuru">
<meta name="robots" content="index,follow"><meta property="og:type" content="website"><meta property="og:locale" content="en_KE">
<meta property="og:title" content="Lisaluxhomes | Homes for Sale, Rent &amp; Airbnb Stays in Nairobi"><meta property="og:description" content="Verified homes, land and Airbnb stays in Nairobi's prime estates. All prices in Kenyan shillings.">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"RealEstateAgent","name":"Lisaluxhomes","description":"Homes for sale, rentals, land and Airbnb stays in Nairobi's prime estates, with verified listings priced in Kenyan shillings.","telephone":"+254722526996","email":"lisaluxhomes@gmail.com","address":{"@type":"PostalAddress","addressLocality":"Nairobi","addressCountry":"KE"},"areaServed":["Muthaiga","Kileleshwa","Kilimani","Runda","Lavington","Kitisuru","Karen","Westlands"],"priceRange":"KSh"}</script>'''

FOOT_OLD = '<footer><div class="w fg"><div><h4 id="fn"></h4><p id="ft"></p></div><div><h4>Quick links</h4><p id="fl"></p></div><div><h4>Contact</h4><p><a id="fp"></a><br><a id="fe"></a></p></div></div>'
FOOT_NEW = ('<footer><div class="w fg"><div class="about"><h4 id="fn"></h4><p id="ft"></p><p>Lisaluxhomes is a Nairobi real estate company helping buyers, tenants, investors and travellers find homes for sale, houses to rent, land, commercial property and Airbnb stays in Kenya\'s most sought-after estates: '
 + AREAS + ' and more. Every listing is checked by our team and every price is shown in Kenyan shillings (KSh).</p></div>'
 '<div><h4>Quick links</h4><p id="fl"></p></div>'
 '<div><h4>Areas we serve</h4><p>Muthaiga &middot; Kileleshwa &middot; Kilimani &middot; Runda &middot; Lavington &middot; Kitisuru &middot; Karen &middot; Westlands &middot; Gigiri &middot; Rosslyn &middot; Spring Valley &middot; Loresho &middot; Riverside &middot; Nyari &middot; Parklands &middot; Upper Hill &middot; Langata</p></div>'
 '<div><h4>Contact</h4><p><a id="fp"></a><br><a id="fe"></a></p></div></div>')

sub(P + 'index.html', [
 ('<title>Lisaluxhomes | Homes, Land &amp; Airbnb Stays in Kenya</title>', '<title>Lisaluxhomes | Homes for Sale, Rent &amp; Airbnb Stays in Nairobi, Kenya</title>'),
 ('<meta name="description" content="Homes for sale, rentals, land and Airbnb stays in Nairobi\'s prime estates. All prices in Kenyan shillings.">', HEAD),
 ("' | Homes, Land & Airbnb Stays in Kenya'", "' | Homes for Sale, Rent & Airbnb Stays in Nairobi, Kenya'"),
 ('<div class="hd" style="margin-top:50px"><h2>Airbnb picks</h2><a href="#airbnb">All stays &rarr;</a></div><div id="hbgrid" class="grid"></div>',
  '<div class="bnbstrip"><div><h2>Airbnb stays</h2><p class="mut">Book short stays by the night in Nairobi\'s prime estates.</p></div><a class="btn bnb" href="#airbnb">See available stays</a></div><div id="hbgrid" style="display:none"></div>'),
 ("function route(){const h=(location.hash||'#home').slice(1),id=PAGES.some(p=>p[0]===h)?h:'home';", "function route(){const h=(location.hash||'#home').slice(1),id=PAGES.some(p=>p[0]===h)?h:'home';document.body.dataset.pg=id;"),
 (FOOT_OLD, FOOT_NEW),
])

if os.path.isfile(P + 'agent.html'):
    s = open(P + 'agent.html', encoding='utf-8').read()
    if 'noindex' not in s:
        sub(P + 'agent.html', [('<title>Agent Portal</title>', '<title>Agent Portal</title><meta name="robots" content="noindex,nofollow">')])

open(P + 'style.css', 'a', encoding='utf-8').write('''
/* homepage: lighter */
#home .stats{display:none}body[data-pg=home] .cta{display:none}
.bnbstrip{margin-top:46px;padding:26px 28px;border-radius:18px;background:#fff;border:1px solid var(--line);display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}.bnbstrip h2{margin:0;font-size:26px}.bnbstrip p{margin:2px 0 0}
.about p{color:#d9d2e0;font-size:14px}.fg{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}@media(min-width:900px){.fg{grid-template-columns:1.6fr 1fr 1.3fr 1fr}}
''')

host = 'https://www.yourdomain.co.ke'
open(P + 'robots.txt', 'w').write('User-agent: *\nAllow: /\nDisallow: /_/\nDisallow: /agent.html\nSitemap: ' + host + '/sitemap.xml\n')
open(P + 'sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + host + '/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url></urlset>\n')
print('wrote robots.txt and sitemap.xml (replace', host, 'with your real domain)')
print('\nDone. Reload the site with Ctrl+Shift+R.')
