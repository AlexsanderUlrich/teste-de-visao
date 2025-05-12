from typing import TypedDict

from .root import Root
from .home import HomeView
from .selecao_de_testes import SelecaoDeTestesView
from .disclaimer import DisclaimerView
from .instrucoes_daltonismo import InstrucoesDaltonismoView

class Frames(TypedDict):

    home: HomeView
    selecaoDeTestes: SelecaoDeTestesView
    disclaimer: DisclaimerView
    instrucoesDaltonismo: InstrucoesDaltonismoView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._add_frame(SelecaoDeTestesView, "selecaoDeTestes")
        self._add_frame(DisclaimerView, "disclaimer")
        self._add_frame(InstrucoesDaltonismoView, "instrucoesDaltonismo")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
