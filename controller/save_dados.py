from openpyxl import load_workbook
import controller.functions as func
import time
from openpyxl.utils import column_index_from_string

def save_dados(dados, list_conq, list_sub_conq, prompt, root):

    wb = load_workbook(dados["PLANILHA"])
    ws = wb.active

    # Determinar células
    if dados["CELULAS PADÃO"] == 0:
        col1, row1 = func.split_text_nun(dados["CELL1"])
        col2, row2 = func.split_text_nun(dados["CELL2"])

    else:
        col1 = "A"
        row1 = 2
        col2 = "B"
        row2 = 2

    # <editor-fold desc="## SALVAR TODOS OS DADOS NA PLANILHA ##">
    prompt.configure(
        text=f"::==> Iniciar Salvamendo de dados",
    )
    root.update()
    time.sleep(1)
    text10 = f"::==> Salvar Conquista nas CELL '{col1}{row1}' e Sub Conquista nas CELL '{col2}{row2}'" if dados["CELULAS PADÃO"] == 0 else \
                                                                            "::==> Salvar Conquista nas celulas Padrão 'A2' & 'b2'"
    prompt.configure(
        text=text10
    )
    root.update()

    if dados["COLETAR CONQUISTA"] == 1:
        for conquista in list_conq:
            cel1 = f"{col1}{row1}"
            ws[cel1].value = conquista
            prompt.configure(
                text=f"::==> CONQUISTA {conquista} Salva na CELL {cel1}."
            )
            root.update()
            row1 += 1

        wb.save(dados["PLANILHA"])

    if dados["COLETAR SUB CONQUISTA"] == 1:
        for sub_conquista in list_sub_conq:
            try:
                cel2 = f"{col2}{row2}"
                if len(sub_conquista) == 1:
                    ws[cel2].value = sub_conquista[0]
                    prompt.configure(
                        text=f"::==> SUB CONQUISTA {sub_conquista} Salva na CELL {cel2}."
                    )
                    root.update()
                    row2 += 1
                else:
                    indice = 0
                    for text in sub_conquista:
                        celula = ws[cel2]
                        ws.cell(row=celula.row, column=celula.column + indice).value = text
                        indice += 1
                    row2 += 1
            except Exception as e:
                aviso = f"[ERRO] Ao salvar SUB CONQUISTA {sub_conquista}: {e}"
                print(aviso)
                prompt.configure(text=aviso)
                root.update()

        wb.save(dados["PLANILHA"])
        # </editor-fold

