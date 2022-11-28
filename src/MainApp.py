import tkinter as tk
from tkinter import ttk

from models.User import User
from views.LoginView import LoginView
from controllers.LoginController import LoginController

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        model = User('max_eberlein', 'ILikeIt', 3)

        # create a view and place it on the root window
        view = LoginView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = LoginController(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
