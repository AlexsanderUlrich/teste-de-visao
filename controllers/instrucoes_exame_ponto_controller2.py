from views.main import View
from views.instrucoes_exame_ponto2 import InstrucoesExamePontoView2  # ajuste conforme seu nome real

class InstrucoesExamePontoController2:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesExamePontoView2(master=self.view.root, controller=self)
        self.view.frames["instrucoesExamePonto2"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
