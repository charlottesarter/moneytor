import tkinter as tk
from tkinter import ttk, Tk, Toplevel
from tkinter.messagebox import showinfo

from RegisterView import RegisterView

class WelcomeView(ttk.Frame):

    def login():
        login = Toplevel()

    def register():
        RegisterView()

    #---------------- Startpage ----------------
    # root window
    root = Tk()
    root.geometry('320x150')
    root.title('Moneytor')
    
    frame_login = tk.Frame(root)

    label_welcome = tk.Label(frame_login, text='Welcome to Moneytor', font=('Times New Roman', 15))
    label_welcome.pack()
    label_start_1 = tk.Label(frame_login, text='To see your Transactions please log in first', font=('Times New Roman', 10))
    label_start_1.pack()
            
    button_login = tk.Button(frame_login, text='Log in', command=login)
    button_login.pack()
    button_signup = tk.Button(frame_login, text='Sign up', command=register)
    #button_signup.bind("<Button>", lambda e: RegisterView())
    button_signup.pack()
            
    frame_login.pack()
    
    root.mainloop()

