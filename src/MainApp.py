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
    root.geometry('800x450')
    root.title('Moneytor')
    root.resizable(0, 0)

    # Show the first view : the welcome page
    WelcomeView.showWelcomeView(root)

    # Run the gui
    root.mainloop()