from views.main import View
from views.instrucoes_acuidade import InstrucoesAcuidadeView

class InstrucoesAcuidadeController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesAcuidadeView(master=self.view.root, controller=self)
        self.view.frames["instrucoesAcuidade"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
