import urllib.request
import urllib.parse
import os
import ssl

try:
    from googlesearch import search
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'googlesearch-python', '-q'])
    from googlesearch import search

# Ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

pasta = r'c:\Users\visitante\.gemini\antigravity-ide\scratch\shopee-gateways'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

nichos = {
    'carteirinha_estudante': 'carteirinha de estudante pdf -site:gov.br -site:edu.br',
    'prostata': 'cancer de prostata manual pdf -site:gov.br -site:edu.br',
    'desempenho_masculino': 'saude do homem cartilha pdf -site:gov.br -site:edu.br'
}

def bypass_download(url, filename):
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
        print(f'  [ERRO DOWNLOAD] {e}')
    return False

for nicho, query in nichos.items():
    print(f'\nBuscando: {nicho}')
    arquivo = os.path.join(pasta, f'isca_{nicho}.pdf')
    sucesso = False
    try:
        for url in search(query, num_results=30, lang='pt', pause=2.0):
            if url.lower().endswith('.pdf'):
                if bypass_download(url, arquivo):
                    sucesso = True
                    break
    except Exception as e:
        print(f'  [ERRO GOOGLE] {e}')
    
    if not sucesso:
        print('  [FALHA] Tentando via DuckDuckGo Lite...')
        ddg_url = 'https://lite.duckduckgo.com/lite/'
        data = urllib.parse.urlencode({'q': query}).encode('utf-8')
        req = urllib.request.Request(ddg_url, data=data, headers=headers)
        try:
            html = urllib.request.urlopen(req, timeout=10, context=ctx).read().decode('utf-8')
            import re
            links = re.findall(r'href=[\'\"]([^\'\"]+\.pdf)[\'\"]', html, re.IGNORECASE)
            for link in links:
                if link.startswith('//'): link = 'https:' + link
                elif link.startswith('/'): link = 'https://lite.duckduckgo.com' + link
                if bypass_download(link, arquivo):
                    sucesso = True
                    break
        except Exception as e:
            print(f'  [ERRO DDG] {e}')
            
    if not sucesso:
        print(f'[FALHA TOTAL] Nao foi possivel baixar {nicho}')
