import sys,re,csv,json,concurrent.futures as cf,requests,datetime
ex=set(open('excluded.txt').read().split())
rows=[l.strip().split('|') for l in open('sites.txt') if l.strip()]
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124'}
E=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}')
bad=('example','sentry','wix','domain','squarespace','godaddy','.png','.jpg','.webp','email.com','yourname','shopify','gmail.co')
def get(u):
    try: return requests.get(u,headers=H,timeout=12).text
    except: return ''
def go(r):
    biz,typ,city,site=r
    base=site.rstrip('/')
    if not base.startswith('http'): base='https://'+base
    pages={p:get(base+p) for p in ['','/contact','/pages/contact','/contact-us','/about']}
    txt=' '.join(pages.values())
    em=[e.lower() for e in E.findall(txt) if not any(b in e.lower() for b in bad)]
    em=[e for e in dict.fromkeys(em) if e not in ex]
    if not em: return None
    dom=re.sub(r'^https?://(www\.)?','',base).split('/')[0]
    em.sort(key=lambda e:(dom.split('.')[0] not in e, not e.startswith(('info','hello','contact','shop'))))
    h=pages[''].lower()
    hol=any(k in h for k in ['black friday','small business saturday','holiday sale','gift guide','cyber monday'])
    gc='gift card' in h
    if hol: det='site already mentions a holiday/Black Friday promo'
    elif typ in('boutique','gift shop','florist'): det='no Black Friday or Small Business Saturday promo on homepage yet'
    else: det='no holiday offer on homepage'+('' if gc else ' and no gift card promo')
    return dict(business=biz,type=typ,city=city,email=em[0],website=base,personalization=det,holiday_promo_found=hol)
with cf.ThreadPoolExecutor(30) as x: res=[r for r in x.map(go,rows) if r]
seen=set();out=[]
for r in res:
    if r['email'] in seen: continue
    seen.add(r['email']);out.append(r)
w=csv.DictWriter(open('leads.csv','w'),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print(len(rows),len(out))
