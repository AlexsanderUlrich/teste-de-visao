from models.main import Model
from views.main import View
from views.home import HomeView

class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

        # Cria e registra a view passando o controller
        frame = HomeView(master=self.view.root, controller=self)
        self.view.frames["home"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def ir_para_selecao(self):
        self.view.switch("selecaoDeTestes")
