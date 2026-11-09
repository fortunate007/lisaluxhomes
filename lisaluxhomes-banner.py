import os
P = 'pb_public/'
if not os.path.isfile(P + 'index.html'):
    raise SystemExit('Run this from your project folder (the one containing pb_public)')

CSS = r'''/* Lisaluxhomes - Zillow-style theme: everything white, blue accents. Loaded after style.css */
:root{--navy:#2a2a33;--ink:#2a2a33;--gold:#006aff;--mut:#5d5d65;--line:#e1e1e5;--rose:#e8455c}
body{background:#fff;color:#2a2a33;font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif}
h1,h2,h3,h4{font-family:Inter,system-ui,sans-serif;font-weight:800;color:#2a2a33;letter-spacing:-.01em}
h2{font-size:26px}a{color:#006aff}.mut{color:#5d5d65}
.pg,.alt,section{background:#fff}

/* top bars + header */
.ann{background:#fff;color:#5d5d65;border-bottom:1px solid #e1e1e5;font-weight:500}.ann a,.ann button{color:#006aff}.ann button:hover{background:none}
.bar{background:#fff;color:#5d5d65;border-bottom:1px solid #e1e1e5}.bar a{color:#5d5d65}.bar i{color:#006aff}
.top{background:#fff;border-bottom:1px solid #e1e1e5;box-shadow:none;backdrop-filter:none}
.logo{font-family:Inter,system-ui,sans-serif;font-weight:800;font-size:22px;color:#006aff}
.links a{color:#2a2a33;font-weight:600;font-size:15px;border-radius:6px}.links a:hover,.links a.on{background:transparent;color:#006aff;box-shadow:inset 0 -3px 0 #006aff}
.links a.agent{background:#fff;color:#006aff;border:1px solid #006aff;border-radius:8px;box-shadow:none;margin-left:10px}.links a.agent:hover{background:#006aff;color:#fff}
#mb{background:#fff;color:#2a2a33;border:1px solid #e1e1e5;box-shadow:none}.links.open{background:#fff}

/* buttons */
button,.btn{background:#006aff;color:#fff;border-radius:8px;box-shadow:none;padding:12px 22px;font-weight:700;letter-spacing:0;transition:background .15s}
button:hover,.btn:hover{background:#0050c8;transform:none;box-shadow:none}
button.s{background:#fff;color:#006aff;border:1px solid #b9d4ff}button.s:hover{background:#eef5ff}
button.d{background:#d32f2f}.bnb{background:#ff385c}.bnb:hover{background:#e0294a}
.tabs button:not(.on){background:#fff;color:#006aff;border:1px solid #b9d4ff}

/* hero: white, headline + search bar, then a running banner of listings */
.hero{display:block;height:auto;margin:0;padding:44px 0 30px;border-radius:0;box-shadow:none;background:#fff;overflow:hidden}
.zh{width:100%;max-width:780px;margin:0 auto;padding:0 20px;text-align:center}
.zh h1{color:#2a2a33;font-size:clamp(28px,4.6vw,48px);font-weight:800;line-height:1.1;margin:0}
.zs{display:flex;margin-top:22px;background:#fff;border:1px solid #c8c8ce;border-radius:10px;overflow:hidden;box-shadow:0 6px 22px rgba(0,0,0,.09)}
.zs input{flex:1;border:0;border-radius:0;padding:18px 20px;font-size:17px;box-shadow:none}.zs input:focus{box-shadow:none}
.zs button{border-radius:0;padding:0 28px;font-size:20px}
.zt{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:16px}
.zt a{color:#006aff;text-decoration:none;font-weight:700;border:1px solid #b9d4ff;background:#fff;padding:8px 18px;border-radius:999px}.zt a:hover{background:#006aff;color:#fff}
.banner{margin-top:34px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.btrack{display:flex;width:max-content;animation:bscroll 60s linear infinite}.banner:hover .btrack{animation-play-state:paused}
@keyframes bscroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.bi{position:relative;flex:0 0 280px;height:210px;margin-right:16px;border-radius:12px;overflow:hidden;cursor:pointer;background:#eef5ff}
.bi img,.bi .ph{width:100%;height:100%;object-fit:cover;display:block;border-radius:0}
.bi:after{content:"";position:absolute;left:0;right:0;bottom:0;height:100px;background:linear-gradient(transparent,rgba(0,0,0,.68))}
.bb{position:absolute;top:10px;left:10px;z-index:2;background:#fff;color:#0b3d91;font-size:11px;font-weight:800;text-transform:uppercase;padding:3px 9px;border-radius:4px}.bb.bz{background:#ff385c;color:#fff}
.bt{position:absolute;left:12px;right:12px;bottom:10px;z-index:2;color:#fff}.bt b{display:block;font-size:20px}.bt span{display:block;font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media(prefers-reduced-motion:reduce){.btrack{animation:none}.banner{overflow-x:auto}}
.intro{padding:36px 0 26px}.intro h1{font-size:30px}

/* listing cards: price first, then details, like Zillow */
.grid{gap:22px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.card{background:#fff;border:1px solid #ececf0;border-radius:10px;box-shadow:none;overflow:hidden}
.card:hover{transform:none;box-shadow:0 6px 22px rgba(0,0,0,.13);border-color:#ececf0}
.card img,.ph{height:200px}.card:hover img{transform:scale(1.03)}.ph{background:linear-gradient(135deg,#eaf2ff,#f6f9ff);color:#b9cffa}
.card .b{display:flex;flex-direction:column;gap:3px;padding:14px}
.card .b>div:first-child{order:-4}.price{order:-3;font-size:24px;font-weight:800;color:#2a2a33}.price small{font-size:14px;font-weight:500;color:#5d5d65}.old{color:#767680}
.card .b>.mut{order:-2;font-size:14px;color:#2a2a33}.card h3{order:-1;font-size:15px;font-weight:600;color:#5d5d65;margin:0}
.d{order:0;color:#5d5d65;font-size:13px}.act{order:1;margin-top:10px}
.tag{background:#eef5ff;color:#0b3d91;border:0;border-radius:4px;font-weight:700}.tag.r{background:#fdecec;color:#c0392b}
.rib{background:#e8455c;border-radius:4px;box-shadow:none}
.cat{padding:30px 16px}.cat i{color:#006aff;background:none;-webkit-text-fill-color:#006aff}.ico{background:#eef5ff;color:#006aff}

/* tabs, strips, forms */
.src{background:#fff;border:1px solid #e1e1e5;border-radius:10px;box-shadow:none}.src.on{background:#eef5ff;color:#0b3d91;border-color:#006aff}.src.on span{color:#5d5d65}.src:hover{background:#f7faff}.src .n{color:#006aff}
.bnbstrip{background:#fff;border:1px solid #e1e1e5;border-radius:12px;box-shadow:none}
.cta{background:#eef5ff;border:0;border-radius:12px;box-shadow:none}.cta p{color:#3d4a66}
input,select,textarea{background:#fff;border:1px solid #c8c8ce;border-radius:8px}
input:focus,select:focus,textarea:focus{border-color:#006aff;box-shadow:0 0 0 3px rgba(0,106,255,.18)}
.faq details{background:#fff;border:1px solid #e1e1e5;border-radius:10px;box-shadow:none}.faq details[open]{border-color:#006aff}
dialog{border-radius:14px}dialog::backdrop{background:rgba(0,0,0,.5)}
.soc a{background:#fff;border:1px solid #e1e1e5;color:#006aff}.soc a:hover{background:#006aff;color:#fff;border-color:#006aff}
table{box-shadow:none;border:1px solid #e1e1e5}th{background:#f5f8ff}

/* footer: white, link columns */
footer{background:#fff;color:#5d5d65;border-top:1px solid #e1e1e5;margin-top:56px}
footer h4{color:#2a2a33;font-size:16px}footer a{color:#006aff}.about p{color:#5d5d65}.copy{border-top:1px solid #e1e1e5;color:#767680}
@media(max-width:700px){.hero{padding:30px 0 20px}.bi{flex-basis:230px;height:180px}.zs input{padding:16px;font-size:16px}h2{font-size:22px}}
'''
open(P + 'theme.css', 'w', encoding='utf-8').write(CSS)
print('wrote theme.css')

HERO = ('<div class="hero"><div class="zh"><h1>Find homes, rentals &amp; Airbnb stays in Nairobi</h1>'
 '<form class="zs" onsubmit="zsearch(event)"><input name="q" placeholder="Enter an estate or keyword, e.g. Kilimani, Karen, pool"><button aria-label="Search">&#128269;</button></form>'
 '<div class="zt"><a href="#listings" onclick="cat(\'sale\');return false">Buy</a><a href="#listings" onclick="cat(\'rent\');return false">Rent</a><a href="#airbnb">Airbnb stays</a><a href="#contact">Sell</a></div></div>'
 '<div id="bn" class="banner" aria-label="Listings"></div><div id="hs" style="display:none"></div></div>')

ZJS = r'''function zsearch(e){e.preventDefault();F={q:String(new FormData(e.target).get('q')||'')};SRC='all';pg=1;location.hash='#listings';render()}
function banner(){const el=$('bn');if(!el)return;let L=ALL.filter(l=>l.status!=='hidden');if(!L.length){el.innerHTML='';return}
 for(let i=L.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[L[i],L[j]]=[L[j],L[i]]}
 while(L.length<10)L=L.concat(L);
 const name={airbnb:'Airbnb stay',sale:'For sale',rent:'For rent',land:'Land',commercial:'Commercial'};
 const card=l=>`<div class="bi" data-i="${l.id}" onclick="det(this.dataset.i)">${img(l)?`<img src="${esc(img(l))}" alt="${esc(l.title)}" loading="lazy">`:'<div class="ph"><i class="fa-solid fa-house"></i></div>'}<span class="bb${l.type==='airbnb'?' bz':''}">${name[l.type]||esc(l.type)}</span><div class="bt"><b>${money(l.price)}${l.type==='airbnb'?' / night':''}</b><span>${esc(l.title)} &middot; ${esc(l.location)}</span></div></div>`;
 const row=L.map(card).join('');el.innerHTML=`<div class="btrack" style="animation-duration:${Math.max(30,L.length*5)}s">${row}${row}</div>`}
function doSearch(e){'''

s = open(P + 'index.html', encoding='utf-8').read()
a = s.find('<div class="hero">'); b = s.find('<div class="w"><div class="intro">')
if a < 0 or b < 0:
    print('MISS index.html | hero block not found')
else:
    s = s[:a] + HERO + '\n' + s[b:]; print('ok   index.html | hero replaced with search + running banner')
s = s.replace('function zsearch(e){e.preventDefault();F={q:String(new FormData(e.target).get(\'q\')||\'\')};SRC=\'all\';pg=1;location.hash=\'#listings\';render()}\nfunction doSearch(e){', 'function doSearch(e){')
if 'function banner()' not in s:
    if 'function doSearch(e){' in s:
        s = s.replace('function doSearch(e){', ZJS, 1); print('ok   index.html | banner code added')
    else:
        print('MISS index.html | doSearch not found')
if 'banner()}' not in s:
    if 'extras();render();hero()}' in s:
        s = s.replace('extras();render();hero()}', 'extras();render();hero();banner()}', 1); print('ok   index.html | banner starts after listings load')
    else:
        print('MISS index.html | load hook not found')
if 'theme.css' not in s:
    s = s.replace('<link rel="stylesheet" href="/style.css">', '<link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/theme.css">', 1); print('ok   index.html | theme linked')
open(P + 'index.html', 'w', encoding='utf-8').write(s)
if os.path.isfile(P + 'agent.html'):
    t = open(P + 'agent.html', encoding='utf-8').read()
    if 'theme.css' not in t:
        t = t.replace('<link rel="stylesheet" href="/style.css">', '<link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/theme.css">', 1)
        open(P + 'agent.html', 'w', encoding='utf-8').write(t); print('ok   agent.html | theme linked')
print('\nDone. Reload with Ctrl+Shift+R.')
