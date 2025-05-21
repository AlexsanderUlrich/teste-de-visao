from views.main import View
from views.instrucoes_acuidade2 import InstrucoesAcuidadeView2  # ajuste conforme seu nome real

class InstrucoesAcuidadeController2:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesAcuidadeView2(master=self.view.root, controller=self)
        self.view.frames["instrucoesAcuidade2"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
