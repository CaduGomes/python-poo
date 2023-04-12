from UserABC import UserABC


class UserPF(UserABC):

    def __init__(self, name: str, email: str, password: str, cpf: str) -> None:
        self.__name = name
        self.__email = email
        self.__password = password
        self.__cpf = cpf

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_password(self, password: str) -> None:
        self.__password = password

    def set_cpf(self, cpf: str) -> str:
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf

    def isPasswordCorrect(self, password: str) -> bool:
        return self.__password == password
