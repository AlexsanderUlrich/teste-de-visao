from views.main import View
from views.astigmatismo2 import AstigmatismoView2

class AstigmatismoController2:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = AstigmatismoView2(master=self.view.root, controller=self)
        self.view.frames["astigmatismo2"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.frames[nome].atualizar()
        self.view.switch(nome)
