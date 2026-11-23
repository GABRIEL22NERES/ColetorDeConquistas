import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException


def begin_data_scraping(data_package, prompt):
    def traduzir_lista(lista_textos):
        traduzidos = []

        for texto in lista_textos:
            # Se for lista, traduz cada item separadamente
            if isinstance(texto, list):
                itens_traduzidos = []
                for t in texto:
                    t = (t or "").strip()
                    if not t:
                        continue
                    try:
                        idioma = detect(t)
                    except LangDetectException:
                        idioma = None

                    if idioma == "en":
                        try:
                            traducao = GoogleTranslator(source='en', target='pt').translate(t)
                        except Exception as e:
                            print(f"[ERRO TRADUÇÃO] Texto: '{t}' | Erro: {e}")
                            traducao = t
                    else:
                        traducao = t  # texto já não está em inglês, mantém
                    itens_traduzidos.append(traducao)
                traduzidos.append(itens_traduzidos)
            else:
                texto = (texto or "").strip()
                if not texto:
                    traduzidos.append("")
                    continue
                try:
                    idioma = detect(texto)
                except LangDetectException:
                    idioma = None

                if idioma == "en":
                    try:
                        traducao = GoogleTranslator(source='en', target='pt').translate(texto)
                    except Exception as e:
                        print(f"[ERRO TRADUÇÃO] Texto: '{texto}' | Erro: {e}")
                        traducao = texto
                else:
                    traducao = texto  # texto já não está em inglês, mantém
                traduzidos.append(traducao)

        return traduzidos


    # === Requisição da página ===
    url = data_package["LINK"]
    cabecalho = {'User-Agent': 'Mozilla/5.0'}
    resposta = requests.get(url, headers=cabecalho, timeout=15)
    resposta.raise_for_status()
    sopa = BeautifulSoup(resposta.text, 'html.parser')

    conquistas = []
    subtitles = []

    for bloco in sopa.find_all('div', class_='subSection detailBox'):

        titulo = ''
        subtitulo_text = ''

        # --- Coletar Título ---
        if data_package["COLETAR CONQUISTA"] == 1:
            titulo_div = bloco.find('div', class_='subSectionTitle')
            if titulo_div:
                raw = titulo_div.get_text()
                titulo = " ".join(raw.split()).strip()

        # --- Coletar Subtítulo ---
        if data_package["COLETAR SUB CONQUISTA"] == 1:
            desc_div = bloco.find('div', class_='subSectionDesc')
            if desc_div:
                # Captura todos os textos dentro da div, independente das tags
                textos_encontrados = desc_div.find_all(string=True)
                subtitulo_text = [t.strip() for t in textos_encontrados if t.strip() != ""]


        # --- Armazenar resultados ---
        if titulo or subtitulo_text:
            prompt.configure(text=f"::==> {titulo}")
            conquistas.append(titulo)
            prompt.configure(text=f"::==> {subtitulo_text}")
            subtitles.append(subtitulo_text)

    # === Tradução condicional ===
    conquistas_pt, subtitles_pt = [], []
    if data_package["COLETAR CONQUISTA"] == 1:
        conquistas_pt = traduzir_lista(conquistas)
    if data_package["COLETAR SUB CONQUISTA"] == 1:
        subtitles_pt = traduzir_lista(subtitles)

    return conquistas_pt, subtitles_pt
