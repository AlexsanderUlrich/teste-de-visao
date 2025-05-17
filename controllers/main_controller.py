from views.main import View

from .home_controller import HomeController
from .selecao_de_testes_controller import SelecaoDeTestesController

from .instrucoes_daltonismo_controller import InstrucoesDaltonismoController
from .daltonismo_controller import DaltonismoController

from .instrucoes_exame_ponto_controller import InstrucoesExamePontoController
from .exame_ponto_controller import ExamePontoController

from .instrucoes_exame_ponto_controller2 import InstrucoesExamePontoController2
from .exame_ponto_controller2 import ExamePontoController2

from .resultado_controller import ResultadoController


class Controller:
    def __init__(self, view: View) -> None:
        self.view = view
        self.home_controller = HomeController(view)
        self.selecao_de_testes_controller = SelecaoDeTestesController(view)

        self.instrucoes_daltonismo_controller = InstrucoesDaltonismoController(view)
        self.daltonismo_controller = DaltonismoController(view)

        self.instrucoes_exame_ponto_controller = InstrucoesExamePontoController(view)
        self.exame_ponto_controller = ExamePontoController(view)

        self.instrucoes_exame_ponto_controller2 = InstrucoesExamePontoController2(view)
        self.exame_ponto_controller2 = ExamePontoController2(view)

        self.resultado_controller = ResultadoController(view)

    def start(self) -> None:     
        self.view.switch("home")
        self.view.start_mainloop()
