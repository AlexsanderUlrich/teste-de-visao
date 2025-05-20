from views.main import View
from views.home import HomeView

class HomeController:
    def __init__(self, view: View) -> None:
        self.view = view

        # Cria e registra a view passando o controller
        frame = HomeView(master=self.view.root, controller=self)
        self.view.frames["home"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.frame = frame

    def switch(self):
        self.view.switch("disclaimer")
