import requests
import os
import re

def verificar_url(url: str) -> bool:
    try:
        resposta = requests.head(url, timeout=10)
        return resposta.status_code == 200
    except requests.RequestException:
        return False

def validar_plan(caminho_planilha):
    if os.path.exists(caminho_planilha):
        return True
    else:
        return False

def split_text_nun(texto):
    letras = re.findall(r'[A-Za-z]+', texto)
    numeros = re.findall(r'\d+', texto)

    letra = letras[0] if letras else ''
    numero = numeros[0] if numeros else ''

    return letra, numero
