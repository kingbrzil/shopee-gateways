import urllib.request
import urllib.parse
import os
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

pasta = r'c:\Users\visitante\.gemini\antigravity-ide\scratch\shopee-gateways'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

nichos = {
    'carteirinha_estudante': 'carteira de estudante manual pdf',
    'prostata': 'cancer de prostata manual pdf',
    'desempenho_masculino': 'saude do homem cartilha pdf'
}

def bypass_download(url, filename):
    if not url.startswith('http'):
        return False
    print(f'  Testando: {url}')
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10, context=ctx)
        data = resp.read()
        if len(data) > 15000 and data.startswith(b'%PDF'):
            with open(filename, 'wb') as f:
                f.write(data)
            print(f'  [OK] Baixado com sucesso! ({len(data)} bytes)')
            return True
    except Exception as e:
        pass
    return False

for nicho, query in nichos.items():
    print(f'\nBuscando: {nicho} no Bing...')
    arquivo = os.path.join(pasta, f'isca_{nicho}.pdf')
    sucesso = False
    bing_url = f'https://www.bing.com/search?q={urllib.parse.quote(query)}'
    req = urllib.request.Request(bing_url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=15, context=ctx).read().decode('utf-8')
        links = re.findall(r'href=[\'\"](https?://[^\'\"]+\.pdf)[\'\"]', html, re.IGNORECASE)
        if not links:
            links = re.findall(r'href=[\'\"](https?://[^\'\"]+)[\'\"]', html, re.IGNORECASE)
            links = [l for l in links if '.pdf' in l.lower()]
            
        print(f'  Encontrados {len(links)} links PDF via Bing.')
        for link in links:
            if bypass_download(link, arquivo):
                sucesso = True
                break
    except Exception as e:
        print(f'  [ERRO BING] {e}')
    
    if not sucesso:
        print(f'[FALHA TOTAL] Nao foi possivel baixar {nicho}')
