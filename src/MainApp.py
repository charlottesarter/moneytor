import tkinter as tk
from controllers.RegisterController import RegisterController
from models.ModelMoneytor import ModelMoneytor
from models.Transaction import Transaction
from views.WelcomeView import WelcomeView

if __name__ == '__main__':

    # Initialization of the model
    model = ModelMoneytor()

    # Create root window of the app
    root = tk.Tk()
    root.geometry('900x610')
    root.title('Moneytor')

    # Show the first view : the welcome page
    WelcomeView.showWelcomeView(root)

    # Run the gui
    root.mainloop()