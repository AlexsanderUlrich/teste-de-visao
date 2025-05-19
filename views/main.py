from typing import TypedDict

from .root import Root
from .home import HomeView
from .selecao_de_testes import SelecaoDeTestesView

from .instrucoes_daltonismo import InstrucoesDaltonismoView
from .daltonismo import DaltonismoView

from .instrucoes_exame_ponto import InstrucoesExamePontoView
from .exame_ponto import ExamePontoView

from .instrucoes_exame_ponto2 import InstrucoesExamePontoView2
from .exame_ponto2 import ExamePontoView2

from .instrucoes_astigmatismo import InstrucoesAstigmatismoView
from .astigmatismo import AstigmatismoView

from .instrucoes_astigmatismo2 import InstrucoesAstigmatismoView2
from .astigmatismo2 import AstigmatismoView2

from .acuidade import AcuidadeView

from .resultado import ResultadoView

class Frames(TypedDict):

    home: HomeView
    selecaoDeTestes: SelecaoDeTestesView
    instrucoesDaltonismo: InstrucoesDaltonismoView
    daltonismo: DaltonismoView
    instrucoesExamePonto: InstrucoesExamePontoView
    examePonto: ExamePontoView
    instrucoesExamePonto2: InstrucoesExamePontoView2
    examePonto2: ExamePontoView2
    resultado: ResultadoView
    


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._add_frame(HomeView, "home")
        self._add_frame(SelecaoDeTestesView, "selecaoDeTestes")
        self._add_frame(InstrucoesDaltonismoView, "instrucoesDaltonismo")
        self._add_frame(DaltonismoView, "daltonismo")
        self._add_frame(InstrucoesExamePontoView,"instrucoesExamePonto")
        self._add_frame(ExamePontoView,"examePonto")
        self._add_frame(InstrucoesExamePontoView2,"instrucoesExamePonto2")
        self._add_frame(ExamePontoView2,"examePonto2")
        self._add_frame(InstrucoesAstigmatismoView,"instrucoesAstigmatismo")
        self._add_frame(AstigmatismoView,"astigmatismo")
        self._add_frame(InstrucoesAstigmatismoView2,"instrucoesAstigmatismo2")
        self._add_frame(AstigmatismoView2,"astigmatismo2")


        self._add_frame(AcuidadeView,"acuidade")

        self._add_frame(ResultadoView, "resultado")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root, controller=self)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def ir_para_selecao(self):
        self.switch("selecaoDeTestes")


    def start_mainloop(self) -> None:
        self.root.mainloop()
