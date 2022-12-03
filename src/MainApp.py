import tkinter as tk
from controllers.RegisterController import RegisterController
from models.ModelMoneytor import ModelMoneytor
from models.Transaction import Transaction
from views.WelcomeView import WelcomeView


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Moneytor')

#         # create a model TODO
#         path_data = 'data/sample_file.csv'
#         model = Transaction.initialize(path_data)


#         # create a view and place it on the root window
#         view = WelcomeView(self)
#         view.grid(row=0, column=0, padx=10, pady=10)

#         # create a controller
#         controller = RegisterController(model, view)

#         # set the controller to view
#         view.set_controller(controller)


if __name__ == '__main__':

    # Initialization of the model

    model = ModelMoneytor()

    model.addUser('toto,bla,2')

    users = model.getAllUsers()
    for user in users:
        print(user)

    # welcomeView.showView() --> mettre le code dans showView()
    
    # app = App()
    # app.mainloop()
    
#TODO how do we handle, if the whole page changes, for example for signup when we click next after each step?
