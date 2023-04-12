from views.LoginView import LoginView
from models.DBConnection import DBConnection
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class AuthController:

    def __init__(self) -> None:
        self.__dbCon = DBConnection('database.json')

    def __isAuthValid(self, email: str, password: str) -> bool:
        for i in self.__dbCon.get('users'):
            if i['email'] == email:
                if i['password'] == password:
                    self._user = i
                    self.__loginView.stop()
        self.__loginView.errorText()

    def start(self) -> dict:
        self.__loginView = LoginView()

        self.__loginView.start(self.__isAuthValid)

        return self._user
