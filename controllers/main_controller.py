from views.main import View

from .home_controller import HomeController
from .selecao_de_testes_controller import SelecaoDeTestesController
from .instrucoes_daltonismo_controller import InstrucoesDaltonismoController
from .daltonismo_controller import DaltonismoController


class Controller:
    def __init__(self, view: View) -> None:
        self.view = view
        self.home_controller = HomeController(view)
        self.selecao_de_testes_controller = SelecaoDeTestesController(view)
        self.instrucoes_daltonismo_controller = InstrucoesDaltonismoController(view)
        self.instrucoes_daltonismo_controller = DaltonismoController(view)

    def start(self) -> None:     
        self.view.switch("home")
        self.view.start_mainloop()
