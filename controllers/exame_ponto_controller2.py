from views.main import View
from views.exame_ponto2 import ExamePontoView2

class ExamePontoController2:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = ExamePontoView2(master=self.view.root, controller=self)
        self.view.frames["examePonto2"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.frames[nome].atualizar()
        self.view.switch(nome)
