import tkinter as tk
from tkinter import ttk

from models.Transaction import Transaction
from views.MenuView import MenuView
from controllers.MoneytorController import MoneytorController

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Moneytor')

        # create a model
        path_data = 'data/sample_file.csv'
        model = Transaction.initialize(path_data)

        # create a view and place it on the root window
        view = MenuView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = MoneytorController(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
