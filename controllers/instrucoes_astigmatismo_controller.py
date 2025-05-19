from views.main import View
from views.instrucoes_astigmatismo import InstrucoesAstigmatismoView

class InstrucoesAstigmatismoController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesAstigmatismoView(master=self.view.root, controller=self)
        self.view.frames["instrucoesAstigmatismo"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
