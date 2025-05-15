from models.main import Model
from views.main import View
from views.daltonismo import DaltonismoView

class DaltonismoController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

        # Cria e registra a view passando o controller
        frame = DaltonismoView(master=self.view.root, controller=self)
        self.view.frames["daltonismo"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.frames[nome].atualizar()
        self.view.switch(nome)
