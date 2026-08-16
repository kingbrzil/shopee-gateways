import sys
import subprocess
import urllib.request
import re
import os

try:
    from googlesearch import search
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'googlesearch-python', '-q'])
    from googlesearch import search

pasta = r'c:\Users\visitante\.gemini\antigravity-ide\scratch\shopee-gateways'

nichos = {
    'carteirinha_estudante': 'manual do estudante ufpr pdf',
    'prostata': 'manual cancer de prostata urologia pdf',
    'desempenho_masculino': 'cartilha saude do homem sbu pdf',
    'unhas_fibra': 'apostila manicure unhas pdf infolivros',
    'alocacao_ativos': 'guia alocacao de ativos pdf cvm',
    'pnl_mente': 'apostila pnl pdf',
    'migalhas_emocionais': 'cartilha dependencia emocional pdf',
    'mulher_magnetica': 'livro autoestima pdf'
}

def bypass_download(url, filename):
    print(f'Tentando baixar: {url}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        data = resp.read()
        if len(data) > 50000 and data.startswith(b'%PDF'):
            with open(filename, 'wb') as f:
                f.write(data)
            print(f'[OK] {filename} baixado ({len(data)} bytes)')
            return True
        else:
            print(f'[ERRO] Nao e PDF ou e muito pequeno: {len(data)} bytes')
    except Exception as e:
        print(f'[ERRO] {e}')
    return False

for nicho, query in nichos.items():
    arquivo = os.path.join(pasta, f'isca_{nicho}.pdf')
    print(f'\nBuscando: {nicho} ({query})...')
    try:
        success = False
        for url in search(query, num_results=10, lang='pt'):
            if url.lower().endswith('.pdf') and 'gov.br' not in url:
                if bypass_download(url, arquivo):
                    success = True
                    break
        if not success:
            print(f'[FALHA TOTAL] Nao conseguiu um PDF real para {nicho}')
    except Exception as e:
        print(f'[ERRO GOOGLE] {e}')
