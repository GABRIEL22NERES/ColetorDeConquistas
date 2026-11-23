import json
from pathlib import Path

class Model:
    def __init__(self):
        self.db_path = Path(__file__).parent / "database"

    # ----- Carregar JSON -----
    def carregar_json(self, nome_arquivo: str) -> dict:
        caminho_arquivo = self.db_path / nome_arquivo

        if caminho_arquivo.exists():
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {}  # retorna dicionário vazio se o arquivo não existir

    # ----- Salvar JSON -----
    def salvar_json(self, nome_arquivo: str, dados: dict):
        caminho_arquivo = self.db_path / nome_arquivo
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
