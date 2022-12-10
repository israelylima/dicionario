import requests
from bs4 import BeautifulSoup


def buscaSignificado(palavra):
    url = 'https://www.dicio.com.br/pesquisa.php?q=' + palavra

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    pagina_unico_resultado = soup.findAll('p', class_="significado textonovo")

    if len(pagina_unico_resultado) > 0:
        titulo = soup.findAll('h2', class_="tit-significado")
        titulo = titulo[0].getText()
        card_definicoes = pagina_unico_resultado[0]
        definicoes = card_definicoes.findAll('span')
        significado = definicoes[1].getText()
        return titulo + '\n' + significado

    else:
        titulo = soup.findAll('span', class_="list-link")
        pagina_varios_resultados = soup.findAll('span', class_="list-desc")
        titulo = titulo[0].getText()
        significado = pagina_varios_resultados[0].getText()
        return 'Significado de ' + titulo + '\n' + significado
