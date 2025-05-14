from models.main import Model
from views.main import View
from views.instrucoes_daltonismo import InstrucoesDaltonismoView  # ajuste conforme seu nome real

class InstrucoesDaltonismoController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

        # Cria e registra a view passando o controller
        frame = InstrucoesDaltonismoView(master=self.view.root, controller=self)
        self.view.frames["instrucoesDaltonismo"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, name: str):
        self.view.switch(name)
