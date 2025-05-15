from views.main import View
from controllers.main_controller import Controller


def main():
    view = View()
    controller = Controller(view)
    controller.start()


if __name__ == "__main__":
    main()
