from views.main import View
from views.instrucoes_exame_ponto import InstrucoesExamePontoView  # ajuste conforme seu nome real

class InstrucoesExamePontoController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesExamePontoView(master=self.view.root, controller=self)
        self.view.frames["instrucoesExamePonto"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
