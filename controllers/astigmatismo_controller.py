from views.main import View
from views.astigmatismo import AstigmatismoView

class AstigmatismoController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = AstigmatismoView(master=self.view.root, controller=self)
        self.view.frames["astigmatismo"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.switch(nome)
