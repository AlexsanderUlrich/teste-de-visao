from views.main import View
from views.disclaimer import DisclaimerView

class DisclaimerContoller:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = DisclaimerView(master=self.view.root, controller=self)
        self.view.frames["disclaimer"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self, nome: str):
        self.view.frames[nome]
        self.view.switch(nome)
