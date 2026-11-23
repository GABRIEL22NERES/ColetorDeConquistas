import customtkinter as ctk

class View:
    def __init__(self, contoller, root, list_widgets):
        self.contoller = contoller
        self.root = root
        self.list_widgets = list_widgets
        self.variables = {
            "variables_default": {
                "font_h1": ("Helvetica", 16, "bold"),
                "font_h2": ("Helvetica", 14, "bold"),
                "font_h3": ("Helvetica", 12, "bold"),
                "font_h4": ("Helvetica", 10, "bold"),
                "font_h5": ("Helvetica", 9, "bold"),
                "font_h6": ("Helvetica", 8),
                "margin_a": 2,
                "margin_b": 3,
                "margin_c": 3,
                "margin_d": 5,
                "margin_e": 10,
                "margin_f": 20,
                "margin_g": 30
            },
            "variables_header": {
                "height": 30
            },
            "variables_body": {
                "x": 0
            },
            "variables_section_coleta": {
                "height": 150
            },
            "variables_section_salvar_dados": {
                "height": 210
            }
        }

    def create_header_screen(self):
        div = ctk.CTkFrame(
            self.root,
            height=self.variables["variables_header"]["height"],
        )
        div.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=self.variables["variables_default"]["margin_d"])

        label_prompt = ctk.CTkLabel(
            div,
            font=self.variables["variables_default"]["font_h3"],
            text="::==> Aguardando!!",
            text_color="yellow",
            anchor="w"
        )
        label_prompt.pack(fill="both", expand=True,
                          padx=self.variables["variables_default"]["margin_d"],
                          pady=self.variables["variables_default"]["margin_c"])


        self.list_widgets.add_widget("header", "label_prompt", label_prompt)

    def create_body_screen(self):

        # <editor-fold desc="SEÇÃO DA COLETA DE DADOS">
        div_coleta = ctk.CTkFrame(
            self.root,
            height=self.variables["variables_section_coleta"]["height"],
            #fg_color="yellow",
        )
        div_coleta.pack_propagate(False)
        div_coleta.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],)

        h1_div_coleta = ctk.CTkLabel(
            div_coleta,
            text="COLETA",
            font=self.variables["variables_default"]["font_h1"],
            height=30,
            #fg_color="blue"
        )
        h1_div_coleta.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"]))
        h4_div_coleta = ctk.CTkLabel(
            div_coleta,
            text="LINK DO SITE",
            font=self.variables["variables_default"]["font_h4"],
            height=20,
            anchor="w",
            #fg_color="red"
        )
        h4_div_coleta.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"]))

        textbox_link = ctk.CTkEntry(
            div_coleta,
            height=30,
            border_width=1,
            border_color="light grey"
        )
        textbox_link.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"]))

        check_var1 = ctk.IntVar(value=1)
        check_var2 = ctk.IntVar(value=1)
        checkbox_1 = ctk.CTkCheckBox(
            div_coleta,
            text="COLETAR CONQUISTAS",
            font=self.variables["variables_default"]["font_h5"],
            variable=check_var1,
            onvalue=1,
            offvalue=0,
            command=lambda: self.contoller.actions_buttons("<<CheckBox1>>")
        )
        checkbox_2 = ctk.CTkCheckBox(
            div_coleta,
            text="COLETAR TITULOS DAS CONQUISTAS",
            font=self.variables["variables_default"]["font_h5"],
            variable=check_var2,
            onvalue=1,
            offvalue=0,
            command=lambda: self.contoller.actions_buttons("<<CheckBox2>>")

        )
        checkbox_1.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"])
                        )
        checkbox_2.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"])
                        )
        #</editor-fold

        # <editor-fold desc="SALVAR DADOS">


        div_save_dados = ctk.CTkFrame(
            self.root,
            height=self.variables["variables_section_salvar_dados"]["height"],
            #fg_color="yellow",
        )
        div_save_dados.pack_propagate(False)
        div_save_dados.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"], )
        h1_div_save_dados = ctk.CTkLabel(
            div_save_dados,
            text="SALVAR DADOS",
            font=self.variables["variables_default"]["font_h1"],
            height=30,
            #fg_color="blue"
        )
        h1_div_save_dados.pack(side="top", fill="x", expand=False,
                           padx=self.variables["variables_default"]["margin_d"],
                           pady=(0,
                                 self.variables["variables_default"]["margin_c"]))
        h4_div_save_dados = ctk.CTkLabel(
            div_save_dados,
            text="PLANILHA",
            font=self.variables["variables_default"]["font_h4"],
            height=20,
            anchor="w",
            #fg_color="blue"
        )
        h4_div_save_dados.pack(side="top", fill="x", expand=False,
                               padx=self.variables["variables_default"]["margin_d"],
                               pady=(0,self.variables["variables_default"]["margin_c"])
                               )
        div_end_plan = ctk.CTkFrame(
            div_save_dados,
            height=30,
        )
        div_end_plan.pack(side="top", fill="x", expand=False,
                          padx=self.variables["variables_default"]["margin_d"],
                          pady=(0,
                                self.variables["variables_default"]["margin_c"]))

        textbox_planilha = ctk.CTkEntry(
            div_end_plan,
            border_width=1,
            border_color="light grey"
        )
        textbox_planilha.pack(side="left", fill="both", expand=True,
                          padx=(0, self.variables["variables_default"]["margin_d"]))
        button_select_end = ctk.CTkButton(
            div_end_plan,
            text=":::",
            width=25,
            command=lambda: self.contoller.actions_buttons("<<ButtonSelectEndPlan>>")
        )
        button_select_end.pack(side="right", fill="y", expand=False,
                              padx=(0, 5), pady=2)

        check_var3 = ctk.IntVar(value=0)
        check_var4 = ctk.IntVar(value=1)
        checkbox_3 = ctk.CTkCheckBox(
            div_save_dados,
            text="CRIAR NOVA PLANILHA",
            font=self.variables["variables_default"]["font_h5"],
            variable=check_var3,
            onvalue=1,
            offvalue=0,
            command = lambda: self.contoller.actions_buttons("<<CheckBox3>>")
        )
        checkbox_3.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"])
                        )
        checkbox_4 = ctk.CTkCheckBox(
            div_save_dados,
            text="COLAR APARTIR DAS CELULAS PADRAO (A2:B2))",
            font=self.variables["variables_default"]["font_h5"],
            variable=check_var4,
            onvalue=1,
            offvalue=0,
            command=lambda: self.contoller.actions_buttons("<<CheckBox4>>")
        )
        checkbox_4.pack(side="top", fill="x", expand=False,
                        padx=self.variables["variables_default"]["margin_d"],
                        pady=(0,
                              self.variables["variables_default"]["margin_c"])
                        )

        container_1_2 = ctk.CTkFrame(
            div_save_dados,
            #fg_color="green"
        )
        container_1_2.pack(side="top", fill="both", expand=True,
                          padx=self.variables["variables_default"]["margin_d"],
                          pady=(0,
                                self.variables["variables_default"]["margin_c"])
                          )
        container_1 = ctk.CTkFrame(
            container_1_2,
            #fg_color="blue"
        )
        container_1.pack(side="left", fill="both", expand=True,
                          padx=(self.variables["variables_default"]["margin_d"], 0),
                          pady=self.variables["variables_default"]["margin_c"]
                          )

        container_2 = ctk.CTkFrame(
            container_1_2,
            #fg_color="red"
        )
        container_2.pack(side="right", fill="both", expand=True,
                          padx=(self.variables["variables_default"]["margin_c"],
                                self.variables["variables_default"]["margin_d"]),
                          pady=self.variables["variables_default"]["margin_c"]
                          )

        label_cell_1 = ctk.CTkLabel(
            container_1,
            text="PRIMEIRA CELULA",
            font=self.variables["variables_default"]["font_h4"],
            height=20,
        )
        text_box_cell_1 = ctk.CTkEntry(
            container_1,
            border_width=0,
            border_color="light grey",
        )
        label_cell_2 = ctk.CTkLabel(
            container_2,
            text="SEGUNDA CELULA",
            font=self.variables["variables_default"]["font_h4"],
            height=20,
        )
        text_box_cell_2 = ctk.CTkEntry(
            container_2,
            border_width=0,
            border_color="light grey",
        )

        label_cell_1.pack(side="top", fill="x", expand=False)
        text_box_cell_1.pack(side="top", fill="both", expand=True)
        text_box_cell_1.configure(state="disabled")
        label_cell_2.pack(side="top", fill="x", expand=False)
        text_box_cell_2.pack(side="top", fill="both", expand=True)
        text_box_cell_2.configure(state="disabled")

        # </editor-fold

        # <editor-fold desc="BOTAO DE SALVAR">
        button_save = ctk.CTkButton(
            self.root,
            text="INICIAR",
            width=200,
            height=80,
            command=lambda: self.contoller.actions_buttons("<<ButtonStart>>")
        )

        button_save.pack(fill="y", expand=False,
                         pady=self.variables["variables_default"]["margin_f"]
                         )
        # </editor-fold


        # <editor-fold desc="ARMAZENAMENTO DOS WIDGETS">
        self.list_widgets.add_widget("div_coleta", "textbox_link", textbox_link)
        self.list_widgets.add_widget("div_coleta", "checkbox_1", checkbox_1)
        self.list_widgets.add_widget("div_coleta", "checkbox_2", checkbox_2)
        self.list_widgets.add_widget("div_salvar_dados", "textbox_planilha", textbox_planilha)
        self.list_widgets.add_widget("div_salvar_dados", "checkbox_3", checkbox_3)
        self.list_widgets.add_widget("div_salvar_dados", "checkbox_4", checkbox_4)
        self.list_widgets.add_widget("div_salvar_dados", "text_box_cell_1", text_box_cell_1)
        self.list_widgets.add_widget("div_salvar_dados", "text_box_cell_2", text_box_cell_2)
        self.list_widgets.add_widget("body", "button_save", button_save)
        # </editor-fold

