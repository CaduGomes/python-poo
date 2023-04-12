import tkinter as tk
from tkinter import ttk


class LoginView:

    def __init__(self) -> None:
        self.__mainWindow = tk.Tk()
        self.__mainWindow.title('Login')
        self.__mainWindow.geometry('200x400')

        self.__emailVar = tk.StringVar()
        self.__passwordVar = tk.StringVar()
        self.__errorText = tk.StringVar(value='')

    def start(self, authFunction) -> None:
        email = ttk.Entry(master=self.__mainWindow,
                          textvariable=self.__emailVar)
        password = ttk.Entry(master=self.__mainWindow,
                             textvariable=self.__passwordVar)

        button = ttk.Button(
            master=self.__mainWindow,
            text='Entrar',
            command=lambda: authFunction(self.__emailVar.get(),
                                         self.__passwordVar.get()))

        title = ttk.Label(master=self.__mainWindow, text='Faça login')

        errorText = ttk.Label(master=self.__mainWindow,
                              textvariable=self.__errorText)

        title.pack(pady=5)
        email.pack(pady=5)
        password.pack(pady=5)
        button.pack(pady=5)

        errorText.pack(pady=5)

        self.__mainWindow.mainloop()

    def stop(self) -> None:
        self.__mainWindow.destroy()

    def errorText(self):
        self.__errorText.set('Senha inválida')
