import tkinter as tk
from tkinter import ttk


class MainView:

    def __init__(self, userData) -> None:
        self.__mainWindow = tk.Tk()
        self.__mainWindow.title('Sistema')
        self.__mainWindow.geometry('600x600')
        self.__userData = userData

        self.__emailVar = tk.StringVar()

    def start(self) -> None:

        title = ttk.Label(master=self.__mainWindow, text='Sistema de produtos')

        title.pack(pady=5)

        userName = ttk.Label(master=self.__mainWindow,
                             text=self.__userData['name'])

        userName.pack(pady=5)

        self.__mainWindow.mainloop()
