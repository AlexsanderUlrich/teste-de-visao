from views.main import View
from views.acuidade import AcuidadeView

class AcuidadeController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = AcuidadeView(master=self.view.root, controller=self)
        self.view.frames["acuidade"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.frames[nome].atualizar()
        self.view.switch(nome)
