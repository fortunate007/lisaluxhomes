import os
P = 'pb_public/'
if not os.path.isfile(P + 'index.html'):
    raise SystemExit('Run this from your project folder (the one containing pb_public)')

url = input('Supabase Project URL (https://xxxx.supabase.co): ').strip().rstrip('/')
key = input('Supabase anon public key: ').strip()
if not url.startswith('https://') or len(key) < 20:
    raise SystemExit('That does not look right. Run the script again.')

# ---- config.js: add the keys ----
c = open(P + 'config.js', encoding='utf-8').read()
import re
c = re.sub(r'\n\s*supabaseUrl:.*|\n\s*supabaseKey:.*', '', c)
c = c.replace('window.SITE = {', 'window.SITE = {\n  supabaseUrl: "%s",\n  supabaseKey: "%s",' % (url, key), 1)
open(P + 'config.js', 'w', encoding='utf-8').write(c)
print('ok   config.js | Supabase URL and key saved')

# ---- index.html: read listings and send inquiries through Supabase ----
s = open(P + 'index.html', encoding='utf-8').read()
R = [
 ("const API='/api/collections/',",
  "const SBU=(window.SITE&&window.SITE.supabaseUrl||'').replace(/\\/$/,''),SBK=(window.SITE&&window.SITE.supabaseKey)||'',SBH={apikey:SBK,Authorization:'Bearer '+SBK},"),
 ("const img=l=>l.image?`/api/files/${l.collectionId}/${l.id}/${encodeURIComponent(l.image)}`:'';",
  "const img=l=>l.image?SBU+'/storage/v1/object/public/listing-images/'+encodeURIComponent(l.image):'';"),
 ("const r=await fetch(API+'listings/records?perPage=200&sort=-featured,-created');if(!r.ok)throw 0;ALL=(await r.json()).items",
  "const r=await fetch(SBU+'/rest/v1/listings?select=*&order=featured.desc,created_at.desc&limit=200',{headers:SBH});if(!r.ok)throw 0;ALL=await r.json()"),
 ("const r=await fetch(API+'inquiries/records',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});",
  "const r=await fetch(SBU+'/rest/v1/inquiries',{method:'POST',headers:{...SBH,'Content-Type':'application/json',Prefer:'return=minimal'},body:JSON.stringify(b)});"),
]
for a, b in R:
    print('ok  ' if a in s else 'MISS', 'index.html |', a[:50]); s = s.replace(a, b)
open(P + 'index.html', 'w', encoding='utf-8').write(s)

# ---- agent.html: new portal on Supabase ----
open(P + 'agent.html', 'w', encoding='utf-8').write(r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Agent Portal</title><meta name="robots" content="noindex,nofollow"><link rel="icon" href="/lisaluxhomes-icon.svg"><link rel="stylesheet" href="/style.css"><script src="/config.js"></script></head><body>
<header class="top"><strong class="logo">&#9670; Agent Portal</strong><span id="who" class="mut"></span><span><a href="/">View site</a> &middot; <a href="#" onclick="out();return false">Logout</a></span></header>
<main id="app"></main>
<script>
const C=window.SITE||{},U=(C.supabaseUrl||'').replace(/\/$/,''),K=C.supabaseKey||'',S=sessionStorage,app=document.getElementById('app');
let tok=S.tok||'',me=JSON.parse(S.me||'null'),tab='listings',edit=null,L=[];
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const mgr=()=>me&&me.app_metadata&&me.app_metadata.role==='manager',$w=t=>document.getElementById('who').textContent=t;
const hdr=()=>({apikey:K,Authorization:'Bearer '+(tok||K)});
async function api(p,o={}){o.headers={...hdr(),...(o.headers||{})};const r=await fetch(U+p,o),t=await r.text();let j=null;try{j=t?JSON.parse(t):null}catch(e){}
 if(r.status===401){out();throw 0}if(!r.ok){alert((j&&(j.message||j.msg||j.error))||'Not allowed');throw 0}return j}
function login(){$w('');app.innerHTML=`<div class="card b" style="max-width:340px;margin:60px auto"><h3>Agent login</h3><input id="em" placeholder="Email" style="margin-bottom:8px"><input id="pw" type="password" placeholder="Password" style="margin-bottom:10px" onkeydown="event.key==='Enter'&&go()"><button onclick="go()">Enter</button></div>`}
async function go(){const r=await fetch(U+'/auth/v1/token?grant_type=password',{method:'POST',headers:{apikey:K,'Content-Type':'application/json'},body:JSON.stringify({email:em.value,password:pw.value})});
 if(!r.ok)return alert('Wrong email or password');const d=await r.json();tok=d.access_token;me=d.user;S.tok=tok;S.me=JSON.stringify(me);render()}
function out(){S.clear();tok='';me=null;login()}
async function render(){if(!me||!tok)return login();$w((me.email||'')+' - '+(mgr()?'manager':'agent'));
 let h=`<div class="tabs">${['listings','inquiries'].map(t=>`<button class="${t===tab?'on':''}" onclick="tab='${t}';edit=null;render()">${t}</button>`).join('')}</div>`;
 if(tab==='listings'){L=await api('/rest/v1/listings?select=*&order=created_at.desc&limit=200'+(mgr()?'':'&owner=eq.'+me.id));const e=edit?L.find(x=>x.id===edit)||{}:{};
  const o=(v,a)=>a.map(x=>`<option ${x===v?'selected':''}>${x}</option>`).join('');
  h+=`<form class="card f" id="lf" onsubmit="save(event)"><strong style="grid-column:1/-1">${edit?'Edit':'Add'} listing</strong>
  <input name="title" placeholder="Title" value="${esc(e.title)}" required><input name="price" type="number" placeholder="Price in KSh (nightly rate for Airbnb)" value="${e.price??''}">
  <select name="type">${o(e.type,['sale','rent','land','commercial','airbnb'])}</select><select name="status">${o(e.status||'available',['available','sold','rented','hidden'])}</select>
  <input name="location" placeholder="Location e.g. Karen, Nairobi" value="${esc(e.location)}"><input name="size" type="number" placeholder="Size (m2)" value="${e.size??''}">
  <input name="bedrooms" type="number" placeholder="Beds" value="${e.bedrooms??''}"><input name="bathrooms" type="number" placeholder="Baths" value="${e.bathrooms??''}">
  <input name="photo" type="file" accept="image/jpeg,image/png,image/webp"><label><input type="checkbox" name="featured" style="width:auto" ${e.featured?'checked':''}> Featured</label>
  <label><input type="checkbox" name="offer" style="width:auto" ${e.offer?'checked':''}> On offer</label><input name="old_price" type="number" placeholder="Old price (for offers)" value="${e.old_price||''}">
  <input name="airbnb_url" placeholder="Airbnb link (Airbnb stays only)" value="${esc(e.airbnb_url)}"><input name="offer_note" placeholder="Offer note e.g. 10% off" value="${esc(e.offer_note)}">
  <textarea name="description" placeholder="Description" style="grid-column:1/-1">${esc(e.description)}</textarea>
  <button>${edit?'Update':'Create'}</button>${edit?'<button type="button" class="s" onclick="edit=null;render()">Cancel</button>':''}</form>
  <div class="wrap"><table><tr><th>Title</th><th>Type</th><th>Status</th><th>Location</th><th>Price (KSh)</th><th></th></tr>${L.map(l=>`<tr><td>${esc(l.title)}${l.offer?' &#128293;':''}</td><td>${esc(l.type)}</td><td>${esc(l.status)}</td><td>${esc(l.location)}</td><td>${Number(l.price).toLocaleString()}</td>
  <td><button class="s" data-i="${l.id}" onclick="edit=this.dataset.i;render();scrollTo(0,0)">Edit</button> <button class="d" data-i="${l.id}" onclick="del(this.dataset.i)">Delete</button></td></tr>`).join('')||'<tr><td colspan=6>No listings yet.</td></tr>'}</table></div>`}
 if(tab==='inquiries'){const I=await api('/rest/v1/inquiries?select=*,listings(title)&order=handled.asc,created_at.desc&limit=200');
  h+=`<div class="wrap"><table><tr><th>From</th><th>Contact</th><th>Property</th><th>Message</th><th></th></tr>${I.map(i=>`<tr style="opacity:${i.handled?.5:1}"><td>${esc(i.name)}<div class="mut">${esc((i.created_at||'').slice(0,16))}</div></td><td>${esc(i.email)}<br>${esc(i.phone)}</td>
  <td>${esc(i.listings?i.listings.title:'-')}</td><td>${esc(i.message)}</td><td><button class="s" data-i="${i.id}" data-h="${!i.handled}" onclick="mark(this.dataset.i,this.dataset.h==='true')">${i.handled?'Reopen':'Done'}</button></td></tr>`).join('')||'<tr><td colspan=5>No enquiries yet.</td></tr>'}</table></div>
  <p class="mut">You see enquiries on your own listings${mgr()?' (managers see all, including general contact messages)':''}.</p>`}
 app.innerHTML=h}
async function save(ev){ev.preventDefault();const fm=ev.target,d=new FormData(fm),v=k=>String(d.get(k)||'').trim(),n=k=>v(k)===''?null:+v(k);
 const b={title:v('title'),price:n('price')||0,type:v('type'),status:v('status'),location:v('location'),size:n('size'),bedrooms:n('bedrooms'),bathrooms:n('bathrooms'),description:v('description'),featured:fm.featured.checked,offer:fm.offer.checked,old_price:n('old_price'),offer_note:v('offer_note'),airbnb_url:v('airbnb_url')};
 const f=fm.photo.files[0];if(f){if(f.size>5242880)return alert('Photo is over 5 MB. Please choose a smaller one.');
  const path=(crypto.randomUUID?crypto.randomUUID():Date.now())+'.'+((f.name.split('.').pop()||'jpg').toLowerCase());
  await api('/storage/v1/object/listing-images/'+path,{method:'POST',headers:{'x-upsert':'true'},body:f});b.image=path}
 const J={'Content-Type':'application/json',Prefer:'return=minimal'};
 if(edit)await api('/rest/v1/listings?id=eq.'+edit,{method:'PATCH',headers:J,body:JSON.stringify(b)});else await api('/rest/v1/listings',{method:'POST',headers:J,body:JSON.stringify(b)});
 edit=null;render()}
async function del(id){if(confirm('Delete this listing?')){await api('/rest/v1/listings?id=eq.'+id,{method:'DELETE'});render()}}
async function mark(id,h){await api('/rest/v1/inquiries?id=eq.'+id,{method:'PATCH',headers:{'Content-Type':'application/json',Prefer:'return=minimal'},body:JSON.stringify({handled:h})});render()}
render().catch(()=>{});
</script></body></html>
''')
print('ok   agent.html | rewritten for Supabase')
print('\nDone. Test it locally:  cd pb_public && python3 -m http.server 8095')
