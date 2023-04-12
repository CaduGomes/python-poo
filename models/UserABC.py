from abc import ABC, abstractmethod


class UserABS(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_email(self, email: str) -> None:
        pass

    @abstractmethod
    def set_password(self, password: str) -> None:
        pass

    @abstractmethod
    def isPasswordCorrect(self, password: bool) -> bool:
        pass
