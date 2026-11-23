import customtkinter as ctk
from controller.controller import Controller

class AppTela:
    def __init__(self):
        #<editor-fold desc="CONSTRUTOR DA TELA PRINCIPAL">
        self.root = ctk.CTk()
        self.root.title("Coletor de Conquistas")
        self.root_width_min = 500
        self.root_height_min = 490
        self.root.geometry(f"{self.root_width_min}x{self.root_height_min}")
        self.root.minsize( self.root_width_min,  self.root_height_min)
        self.root.maxsize( self.root_width_min, self.root_height_min)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.controller = Controller(self)


        #<editor-fold desc="CONTRUTOR DOS ELEMENTOS DA TELA">
        self.controller.create_main_screen()
        # </editor-fold

        self.root.update()
        self.root.mainloop()

if __name__ == "__main__":
    app = AppTela()