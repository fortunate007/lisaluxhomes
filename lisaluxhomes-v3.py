import os
P = 'pb_public/'
if not os.path.isdir(P):
    raise SystemExit('Run this from your project folder (the one containing pb_public)')
def w(f, s): open(f, 'w', encoding='utf-8').write(s); print('wrote', f)

w('pb_migrations/1760000004_airbnb_samples.js', r'''migrate((db) => {
  const dao = new Dao(db);
  const c = dao.findCollectionByNameOrId("listings");
  // sample listings were entered as USD-style numbers: convert to KSh (x130)
  try { dao.db().newQuery("UPDATE listings SET price = price * 130, old_price = old_price * 130 WHERE type != 'airbnb'").execute(); } catch (e) { console.log("price conversion skipped", e); }
  const mk = (title, loc, price, size, bd, ba, desc, feat) => ({ title, type: "airbnb", status: "available", location: loc, price, size, bedrooms: bd, bathrooms: ba, description: desc, featured: feat, offer: false });
  [
    mk("Kilimani Skyline Studio", "Kilimani, Nairobi", 8500, 45, 1, 1, "Bright studio with city views, fast Wi-Fi, a fully equipped kitchenette and secure parking.", true),
    mk("Karen Garden Cottage", "Karen, Nairobi", 14000, 90, 2, 2, "Quiet cottage in a leafy compound with a private garden, fireplace and breakfast nook.", true),
    mk("Westlands Executive Apartment", "Westlands, Nairobi", 11500, 85, 2, 2, "Modern two-bedroom near restaurants and offices, with a gym, pool and 24/7 security.", false),
    mk("Runda Villa Retreat", "Runda, Nairobi", 38000, 320, 4, 4, "Spacious family villa with a pool, landscaped garden, staff quarters and ample parking.", true),
    mk("Muthaiga Heritage Suite", "Muthaiga, Nairobi", 22000, 120, 2, 2, "Elegant suite in a prestigious estate, with a private terrace and a dedicated workspace.", false),
    mk("Lavington Cosy Loft", "Lavington, Nairobi", 9500, 60, 1, 1, "Stylish loft with a king bed, a balcony and a calm, walkable neighbourhood.", false),
  ].forEach((r) => { try { const rec = new Record(c); Object.keys(r).forEach((k) => rec.set(k, r[k])); dao.saveRecord(rec); } catch (e) { console.log("seed skipped", e); } });
  return null;
}, (db) => {
  const dao = new Dao(db);
  try { dao.db().newQuery("DELETE FROM listings WHERE type = 'airbnb'").execute(); } catch (e) {}
  return null;
});
''')

w(P + 'config.js', r'''// Edit these values, save, refresh.
window.SITE = {
  name: "Lisaluxhomes",
  tagline: "Homes, land and Airbnb stays across Kenya's finest estates.",
  phone: "+254 722 526996",
  email: "lisaluxhomes@gmail.com",
  address: "Operations: Muthaiga, Kileleshwa, Kilimani, Runda, Lavington, Kitisuru, Karen, Westlands and other prime Nairobi estates",
  areas: ["Muthaiga","Kileleshwa","Kilimani","Runda","Lavington","Kitisuru","Karen","Westlands"],
  hours: ["Monday to Friday: 9am - 5pm", "Saturday: 9am - 1pm"],
  stats: [{ n: "10+", l: "Years of experience" }, { n: "500+", l: "Properties handled" }, { n: "98%", l: "Client satisfaction" }, { n: "24/7", l: "Enquiry support" }],
  services: [
    { i: "house-circle-check", t: "Buying", x: "Shortlisting, viewings, negotiation and title checks." },
    { i: "key", t: "Renting", x: "Verified rentals, tenant screening and clear leases." },
    { i: "tags", t: "Selling & Letting", x: "Professional listing, marketing and valuation." },
    { i: "screwdriver-wrench", t: "Property Management", x: "Rent collection, maintenance and reporting." },
    { i: "map-location-dot", t: "Land & Development", x: "Plot sourcing and development support." },
    { i: "chart-line", t: "Valuation & Advice", x: "Honest valuations and investment guidance." }
  ],
  why: [
    { i: "shield-halved", t: "Verified listings", x: "Every property and its documents are checked before it goes online." },
    { i: "tags", t: "Transparent pricing", x: "Clear prices in Kenyan shillings and honest advice, with no surprises." },
    { i: "location-dot", t: "Local expertise", x: "Deep knowledge of Nairobi's prime estates, values and market trends." },
    { i: "file-signature", t: "Legal & title support", x: "Guidance on title checks, agreements and paperwork from start to finish." },
    { i: "bolt", t: "Fast response", x: "Quick replies to enquiries and flexible viewing times that suit you." },
    { i: "handshake", t: "After-sale care", x: "We stay in touch after handover to help with anything that comes up." }
  ],
  faqs: [
    { q: "How do I book a viewing?", a: "Click Enquire on any listing or use the contact form with your preferred date and time. We will confirm quickly." },
    { q: "Are your listings verified?", a: "Yes. We check each property and its documents before it is published, and keep sold or rented listings up to date." },
    { q: "How can I be sure the title is genuine?", a: "We help you run official title searches and review documents with you. Involve a qualified lawyer before paying any deposit." },
    { q: "Do you charge fees to buyers or tenants?", a: "Please contact us for the current fee structure. We explain every cost in writing before you commit." },
    { q: "Can I get financing for a purchase?", a: "Many buyers use a mortgage or financing plan. We can point you to lenders and explain the documents they usually ask for." },
    { q: "How do Airbnb stays work?", a: "Choose a stay, then book directly on Airbnb using the Book on Airbnb button, or enquire with us for longer stays." },
    { q: "How do the special offers work?", a: "Offers are limited-time discounts or perks on selected properties. The note on each listing explains the terms." },
    { q: "Can I list my property with you?", a: "Absolutely. Use the contact page and our team will arrange a free valuation and listing." }
  ],
  social: [
    { name: "Facebook", icon: "facebook-f", url: "https://facebook.com/yourpage" },
    { name: "Instagram", icon: "instagram", url: "https://instagram.com/yourpage" },
    { name: "X", icon: "x-twitter", url: "https://x.com/yourpage" },
    { name: "WhatsApp", icon: "whatsapp", url: "https://wa.me/254722526996" }
  ]
};
''')

w(P + 'index.html', r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lisaluxhomes | Homes, Land &amp; Airbnb Stays in Kenya</title>
<meta name="description" content="Homes for sale, rentals, land and Airbnb stays in Nairobi's prime estates. All prices in Kenyan shillings.">
<link rel="icon" href="/lisaluxhomes-icon.svg">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link rel="stylesheet" href="/style.css"><script src="/config.js"></script></head><body>
<div class="ann" id="ann"><span>Limited-time offers: up to 10% off selected properties</span> <a href="#offers">View offers &rarr;</a><button id="annx" aria-label="Close banner" onclick="$('ann').style.display='none'">&times;</button></div>
<div class="bar"><div class="w"><span><i class="fa-solid fa-location-dot"></i><span id="ba"></span></span><a id="be"></a><a id="bp"></a></div></div>
<header class="top"><a class="logo" href="#home"><img src="/lisaluxhomes-icon.svg" alt=""><span id="brand"></span></a><nav class="links" id="nav"></nav><button id="mb" aria-label="Menu" onclick="$('nav').classList.toggle('open')">&#9776;</button></header>

<section class="pg" id="home"><div class="hero"><div id="hs"></div><div class="hbtns"><button onclick="$('sd').showModal()"><i class="fa-solid fa-magnifying-glass"></i> Search properties</button><a class="btn bnb" href="#airbnb"><i class="fa-brands fa-airbnb"></i> Airbnb stays</a><a class="btn ghost" href="#listings">Browse listings</a></div></div>
<div class="w"><div class="intro"><h1>Find the property that fits your life</h1><p class="mut" id="tag"></p></div><div class="stats" id="stats"></div><div class="hd"><h2>Featured properties</h2><a href="#listings">View all &rarr;</a></div><div id="fgrid" class="grid"></div>
<div class="hd" style="margin-top:50px"><h2>Airbnb picks</h2><a href="#airbnb">All stays &rarr;</a></div><div id="hbgrid" class="grid"></div></div></section>

<section class="pg" id="listings"><div class="w"><div class="hd"><div><h2>Listings</h2><p class="mut" id="count">Loading…</p></div><div class="tools"><a class="btn" href="#contact">Send inquiry</a><button onclick="$('sd').showModal()"><i class="fa-solid fa-magnifying-glass"></i> Search</button><button class="s" id="clr" onclick="clr()" style="display:none">Clear filters</button><button class="s" onclick="view='lg';render()">Large</button><button class="s" onclick="view='sm';render()">Compact</button><button class="s" onclick="view='list';render()">List</button><select onchange="per=+this.value;pg=1;render()"><option value="9">9 per page</option><option value="18">18 per page</option><option value="36">36 per page</option></select></div></div>
<div class="srcs"><button class="src on" data-s="all" onclick="setSrc('all')"><b>All properties</b><span>Sale, rent, land &amp; stays</span><i class="n"></i></button><button class="src" data-s="property" onclick="setSrc('property')"><b>Buy &amp; rent</b><span>Homes, land, commercial</span><i class="n"></i></button><button class="src" data-s="airbnb" onclick="setSrc('airbnb')"><b>Airbnb stays</b><span>Short stays by the night</span><i class="n"></i></button></div><p class="mut">Browse by area</p><div class="chips" id="locs"></div>
<div id="grid" class="grid"></div><div id="pager" class="pager"></div></div></section>

<section class="pg" id="airbnb"><div class="w"><div class="hd"><div><h2><i class="fa-brands fa-airbnb" style="color:#ff385c"></i> Airbnb stays</h2><p class="mut">Short stays by the night in Nairobi's prime estates. Prices in KSh per night.</p></div></div><div id="bgrid" class="grid"></div></div></section>

<section class="pg" id="offers"><div class="w"><h2><i class="fa-solid fa-fire" style="color:#e8455c"></i> Special offers</h2><p class="mut">Limited-time deals on selected properties.</p><div id="ogrid" class="grid"></div></div></section>

<section class="pg" id="categories"><div class="w"><h2>Browse by category</h2><p class="mut">Tap a category to see its listings.</p><div class="grid cats">
<div class="card cat" onclick="cat('sale')"><i class="fa-solid fa-house"></i>For Sale</div><div class="card cat" onclick="cat('rent')"><i class="fa-solid fa-key"></i>For Rent</div><div class="card cat" onclick="cat('land')"><i class="fa-solid fa-tree"></i>Land</div>
<div class="card cat" onclick="cat('commercial')"><i class="fa-solid fa-building"></i>Commercial</div><div class="card cat" onclick="location.hash='#airbnb'"><i class="fa-brands fa-airbnb"></i>Airbnb Stays</div></div></div></section>

<section class="pg" id="services"><div class="w"><h2>Our services</h2><p class="mut">From first search to keys in hand.</p><div class="grid" id="svc"></div></div></section>

<section class="pg" id="about"><div class="w"><h2>About us</h2><div class="card b" style="max-width:820px"><p>Lisaluxhomes is a Nairobi real estate team focused on honest advice and verified listings. We guide you through every step of buying, renting, investing or booking a stay in Muthaiga, Kileleshwa, Kilimani, Runda, Lavington, Kitisuru, Karen, Westlands and other prime estates.</p><p>Every price you see is in Kenyan shillings, and every listing is checked by our team before it goes online.</p><a class="btn" href="#contact">Talk to us</a></div><h2 style="margin-top:44px">What clients say</h2><p class="mut">Sample testimonials. Replace with real ones.</p><div class="grid"><div class="card b quote"><i class="fa-solid fa-quote-left"></i>Found our family home in two weeks. Smooth and honest.<p class="mut">&mdash; Happy buyer</p></div><div class="card b quote"><i class="fa-solid fa-quote-left"></i>They manage my rentals and the income has been steady.<p class="mut">&mdash; Property owner</p></div><div class="card b quote"><i class="fa-solid fa-quote-left"></i>Clear advice on land titles saved me from a bad deal.<p class="mut">&mdash; Investor</p></div></div></div></section>

<section class="pg" id="why"><div class="w"><h2>Why us?</h2><p class="mut">The reasons clients trust us with their biggest decisions.</p><div class="stats" id="stats2"></div><div class="grid" id="whyg"></div></div></section>

<section class="pg" id="faq"><div class="w"><h2>Frequently asked questions</h2><p class="mut">Can't find yours? <a href="#contact">Ask us</a>.</p><div class="faq" id="faqs"></div></div></section>

<section class="pg" id="contact"><div class="w"><h2>Contact us</h2><p class="mut">Tell us what you are looking for.</p><div class="two"><div class="card b"><form class="f" onsubmit="send(event)"><input name="name" placeholder="Full name" required><input name="email" type="email" placeholder="Email address"><input name="phone" placeholder="Phone number">
<select name="timeline"><option>Immediately</option><option>1-3 months</option><option>Just inquiring</option></select><select name="subject" id="sub"><option>Property inquiry</option><option>Airbnb booking</option><option>Selling or letting</option><option>Financing</option><option>General question</option></select>
<textarea name="message" id="msg" placeholder="Message / requirements" style="grid-column:1/-1"></textarea><button>Send message</button></form></div>
<div class="card b"><h3>Get in touch</h3><p><i class="fa-solid fa-phone"></i> <a id="cp"></a><br><i class="fa-solid fa-envelope"></i> <a id="ce"></a><br><i class="fa-solid fa-location-dot"></i> <span id="ca"></span></p><h3>Open hours</h3><p id="ch"></p><div class="soc" id="soc"></div></div></div></div></section>

<div class="w"><div class="cta"><div><h2>Selling or letting your property?</h2><p>Get a free, no-obligation valuation from our team.</p></div><a class="btn" href="#contact">Get a free valuation</a></div></div>
<a class="wa" href="https://wa.me/254722526996" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<footer><div class="w fg"><div><h4 id="fn"></h4><p id="ft"></p></div><div><h4>Quick links</h4><p id="fl"></p></div><div><h4>Contact</h4><p><a id="fp"></a><br><a id="fe"></a></p></div></div><div class="copy">&copy; <span id="yr"></span> <span id="fn2"></span>. All rights reserved.</div></footer>

<dialog id="sd"><form id="sf" class="b" onsubmit="doSearch(event)"><h3>Search properties</h3><div class="f">
<input name="q" placeholder="Keyword e.g. garden, pool"><select name="loc" id="loc"><option value="">Any area</option></select>
<select name="type"><option value="">All types</option><option value="sale">For sale</option><option value="rent">For rent</option><option value="land">Land</option><option value="commercial">Commercial</option><option value="airbnb">Airbnb stays</option></select>
<select name="beds"><option value="">Any bedrooms</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select>
<input name="min" type="number" min="0" placeholder="Min price (KSh)"><input name="max" type="number" min="0" placeholder="Max price (KSh)"><input name="minSize" type="number" min="0" placeholder="Min size (m²)"><input name="maxSize" type="number" min="0" placeholder="Max size (m²)"><label class="chk"><input type="checkbox" name="offer"> Offers only</label></div>
<div class="act"><button><i class="fa-solid fa-magnifying-glass"></i> Search</button><button type="button" class="s" onclick="clr();$('sd').close()">Reset</button><button type="button" class="s" onclick="$('sd').close()">Close</button></div></form></dialog>
<dialog id="dlg"><div id="dm"></div></dialog>

<script>
const API='/api/collections/',S=window.SITE||{},$=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const money=n=>'KSh '+Number(n||0).toLocaleString('en-KE'),safe=u=>/^(#|https?:|mailto:|tel:)/.test(u||'')?u:'#';
const img=l=>l.image?`/api/files/${l.collectionId}/${l.id}/${encodeURIComponent(l.image)}`:'';
const PAGES=[['home','Home'],['listings','Listings'],['airbnb','Airbnb Stays'],['offers','Offers'],['categories','Categories'],['services','Services'],['about','About'],['why','Why us'],['faq','FAQ'],['contact','Contact']];
let ALL=[],F={},SRC='all',view='lg',pg=1,per=9,cur=null,hi=0,timer;
function bookBtn(l){return l.type==='airbnb'&&l.airbnb_url?`<a class="btn bnb" href="${esc(safe(l.airbnb_url))}" target="_blank" rel="noopener">Book on Airbnb</a>`:''}
function card(l){const im=img(l),bn=l.type==='airbnb',off=l.offer&&l.old_price>l.price;
 return `<article class="card">${off?`<span class="rib">${Math.round((1-l.price/l.old_price)*100)}% OFF</span>`:''}${im?`<img src="${esc(im)}" alt="${esc(l.title)}" loading="lazy">`:'<div class="ph"><i class="fa-solid fa-house"></i></div>'}<div class="b"><div><span class="tag">${esc(l.type)}</span>${l.status!=='available'?`<span class="tag r">${esc(l.status)}</span>`:''}</div>
 <h3>${esc(l.title)}</h3><div class="mut"><i class="fa-solid fa-location-dot"></i> ${esc(l.location)}${l.size?` · ${l.size} m²`:''}${l.bedrooms?` · ${l.bedrooms} bd`:''}${l.bathrooms?` · ${l.bathrooms} ba`:''}</div><p class="d">${esc(l.description)}</p>
 <div class="price">${money(l.price)}${bn?'<small> / night</small>':''}${off?`<span class="old">${money(l.old_price)}</span>`:''}</div>${off&&l.offer_note?`<div class="mut"><i class="fa-solid fa-gift"></i> ${esc(l.offer_note)}</div>`:''}
 <div class="act"><button data-i="${l.id}" onclick="det(this.dataset.i)">View details</button>${bookBtn(l)}</div></div></article>`}
function list(){const g=k=>String(F[k]||'').toLowerCase();return ALL.filter(l=>(SRC==='all'||(SRC==='airbnb')===(l.type==='airbnb'))&&(!g('q')||[l.title,l.description,l.location].join(' ').toLowerCase().includes(g('q')))&&(!g('loc')||String(l.location||'').toLowerCase().includes(g('loc')))&&(!g('type')||l.type===g('type'))&&(!F.min||l.price>=+F.min)&&(!F.max||l.price<=+F.max)&&(!F.beds||l.bedrooms>=+F.beds)&&(!F.minSize||l.size>=+F.minSize)&&(!F.maxSize||l.size<=+F.maxSize)&&(!F.offer||l.offer))}
function render(){const L=list(),n=Math.max(1,Math.ceil(L.length/per));pg=Math.min(pg,n);$('grid').className='grid '+view;document.querySelectorAll('.src').forEach(b=>b.classList.toggle('on',b.dataset.s===SRC));
 $('count').textContent=L.length+' propert'+(L.length===1?'y':'ies')+' found';$('grid').innerHTML=L.slice((pg-1)*per,pg*per).map(card).join('')||'<p>No properties match your search.</p>';
 $('pager').innerHTML=n<2?'':Array.from({length:n},(_,i)=>`<button class="${i+1===pg?'':'s'}" onclick="pg=${i+1};render();scrollTo(0,0)">${i+1}</button>`).join('');$('clr').style.display=Object.values(F).some(Boolean)?'':'none'}
function fill(){const A=ALL.filter(l=>l.type==='airbnb'&&l.status==='available'),P=ALL.filter(l=>l.type!=='airbnb'),G=(a,m)=>a.map(card).join('')||`<p>${m}</p>`;
 $('fgrid').innerHTML=G(P.filter(l=>l.featured).concat(P).filter((l,i,a)=>a.indexOf(l)===i).slice(0,3),'No properties yet.');$('hbgrid').innerHTML=G(A.slice(0,3),'Airbnb stays coming soon.');
 $('bgrid').innerHTML=G(A,'Airbnb stays coming soon.');$('ogrid').innerHTML=G(ALL.filter(l=>l.offer&&l.status==='available'),'No offers right now. Check back soon.');extras();render();hero()}
function setSrc(s){SRC=s;pg=1;render()}
function area(a){F={...F,loc:a};SRC='all';pg=1;render()}
function extras(){const n=ALL.filter(l=>l.type==='airbnb').length;document.querySelectorAll('.src').forEach(b=>{const s=b.dataset.s;b.querySelector('.n').textContent=s==='all'?ALL.length:s==='airbnb'?n:ALL.length-n});
 $('locs').innerHTML=(S.areas||[]).map(a=>`<button class="s" data-a="${esc(a)}" onclick="area(this.dataset.a)">${esc(a)}</button>`).join('');$('stats2').innerHTML=$('stats').innerHTML}
function doSearch(e){e.preventDefault();SRC='all';F=Object.fromEntries(new FormData(e.target));pg=1;$('sd').close();location.hash='#listings';render()}
function clr(){F={};SRC='all';$('sf').reset();pg=1;render()}
function cat(t){F={type:t};SRC='all';pg=1;location.hash='#listings';render()}
function hero(){const H=ALL.filter(l=>l.featured&&l.status==='available').slice(0,4);
 $('hs').innerHTML=(H.length?H:[{}]).map((l,i)=>`<div class="hs${i?'':' on'}" style="background-image:url('${esc(l.id?img(l):'/hero1.jpg')}')"><div class="in"><span class="lab">${l.id?(l.type==='airbnb'?'Featured Airbnb Stay':'Featured Property'):'Welcome'}</span><h2>${esc(l.title||'Find a home you will love in Kenya')}</h2>
 <p>${esc(l.id?(l.description||'').slice(0,140):S.tagline)}</p>${l.id?`<button data-i="${l.id}" onclick="det(this.dataset.i)">View details</button>`:''}</div></div>`).join('');
 clearInterval(timer);const s=document.querySelectorAll('.hs');if(s.length>1)timer=setInterval(()=>{s[hi].classList.remove('on');hi=(hi+1)%s.length;s[hi].classList.add('on')},6000)}
function det(id){const l=ALL.find(x=>x.id===id);if(!l)return;cur=l;const im=img(l);
 $('dm').innerHTML=`<button class="x" onclick="$('dlg').close()" aria-label="Close">×</button>${im?`<img src="${esc(im)}" alt="">`:''}<div class="b"><h3>${esc(l.title)}</h3><div class="price">${money(l.price)}${l.type==='airbnb'?'<small> / night</small>':''}</div>
 <p class="mut">${esc(l.location)}${l.size?` · ${l.size} m²`:''}${l.bedrooms?` · ${l.bedrooms} bd`:''}${l.bathrooms?` · ${l.bathrooms} ba`:''}</p><p>${esc(l.description)}</p><div class="act"><button onclick="enq()">Enquire</button>${bookBtn(l)}</div></div>`;$('dlg').showModal()}
function enq(){$('dlg').close();$('sub').value=cur.type==='airbnb'?'Airbnb booking':'Property inquiry';$('msg').value='I am interested in: '+cur.title+' ('+money(cur.price)+')';location.hash='#contact'}
async function send(e){e.preventDefault();const f=Object.fromEntries(new FormData(e.target)),b={name:f.name,email:f.email,phone:f.phone,message:'['+f.subject+' | '+f.timeline+'] '+f.message};
 if(cur&&String(f.message).includes('I am interested in: '+cur.title))b.listing=cur.id;
 const r=await fetch(API+'inquiries/records',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});
 if(r.ok){alert('Thank you! We will be in touch.');e.target.reset()}else alert('Could not send. Please add your name and an email or phone.')}
function route(){const h=(location.hash||'#home').slice(1),id=PAGES.some(p=>p[0]===h)?h:'home';
 document.querySelectorAll('.pg').forEach(s=>s.classList.toggle('on',s.id===id));document.querySelectorAll('#nav a').forEach(a=>a.classList.toggle('on',a.hash==='#'+id));$('nav').classList.remove('open');scrollTo(0,0)}
function init(){const n=S.name||'Lisaluxhomes';document.title=n+' | Homes, Land & Airbnb Stays in Kenya';['brand','fn','fn2'].forEach(i=>$(i).textContent=n);$('ft').textContent=S.tagline||'';$('tag').textContent=S.tagline||'';$('yr').textContent=new Date().getFullYear();
 const tel='tel:'+String(S.phone||'').replace(/\s/g,''),ml='mailto:'+(S.email||'');
 [['ba',S.address],['ca',S.address]].forEach(([i,v])=>$(i).textContent=v||'');[['be',S.email,ml],['ce',S.email,ml],['fe',S.email,ml],['bp',S.phone,tel],['cp',S.phone,tel],['fp',S.phone,tel]].forEach(([i,v,h])=>{$(i).textContent=v||'';$(i).href=h});
 $('ch').innerHTML=(S.hours||[]).map(esc).join('<br>');$('loc').innerHTML+=(S.areas||[]).map(a=>`<option>${esc(a)}</option>`).join('');
 $('nav').innerHTML=PAGES.map(p=>`<a href="#${p[0]}">${p[1]}</a>`).join('')+'<a class="agent" href="/agent.html"><i class="fa-solid fa-user-lock"></i> Agent login</a>';
 $('fl').innerHTML=PAGES.map(p=>`<a href="#${p[0]}">${p[1]}</a>`).join('<br>')+'<br><a href="/agent.html">Agent login</a>';
 $('stats').innerHTML=(S.stats||[]).map(x=>`<div class="stat"><b>${esc(x.n)}</b><span>${esc(x.l)}</span></div>`).join('');
 const cd=(a,k)=>(a||[]).map(x=>`<div class="card b"><div class="ico"><i class="fa-solid fa-${esc(x.i)}"></i></div><h3>${esc(x.t)}</h3><p class="mut">${esc(x.x)}</p></div>`).join('');$('svc').innerHTML=cd(S.services);$('whyg').innerHTML=cd(S.why);
 $('faqs').innerHTML=(S.faqs||[]).map((f,i)=>`<details${i?'':' open'}><summary>${esc(f.q)}</summary><p>${esc(f.a)}</p></details>`).join('');
 $('soc').innerHTML=(S.social||[]).filter(s=>s.url).map(s=>`<a href="${esc(safe(s.url))}" target="_blank" rel="noopener" aria-label="${esc(s.name)}"><i class="fa-brands fa-${esc(s.icon)}"></i></a>`).join('')}
async function load(){try{const r=await fetch(API+'listings/records?perPage=200&sort=-featured,-created');if(!r.ok)throw 0;ALL=(await r.json()).items}catch(e){$('count').textContent='Could not load listings'}fill()}
addEventListener('hashchange',route);init();route();load();
</script></body></html>
''')

w(P + 'style.css', r'''/* Lisaluxhomes. Also used by agent.html. */
.srcs{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:0 0 18px}.src{display:block;text-align:left;background:#fff;color:var(--ink);border:1px solid var(--line);padding:12px 16px;position:relative;border-radius:12px}.src b{display:block}.src span{font-weight:400;font-size:12px;color:var(--mut)}
.src .n{position:absolute;right:14px;top:10px;font:600 22px 'Playfair Display',serif;font-style:normal;color:var(--gold)}.src.on{background:var(--navy);color:#fff}.src.on span{color:#d9d2e0}.src:hover{background:#f6ecde;color:var(--ink)}.src.on:hover{background:var(--navy);color:#fff}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}.tools select{width:auto}.grid.sm{grid-template-columns:repeat(auto-fill,minmax(210px,1fr))}.grid.sm .d{display:none}.grid.list{grid-template-columns:1fr}
@media(min-width:700px){.grid.list .card{display:grid;grid-template-columns:300px 1fr}.grid.list .card img,.grid.list .ph{height:100%;min-height:200px}}
.ann{position:relative;background:linear-gradient(135deg,#f6dd95,#e3bb55 45%,#c9962b);color:#2a2433;text-align:center;padding:9px 46px;font-weight:600;font-size:14px}.ann a{color:#2a2433;margin-left:8px}.ann button{position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;color:#2a2433;font-size:22px;padding:0 8px}.ann button:hover{background:none}
.intro{text-align:center;padding:10px 0 34px}.intro h1{font-size:clamp(28px,4.5vw,44px)}.quote{font-style:italic}.quote i{color:var(--gold);font-size:22px;display:block;margin-bottom:6px}
.cta{margin:46px auto 0;padding:34px 30px;border-radius:20px;display:flex;flex-wrap:wrap;gap:18px;align-items:center;justify-content:space-between;background:linear-gradient(135deg,#fff8e3,#f6e6b6);border:1px solid #e3d3a4}.cta h2{margin:0;font-size:26px}.cta p{margin:4px 0 0;color:#5b5340}
.wa{position:fixed;right:18px;bottom:18px;z-index:50;width:56px;height:56px;border-radius:50%;background:#25d366;color:#fff;display:grid;place-items:center;font-size:30px;box-shadow:0 10px 28px #0006;text-decoration:none}.chk{display:flex;gap:8px;align-items:center}.chk input{width:auto}
:root{--navy:#2a2433;--gold:#b08d57;--rose:#e8455c;--ink:#2a2433;--mut:#6f6a78;--line:#eadfe0}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:15px/1.65 Inter,system-ui,sans-serif;color:var(--ink);background:linear-gradient(160deg,#fff7f0 0%,#fde9e6 42%,#ebe8f9 100%) fixed}
a{color:var(--gold)}h1,h2,h3,h4{margin:0 0 8px;line-height:1.25;font-family:'Playfair Display',Georgia,serif;font-weight:600}h2{font-size:32px}.w{max-width:1240px;margin:0 auto;padding:0 20px}.mut{color:var(--mut);font-size:14px}.b{padding:18px}
.bar{background:var(--navy);color:#e9e4ee;font-size:13px}.bar .w{display:flex;gap:8px 24px;flex-wrap:wrap;align-items:center;padding-block:8px}.bar a{color:#e9e4ee;text-decoration:none}.bar i{color:var(--gold);margin-right:6px}
.top{position:sticky;top:0;z-index:30;background:#ffffffe8;backdrop-filter:blur(10px);border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:18px;padding:10px 24px}
.logo{display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font:600 22px 'Playfair Display',Georgia,serif}.logo img{width:40px;height:40px;border-radius:10px}
.links{display:none;gap:4px;align-items:center}.links a{color:var(--ink);text-decoration:none;font-weight:500;font-size:14px;padding:8px 11px;border-radius:99px;white-space:nowrap}.links a:hover,.links a.on{background:#f6ecde;color:#8a6d3b}
.links a.agent{background:var(--navy);color:#fff;margin-left:6px}.links a.agent:hover{background:var(--gold);color:#fff}
.links.open{display:flex;flex-direction:column;align-items:stretch;position:absolute;top:100%;left:0;right:0;background:#fff;padding:12px 20px;border-bottom:1px solid var(--line);box-shadow:0 16px 30px #2a243322}
@media(min-width:1150px){.links{display:flex}#mb{display:none}}
button,.btn{display:inline-block;background:var(--navy);color:#fff;border:0;border-radius:10px;padding:10px 18px;font:600 13px Inter,sans-serif;cursor:pointer;text-decoration:none;width:auto;transition:.2s}
button:hover,.btn:hover{background:var(--gold)}.bnb{background:#ff385c}.bnb:hover{background:#e0294a}button.s{background:#efe6e6;color:var(--ink)}button.s:hover{background:#e3d6d6}button.d{background:#dc2626}.btn.ghost{background:transparent;border:1px solid #fff;color:#fff}.btn.ghost:hover{background:#fff;color:var(--ink)}
.tabs{display:flex;gap:8px;margin-bottom:16px}.tabs button:not(.on){background:#efe6e6;color:var(--ink)}
input,select,textarea{font:inherit;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:#fff;color:var(--ink);width:100%}input:focus,select:focus,textarea:focus{outline:none;border-color:var(--gold)}
.pg{display:none;padding:52px 0}.pg.on{display:block}#home{padding:0 0 60px}
.hero{position:relative;height:min(74vh,580px);background:linear-gradient(135deg,#2a2433,#5b4b63);overflow:hidden;margin-bottom:40px}
.hs{position:absolute;inset:0;display:flex;align-items:center;padding:0 max(20px,calc((100% - 1200px)/2));background:center/cover;opacity:0;transition:opacity 1.2s}.hs.on{opacity:1}
.hs:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#2a2433d9,#2a243333)}.hs .in{position:relative;z-index:2;max-width:620px;color:#fff}.hs h2{font-size:clamp(28px,5vw,50px);color:#fff}.hs p{color:#eee8f1}
.lab{display:inline-block;background:var(--gold);color:#fff;padding:2px 12px;border-radius:99px;font-size:12px;font-weight:600;margin-bottom:10px}
.hbtns{position:absolute;z-index:3;bottom:30px;left:max(20px,calc((100% - 1200px)/2));display:flex;gap:10px;flex-wrap:wrap}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin-bottom:44px}.stat{background:#ffffffcc;border:1px solid var(--line);border-radius:14px;text-align:center;padding:18px 10px}.stat b{display:block;font:700 34px 'Playfair Display',serif;color:var(--gold)}.stat span{color:var(--mut);font-size:13px}
.hd{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px}.tools{display:flex;gap:8px;flex-wrap:wrap}
.grid{display:grid;gap:24px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}.cats{grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}
.card{position:relative;background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 4px 18px #2a24330d;transition:.25s}.card:hover{transform:translateY(-3px);box-shadow:0 16px 38px #2a243322}
.card img,.ph{width:100%;height:210px;object-fit:cover;display:block}.ph{display:grid;place-items:center;font-size:46px;color:#d8c7ae;background:linear-gradient(135deg,#f6e9df,#e8e3f4)}
.card h3{font-size:19px;margin:8px 0 2px}.d{color:var(--mut);margin:6px 0;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.price{font-weight:700;font-size:20px;color:var(--navy)}.price small{font-weight:400;color:var(--mut);font-size:13px}.old{color:var(--mut);text-decoration:line-through;font-size:13px;margin-left:8px;font-weight:400}
.tag{display:inline-block;padding:1px 10px;border:1px solid var(--line);border-radius:99px;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);margin-right:4px}.tag.r{border-color:#dc2626;color:#dc2626}
.rib{position:absolute;top:12px;left:12px;z-index:2;background:var(--rose);color:#fff;padding:2px 12px;border-radius:99px;font-size:12px;font-weight:700}
.act{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.pager{display:flex;gap:6px;justify-content:center;margin-top:28px;flex-wrap:wrap}
.cat{padding:30px 16px;text-align:center;cursor:pointer;font-weight:600}.cat i{display:block;font-size:30px;color:var(--gold);margin-bottom:8px}
.ico{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;background:#f6ecde;color:#8a6d3b;font-size:20px;margin-bottom:8px}
.faq{max-width:860px}.faq details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:0 20px;margin-bottom:12px}.faq summary{cursor:pointer;padding:16px 0;font-weight:600}.faq p{margin:0 0 16px;color:var(--mut)}
.two{display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}.f{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}
dialog{border:0;border-radius:16px;padding:0;max-width:620px;width:92%;overflow:hidden}dialog::backdrop{background:#2a243399}dialog img{width:100%;max-height:340px;object-fit:cover;display:block}.x{position:absolute;right:10px;top:10px;z-index:2;background:#fff;color:var(--ink);font-size:20px;padding:2px 12px}
footer{background:var(--navy);color:#d9d2e0;padding:44px 0 20px;margin-top:20px}.fg{display:grid;gap:30px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}footer h4{color:#fff}footer a{color:#e6c88f;text-decoration:none}
.soc{display:flex;gap:10px;margin-top:12px}.soc a{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line);color:var(--ink)}.soc a:hover{background:var(--gold);color:#fff}
.copy{max-width:1240px;margin:26px auto 0;padding:16px 20px 0;border-top:1px solid #4a4256;font-size:13px;text-align:center}
main{max-width:1100px;margin:0 auto;padding:24px}table{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden}th,td{padding:10px;text-align:left;border-bottom:1px solid var(--line)}.wrap{overflow-x:auto}form.card{padding:14px;margin-bottom:16px}
''')
print('\nDone. Restart the server, then open the site in a fresh Incognito window.')
