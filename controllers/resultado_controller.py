from models.main import Model
from views.main import View
from views.resultado import ResultadoView

class ResultadoController:        
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

        # Cria e registra a view passando o controller
        frame = ResultadoView(master=self.view.root, controller=self)
        self.view.frames["resultado"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.switch(nome)

    
