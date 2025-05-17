from views.main import View
from views.exame_ponto import ExamePontoView

class ExamePontoController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = ExamePontoView(master=self.view.root, controller=self)
        self.view.frames["examePonto"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.switch(nome)
