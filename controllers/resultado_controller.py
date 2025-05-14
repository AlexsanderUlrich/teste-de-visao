from models.main import Model
from views.main import View
from views.resultado import ResultadoView
from views.daltonismo import resultado as daltonismo_resultado

class ResultadoController: 
    resultado_do_exame = {
        "titulo": "Visão cromática", 
        "mensagem": "A sua visão cromática parece ser Excelente.",
        "olho_esquerdo": "azul",
        "olho_direito": "azul"
        }
        
    if daltonismo_resultado != []:
        resultado_do_exame = daltonismo_resultado

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

    
