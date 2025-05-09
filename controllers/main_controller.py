from models.main import Model
from models.auth import Auth
from views.main import View

from .home_controller import HomeController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)

    def start(self) -> None:     
        self.view.switch("home")
        self.view.start_mainloop()
