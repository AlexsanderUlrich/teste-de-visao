from views.main import View
from views.selecao_de_testes import SelecaoDeTestesView  # ajuste conforme seu nome real

class SelecaoDeTestesController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = SelecaoDeTestesView(master=self.view.root, controller=self)
        self.view.frames["selecaoDeTestes"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
