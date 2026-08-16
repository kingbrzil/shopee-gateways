import urllib.request
import re
import os
import urllib.error

def download_pdf(url, filename):
    print(f'Acessando {url}...')
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        links = re.findall(r'href=[\'\"](https?://[^\'\"]+\.pdf)[\'\"]', html)
        if links:
            pdf_url = links[0]
            print(f'Baixando PDF real: {pdf_url}')
            pdf_req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                pdf_data = urllib.request.urlopen(pdf_req).read()
                with open(filename, 'wb') as f:
                    f.write(pdf_data)
                print(f'[OK] Salvo {filename}')
                return True
            except Exception as e:
                print(f'[ERRO] Falha ao baixar PDF ({pdf_url}): {e}')
        else:
            print('[ERRO] Nenhum link PDF na pagina')
    except urllib.error.HTTPError as e:
        print(f'[ERRO] {e.code} - {e.reason}')
    except Exception as e:
        print(f'[ERRO] {e}')
    return False

def direct_download(pdf_url, filename):
    print(f'Baixando direto: {pdf_url}')
    try:
        pdf_req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
        pdf_data = urllib.request.urlopen(pdf_req).read()
        with open(filename, 'wb') as f:
            f.write(pdf_data)
        print(f'[OK] Salvo {filename}')
    except Exception as e:
        print(f'[ERRO] Falha: {e}')

pasta = r'c:\Users\visitante\.gemini\antigravity-ide\scratch\shopee-gateways'

# 1. Barbeiro
download_pdf('https://infolivros.org/livros-pdf-gratis/oficios/barbearia/', os.path.join(pasta, 'isca_barbeiro_online.pdf'))

# 2. Carteirinha Estudante (using a generic student guide from a real university)
direct_download('https://www.ufrgs.br/prograd/wp-content/uploads/2019/02/Manual-do-Estudante-2019.pdf', os.path.join(pasta, 'isca_carteirinha_estudante.pdf'))

# 3. Prostata (trying a non-gov direct link, or a hospital guide)
direct_download('https://www.hcor.com.br/wp-content/uploads/2019/10/Cartilha-Novembro-Azul.pdf', os.path.join(pasta, 'isca_prostata.pdf'))

# 4. Desempenho Masculino
direct_download('https://bvsms.saude.gov.br/bvs/publicacoes/politica_nacional_atencao_integral_saude_homem.pdf', os.path.join(pasta, 'isca_desempenho_masculino.pdf'))

# 5. CNH Ansiedade
direct_download('https://www.detran.sp.gov.br/wps/wcm/connect/19227ed9-49ed-49a3-a757-b0ccafc011e4/Manual+de+Direcao+Defensiva.pdf', os.path.join(pasta, 'isca_cnh_ansiedade.pdf'))

# 6. Unhas Fibra
download_pdf('https://infolivros.org/livros-pdf-gratis/oficios/manicure-e-pedicure/', os.path.join(pasta, 'isca_unhas_fibra.pdf'))

# Restore the 4 that were successfully downloaded in task 1248 but overwritten by my wikipedia script
# 7. Alocacao Ativos
direct_download('https://assetfront.arquivosparceiros.cloud.itau.com.br/ISG/Apostila_Alocacao_Ativos.pdf', os.path.join(pasta, 'isca_alocacao_ativos.pdf'))

# 8. PNL Mente
download_pdf('https://infolivros.org/livros-pdf-gratis/psicologia/programacao-neurolinguistica-pnl/', os.path.join(pasta, 'isca_pnl_mente.pdf'))

# 9. Migalhas Emocionais
download_pdf('https://infolivros.org/livros-pdf-gratis/psicologia/dependencia-emocional/', os.path.join(pasta, 'isca_migalhas_emocionais.pdf'))

# 10. Mulher Magnetica
download_pdf('https://infolivros.org/livros-pdf-gratis/psicologia/autoestima/', os.path.join(pasta, 'isca_mulher_magnetica.pdf'))
