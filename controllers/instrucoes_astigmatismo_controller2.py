from views.main import View
from views.instrucoes_astigmatismo2 import InstrucoesAstigmatismoView2  # ajuste conforme seu nome real

class InstrucoesAstigmatismoController2:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesAstigmatismoView2(master=self.view.root, controller=self)
        self.view.frames["instrucoesAstigmatismo2"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
