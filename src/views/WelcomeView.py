import tkinter as tk
from tkinter import ttk, Tk, Toplevel
from tkinter.messagebox import showinfo

import sys

# setting path
sys.path.insert(1, 'C:/Users/charl/Desktop/moneytor/src/controllers')
sys.path.insert(1, 'C:/Users/charl/Desktop/moneytor/src/models')

import RegisterController
import User
from ModelMoneytor import ModelMoneytor
# from controllers.RegisterController import RegisterController

# If the user click on the 'register' button
class RegisterWindow(Toplevel):
    
    def __init__(self, master = None):
        
        super().__init__(master = master)
        self.title("Register")
        self.geometry("320x200")
        label = tk.Label(self, text ="Welcome to Moneytor")
        label.grid(column=0, row=0, sticky=tk.EW, columnspan=2, padx=5, pady=5)

        # create widgets
        # username
        label_username = ttk.Label(self, text='Username:')
        label_username.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # username entry
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(self, textvariable=self.username_var, width=30)
        self.username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # password
        label_password = ttk.Label(self, text='Password:')
        label_password.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        # password entry
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, width=30)
        self.password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # currency
        self.label = ttk.Label(self, text='Prefered currency:')
        self.label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # currency entry
        self.currency_var = tk.IntVar()
        self.eur = ttk.Radiobutton(self, text='EUR', variable=self.currency_var, value=1) # Currency['EUR'].value
        self.krw = ttk.Radiobutton(self, text='KRW', variable=self.currency_var, value=2)
        self.usd = ttk.Radiobutton(self, text='USD', variable=self.currency_var, value=3)
        self.eur.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        self.krw.grid(row=3, column=1, sticky=tk.N, padx=5, pady=5)
        self.usd.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        # register button
        self.register_button = ttk.Button(self, text='Register', command=self.register_button_clicked)
        self.register_button.grid(column=0, row=5, sticky=tk.S, columnspan=2, padx=5, pady=5)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(column=0, row=4, sticky=tk.EW, columnspan=2, padx=5, pady=5)

        # set the controller
        # set_controller(RegisterController(User('', '', '')))
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def register_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        print('coucou')
        if self.controller:
            print('ola')
            self.controller.save(self.username_var.get(), self.password_var.get(), self.currency_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.username_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.username_entry['foreground'] = 'black'
        self.username_var.set('')

        self.password_entry['foreground'] = 'black'
        self.password_var.set('')

        # self.currency_entry['foreground'] = 'black'
        self.currency_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
class WelcomeView():

    def showWelcomeView(root):

        # # Create root window

        # root = Tk()
        # root.geometry('320x200')
        # root.title('Moneytor')

        # If the user click on the login button

        def login():
            model_pipi = ModelMoneytor()

            users = model_pipi.getAllUsers()

            for user in users:
                print(user)


        # def register():
            
        #     registerWindow = Toplevel(root)

        # Start page
        
        frame_login = tk.Frame(root)

        label_welcome = tk.Label(frame_login, text='Welcome to Moneytor', font=('Times New Roman', 15))
        label_welcome.pack()

        label_start_1 = tk.Label(frame_login, text='To see your Transactions please log in first', font=('Times New Roman', 10))
        label_start_1.pack()
                
        button_login = tk.Button(frame_login, text='Log in', command=login)
        button_login.pack()

        button_signup = tk.Button(frame_login, text='Register')
        button_signup.bind("<Button>", lambda e: RegisterWindow())
        button_signup.pack()
                
        frame_login.pack()
        
        root.mainloop()

