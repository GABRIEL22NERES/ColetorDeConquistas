import os

from model.model import Model
from view.view import View
from controller.widgets_screen import WidgetStore
from CTkMessagebox import CTkMessagebox
import controller.functions as func
from tkinter import filedialog
import controller.data_scraping as d_s
import controller.save_dados as save_dados
from openpyxl import Workbook

class Controller:
    def __init__(self, class_main):
        self.class_main = class_main
        self.root = self.class_main.root
        self.widgets = WidgetStore()
        self.view = View(self, self.root, self.widgets)
        self.model = Model()

    def create_main_screen(self):
        self.view.create_header_screen()


        self.view.create_body_screen()


    def actions_buttons(self, event):

        # <editor-fold desc="## IMPORTAÇÃO DOS ELEMENTOS PRINCIPAIS DA TELA ##">
        prompt = self.widgets.get_widget("header", "label_prompt")
        cx_link = self.widgets.get_widget("div_coleta", "textbox_link")
        cx_plan = self.widgets.get_widget("div_salvar_dados", "textbox_planilha")
        cx_cell1 = self.widgets.get_widget("div_salvar_dados", "text_box_cell_1")
        cx_cell2 = self.widgets.get_widget("div_salvar_dados", "text_box_cell_2")
        check1 = self.widgets.get_widget("div_coleta", "checkbox_1")
        check2 = self.widgets.get_widget("div_coleta", "checkbox_2")
        check3 = self.widgets.get_widget("div_salvar_dados", "checkbox_3")
        check4 = self.widgets.get_widget("div_salvar_dados", "checkbox_4")

        # </editor-fold

        match event:
            case "<<ButtonSelectEndPlan>>":
                    caminho = filedialog.askopenfilename(
                        title="Selecione um arquivo",
                        filetypes=[("Todos os arquivos", "*.*")]
                    )
                    if caminho:  # se o usuário escolher algum arquivo
                        cx_plan.delete(0, "end")
                        cx_plan.insert(0, caminho)

            case "<<CheckBox1>>":
                txt1 = "::==> Coletas as Conquistas!"
                txt2 = "::==> Não Coletar as Conquistas!"

                if check1.get() == 1:
                    prompt.configure(
                        text=txt1,
                    )
                else:
                    prompt.configure(
                        text=txt2,
                    )
            case "<<CheckBox2>>":
                txt1 = "::==> Coletar Sub Titulos das Conquistas!"
                txt2 = "::==> Não Coletar Sub Titulos das Conquistas!"

                if check2.get() == 1:
                    prompt.configure(
                        text=txt1,
                    )
                else:
                    prompt.configure(
                        text=txt2,
                    )
            case "<<CheckBox3>>":
                txt1 = "::==> Criar um nova planilha!"
                txt2 = "::==> informa endereço da planilha!"

                if check3.get() == 1:
                    cx_plan.delete(0, "end")
                    cx_plan.configure(state="disabled",
                                      border_width=0)
                    prompt.configure(
                        text=txt1,
                    )
                    self.root.update()
                else:
                    cx_plan.configure(state="normal", border_width=1,
                                      border_color="light grey")
                    prompt.configure(
                        text=txt2,
                    )
                    self.root.update()
            case "<<CheckBox4>>":
                txt1 = "::==> colar nas celulas padrão do sistema [A2] [B2]"
                txt2 = "::==> Definir as celulas manualmente."

                if check4.get() == 1:
                    cx_cell1.delete(0, "end")
                    cx_cell2.delete(0, "end")
                    cx_cell1.configure(state="disabled",
                                      border_width=0)
                    cx_cell2.configure(state="disabled",
                                      border_width=0)
                    prompt.configure(
                        text=txt1,
                    )
                else:
                    cx_cell1.configure(state="normal", border_width=1,
                                      border_color="light grey")
                    cx_cell2.configure(state="normal", border_width=1,
                                      border_color="light grey")
                    prompt.configure(
                        text=txt2,
                    )

            case "<<ButtonStart>>":
                config = self.model.carregar_json("config.json")

                # <editor-fold desc="## VALIDAR LINK URL ##">

                txt2 = "O LINK INFORMADO NAO EXISTE, OU ESTA FORA DO AR :("
                link = cx_link.get()

                if not func.verificar_url(link):
                    cx_link.delete(0, "end")
                    cx_link.configure(placeholder_text="Link incorreto!!",
                                  border_color="red")

                    prompt.configure(
                        text=f"::==> Link incorreto ({link})",
                    )

                    CTkMessagebox(
                        master=self.root,
                        title="Erro!",
                        message=txt2,
                        icon="cancel"
                    )
                    return
                else:
                    cx_link.configure(border_color="light grey")
                # </editor-fold

                # <editor-fold desc="## VALIDAR PLANILHA E CELUCAS##">
                txt3 = "A PLANILHA OU O LOCAL INFORMADO NAO EXISTEM!! :("
                plan = cx_plan.get()
                new_caminho = ""
                if check3.get() == 0:
                    if not func.validar_plan(plan):
                        cx_plan.delete(0, "end")
                        cx_plan.configure(placeholder_text="Arquivo não Encontrado!!",
                                      border_color="red")

                        prompt.configure(
                            text=f"::==> Arquivo não Encontrado!! ({plan})",
                        )

                        CTkMessagebox(
                            master=self.root,
                            title="Erro!",
                            message=txt3,
                            icon="cancel"
                        )
                        return
                    else:
                        cx_plan.configure(border_color="light grey")
                else:
                    prompt.configure(
                        text="::==> CRIANDO PLANILHA...",
                    )
                    new_caminho = filedialog.asksaveasfilename(
                        defaultextension=".xlsx",
                        filetypes=[("Planilhas Excel", "*.xlsx")],
                        title="Salvar nova planilha"
                    )

                    if not new_caminho:
                        prompt.configure(
                            text="::==> Operaço cancelada. :( X",
                        )
                        return

                    wb = Workbook()
                    ws = wb.active
                    ws.title = "Planilha1"
                    wb.save(new_caminho)
                    config["PLANILHA"] = new_caminho
                    self.model.salvar_json("config.json", config)
                    prompt.configure(
                        text=f"::==> Planilha Criada > ({new_caminho})",
                    )
                # </editor-fold

                # <editor-fold desc="##SALVAR DADOS NO BD ##">
                config["LINK"] = link
                config["COLETAR CONQUISTA"] = check1.get()
                config["COLETAR SUB CONQUISTA"] = check2.get()
                if check3.get() == 0:
                    config["PLANILHA"] = plan
                config["CRIAR PLANILHA"] = check3.get()
                config["CELULAS PADÃO"] = check4.get()
                config["CELL1"] = cx_cell1.get() if check4.get() == 0 else "-"
                config["CELL2"] = cx_cell1.get() if check4.get() == 0 else "-"

                self.model.salvar_json("config.json", config)
                config = self.model.carregar_json("config.json")

                # </editor-fold

                # <editor-fold desc="## RASPAGEM DE DADOS ##">
                conquistas, sub_titulos = d_s.begin_data_scraping(config, prompt)
                # </editor-fold
                if not os.path.isfile(config["PLANILHA"]):
                    CTkMessagebox(
                        master=self.root,
                        title="Erro!",
                        message=f"{config["PLANILHA"]}   {new_caminho}",
                        icon="cancel"
                    )
                    prompt.configure(
                        text=f"::==> Arquivo não encontrado ({config["PLANILHA"]})"
                    )
                    return

                # <editor-fold desc="## SALVAR DADOS EM PLANILHA ##">
                save_dados.save_dados(config, conquistas, sub_titulos, prompt, self.root)
                # </editor-fold

                prompt.configure(
                    text="(: (:  CONCLUIDO!.  :) :)",
                )