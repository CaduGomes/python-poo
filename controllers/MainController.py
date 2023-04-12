from controllers.AuthController import AuthController
from views.MainView import MainView
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class MainController:

    def __init__(self) -> None:
        authController = AuthController()

        user = authController.start()

        mainView = MainView(user)

        mainView.start()
