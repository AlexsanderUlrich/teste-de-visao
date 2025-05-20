from views.main import View

from .home_controller import HomeController
from .selecao_de_testes_controller import SelecaoDeTestesController

from .instrucoes_daltonismo_controller import InstrucoesDaltonismoController
from .daltonismo_controller import DaltonismoController

from .instrucoes_exame_ponto_controller import InstrucoesExamePontoController
from .exame_ponto_controller import ExamePontoController

from .instrucoes_exame_ponto_controller2 import InstrucoesExamePontoController2
from .exame_ponto_controller2 import ExamePontoController2

from .instrucoes_astigmatismo_controller import InstrucoesAstigmatismoController
from .astigmatismo_controller import AstigmatismoController

from .instrucoes_astigmatismo_controller2 import InstrucoesAstigmatismoController2
from .astigmatismo_controller2 import AstigmatismoController2 

from .disclaimer_controller import DisclaimerContoller

from .acuidade_controller import AcuidadeController

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

        self.instrucoes_astigmatismo_contoller = InstrucoesAstigmatismoController(view)
        self.astigmatismo_contoller = AstigmatismoController(view)

        self.instrucoes_astigmatismo_contoller2 = InstrucoesAstigmatismoController2(view)
        self.astigmatismo_contoller2 = AstigmatismoController2(view)

        self.disclaimer_controller = DisclaimerContoller(view)

        self.acuidade_controller = AcuidadeController(view)

        self.resultado_controller = ResultadoController(view)

    def start(self) -> None:     
        self.view.switch("home")
        self.view.start_mainloop()
