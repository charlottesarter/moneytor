import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter.messagebox import showinfo
import time
from PIL import Image, ImageTk

import sys

# setting path
sys.path.insert(1, 'C:/Users/Max Eberlein/OneDrive/Documents/Studium/5. Semester/Open Source Software/Term project/moneytor/moneytor/src/controllers')
sys.path.insert(1, 'C:/Users/Max Eberlein/OneDrive/Documents/Studium/5. Semester/Open Source Software/Term project/moneytor/moneytor/src/models')

#sys.path.insert(1, 'C:/Users/XX') # @Charlotte: maybe you can add your path seperately then we can both test easier
#sys.path.insert(1, 'C:/Users/XX')

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
            
            #check if the data for registering is valid TODO add more restrictions
            if(self.username == ''):
                show_register_error('The username can not be empty')
            elif(self.password == ''):
                show_register_error('please enter a password to register')
            elif(self.prefered_currency == 0):
                show_register_error('please select a preferrd currency to continue')
            else:
                show_register_success()
                
                model = ModelMoneytor()

                # We add a new user
                model.addUser(str(self.username) + ',' + str(self.password) + ',' + str(self.prefered_currency))
                model.user_logged = self.username

                # Destroy register frame
                frame_register.destroy()

                # Create homepage frame
                homepage_view = HomePageView()
                HomePageView.showHomePageView(homepage_view, root)

        # function to return to the start page           
        def back_button_clicked():
            frame_register.destroy()
            WelcomeView.showWelcomeView(root)

        def getUsername():
            return username_entry.get()

        def getPassword():
            return password_entry.get()

        def getCurrency():
            return currency_var.get()
        
        def show_register_error(error_text):
            label_register_error = tk.Label(frame_register, text=error_text, fg='red')
            label_register_error.grid(column=0, row=6, sticky=tk.S, columnspan=2, padx=5, pady=5)
            label_register_error.after(3000, label_register_error.destroy)
        
        def show_register_success(): 
            def increment(*args):
                for i in range(100):
                    progressbar["value"] = i+1
                    frame_register.update()
                    time.sleep(0.015)
            label_register_sucess = tk.Label(frame_register, text='You registered successfully!', fg='green')
            label_register_sucess.grid(column=0, row=6, sticky=tk.S, columnspan=2, padx=5, pady=5)
            label_register_sucess.after(3000, label_register_sucess.destroy)
            
            #create a progressbar to have some time to display the succesfull registering
            progressbar = ttk.Progressbar(frame_register, length=150, cursor='spider',
                                mode="determinate",
                                orient=tk.HORIZONTAL)
            progressbar.grid(column=0, row=7, sticky=tk.S, columnspan=2, padx=5, pady=5)
            increment()

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
        
        # back button
        back_button = ttk.Button(frame_register, text='Back', command=back_button_clicked)
        back_button.grid(column=0, row=10, sticky=tk.S, columnspan=2, padx=5, pady=5)

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
                    
                    show_login_success()
                    model.user_logged = self.username

                    # Destroy login frame
                    frame_login.destroy()

                    # Create homepage frame
                    homepage_view = HomePageView()
                    HomePageView.showHomePageView(homepage_view, root)
                else:
                    show_login_error('Username or Password not correct.')
        
        # function to return to the start page           
        def back_button_clicked():
            frame_login.destroy()
            WelcomeView.showWelcomeView(root)

        def getUsername():
            return username_entry.get()

        def getPassword():
            return password_entry.get()
        
        def show_login_error(error_text):
            label_login_error = tk.Label(frame_login, text=error_text, fg='red')
            label_login_error.grid(column=0, row=6, sticky=tk.S, columnspan=2, padx=5, pady=5)
            label_login_error.after(3000, label_login_error.destroy)
        
        def show_login_success(): 
            def increment(*args):
                for i in range(100):
                    progressbar["value"] = i+1
                    frame_login.update()
                    time.sleep(0.015)
            label_login_sucess = tk.Label(frame_login, text='Welcome back! We are loading your data...', fg='green')
            label_login_sucess.grid(column=0, row=6, sticky=tk.S, columnspan=2, padx=5, pady=5)
            label_login_sucess.after(3000, label_login_sucess.destroy)
            
            #create a progressbar to have some time to display the succesfull registering
            progressbar = ttk.Progressbar(frame_login, length=150, cursor='spider',
                                mode="determinate",
                                orient=tk.HORIZONTAL)
            progressbar.grid(column=0, row=7, sticky=tk.S, columnspan=2, padx=5, pady=5)
            increment()

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
        password_entry = ttk.Entry(frame_login, textvariable=password, show="*", width=30)
        password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        # checkbox to make the password show up / disapear
        def showPassword():     
            if password_entry.cget('show') == '*':
                password_entry.config(show='')
            else:
                password_entry.config(show='*')
        check_button_password = tk.Checkbutton(frame_login, text='show password', command=showPassword)
        check_button_password.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)
                
        # login button
        login_button = ttk.Button(frame_login, text='Log in', command=login_button_clicked)
        login_button.grid(column=0, row=5, sticky=tk.S, columnspan=2, padx=5, pady=5)
        
        # back button
        back_button = ttk.Button(frame_login, text='Back', command=back_button_clicked)
        back_button.grid(column=0, row=10, sticky=tk.S, columnspan=2, padx=5, pady=5)
                
        frame_login.pack()

        
class WelcomeView():

    def showWelcomeView(root):

        # If the user click on the login button

        def login():

            # Destroy frame_welcome
            frame_welcome.destroy()
            label_logo.destroy()    #needs to be destroyed seperately because it sits in the root window

            # Create login_frame
            login_view = LoginView()
            LoginView.showLoginView(login_view, root)

        # If the user click on the register button

        def register():

            # Destroy frame_welcome
            frame_welcome.destroy()
            label_logo.destroy()    #needs to be destroyed seperately because it sits in the root window

            # Create login_frame
            register_view = RegisterView()
            RegisterView.showRegisterView(register_view, root)

        # Welcome page
        
        frame_welcome = tk.Frame(root)
        
        
        # show the logo at the start page
        path_logo = 'C:/Users/Max Eberlein/OneDrive/Documents/Studium/5. Semester/Open Source Software/Term project/Bilder/MoneytorLogo.png'
        image = Image.open(path_logo)
        photo = ImageTk.PhotoImage(image)   #convert the image type

        label_logo = tk.Label(root, image = photo)
        label_logo.image = photo
        label_logo.pack()

        label_welcome = ttk.Label(frame_welcome, text='Welcome to Moneytor')
        label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

        label_start_1 = ttk.Label(frame_welcome, text='To see your transactions, please log in first')
        label_start_1.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)
                
        button_login = ttk.Button(frame_welcome, text='Log in', command=login)
        button_login.grid(column=0, row=2, sticky=tk.N, padx=10, pady=10)
        
        label_start_2 = ttk.Label(frame_welcome, text='If you are new please create an account first')
        label_start_2.grid(column=0, row=3, sticky=tk.N, padx=5, pady=5)

        button_signup = ttk.Button(frame_welcome, text='Register', command=register)
        button_signup.grid(column=0, row=4, sticky=tk.N, padx=10, pady=10)
                
        frame_welcome.pack()

