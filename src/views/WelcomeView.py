import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter.messagebox import showinfo

import sys

# setting path
sys.path.insert(1, 'C:/Users/charl/Desktop/moneytor/src/controllers')
sys.path.insert(1, 'C:/Users/charl/Desktop/moneytor/src/models')

from ModelMoneytor import ModelMoneytor
from views.HomePageView import HomePageView

# If the user click on the 'register' button
class RegisterView():
    
    def __init__(self):

        self.username = ''
        self.password = ''
        self.prefered_currency = 0
    
    def showRegisterView(self, root):

        def register_button_clicked():

            # Get username, password and currency

            self.username = getUsername()
            self.password = getPassword()
            self.prefered_currency = getCurrency()

            model = ModelMoneytor()

            # We add a new user
            model.addUser(str(self.username) + ',' + str(self.password) + ',' + str(self.prefered_currency))
            model.user_logged = self.username

            # Destroy register frame
            frame_register.destroy()

            # Create homepage frame
            homepage_view = HomePageView()
            HomePageView.showHomePageView(homepage_view, root)

        def getUsername():
            return username_entry.get()

        def getPassword():
            return password_entry.get()

        def getCurrency():
            return currency_var.get()

        frame_register = tk.Frame(root)

        # create widgets
        # username
        label_username = ttk.Label(frame_register, text='Username:')
        label_username.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # username entry
        username_var = tk.StringVar()
        username_entry = ttk.Entry(frame_register, textvariable=username_var, width=30)
        username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # password
        label_password = ttk.Label(frame_register, text='Password:')
        label_password.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        # password entry
        password_var = tk.StringVar()
        password_entry = ttk.Entry(frame_register, textvariable=password_var, width=30)
        password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # currency
        label = ttk.Label(frame_register, text='Prefered currency:')
        label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # currency entry
        currency_var = tk.IntVar()
        eur = ttk.Radiobutton(frame_register, text='EUR', variable=currency_var, value=1) # Currency['EUR'].value
        krw = ttk.Radiobutton(frame_register, text='KRW', variable=currency_var, value=2)
        usd = ttk.Radiobutton(frame_register, text='USD', variable=currency_var, value=3)
        eur.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        krw.grid(row=3, column=1, sticky=tk.N, padx=5, pady=5)
        usd.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        # register button
        register_button = ttk.Button(frame_register, text='Register', command=register_button_clicked)
        register_button.grid(column=0, row=5, sticky=tk.S, columnspan=2, padx=5, pady=5)

        # message
        # message_label = ttk.Label(frame_register, text='', foreground='red')
        # message_label.grid(column=0, row=4, sticky=tk.EW, columnspan=2, padx=5, pady=5)

        frame_register.pack()

class LoginView():

    def __init__(self):

        self.username = ''
        self.password = ''


    def showLoginView(self, root):

        def login_button_clicked():

            # Get username and password

            self.username = getUsername()
            self.password = getPassword()

            model = ModelMoneytor()

            # We go throught the list of users and check if the username and password entered by the user are in the database

            for user in model.getAllUsers():
                if user.username == self.username and user.password == self.password:

                    model.user_logged = self.username

                    # Destroy login frame
                    frame_login.destroy()

                    # Create homepage frame
                    homepage_view = HomePageView()
                    HomePageView.showHomePageView(homepage_view, root)


        def getUsername():
            return username_entry.get()

        def getPassword():
            return password_entry.get()

        frame_login = tk.Frame(root)

        label_welcome = ttk.Label(frame_login, text='To see your transactions, please log in first')
        label_welcome.grid(column=0, row=0, sticky=tk.EW, columnspan=2, padx=5, pady=5)

        # username
        label_username = ttk.Label(frame_login, text='Username:')
        label_username.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # username entry
        username = tk.StringVar()
        username_entry = ttk.Entry(frame_login, textvariable=username, width=30)
        username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # password
        label_password = ttk.Label(frame_login, text='Password:')
        label_password.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        # password entry
        password = tk.StringVar()
        password_entry = ttk.Entry(frame_login, textvariable=password, width=30)
        password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(frame_login, text='Log in', command=login_button_clicked)
        login_button.grid(column=0, row=5, sticky=tk.S, columnspan=2, padx=5, pady=5)
                
        frame_login.pack()

        
class WelcomeView():

    def showWelcomeView(root):

        # If the user click on the login button

        def login():

            # Destroy frame_welcome
            frame_welcome.destroy()

            # Create login_frame
            login_view = LoginView()
            LoginView.showLoginView(login_view, root)

        # If the user click on the register button

        def register():

            # Destroy frame_welcome
            frame_welcome.destroy()

            # Create login_frame
            register_view = RegisterView()
            RegisterView.showRegisterView(register_view, root)

        # Welcome page
        
        frame_welcome = tk.Frame(root)

        label_welcome = ttk.Label(frame_welcome, text='Welcome to Moneytor')
        label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

        label_start_1 = ttk.Label(frame_welcome, text='To see your transactions, please log in first')
        label_start_1.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)
                
        button_login = ttk.Button(frame_welcome, text='Log in', command=login)
        button_login.grid(column=0, row=2, sticky=tk.N, padx=10, pady=10)

        button_signup = ttk.Button(frame_welcome, text='Register', command=register)
        button_signup.grid(column=0, row=3, sticky=tk.N, padx=10, pady=10)
                
        frame_welcome.pack()

