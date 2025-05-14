from models.main import Model
from models.auth import Auth
from views.main import View

from .home_controller import HomeController
from .selecao_de_testes_controller import SelecaoDeTestesController
from .instrucoes_daltonismo_controller import InstrucoesDaltonismoController
from .daltonismo_controller import DaltonismoController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.selecao_de_testes_controller = SelecaoDeTestesController(model, view)
        self.instrucoes_daltonismo_controller = InstrucoesDaltonismoController(model, view)
        self.instrucoes_daltonismo_controller = DaltonismoController(model, view)

    def start(self) -> None:     
        self.view.switch("home")
        self.view.start_mainloop()
