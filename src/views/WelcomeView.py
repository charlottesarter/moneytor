import tkinter as tk
from tkinter import ttk, Tk, Toplevel, Menu, Frame
from tkinter.messagebox import showinfo

from views.RegisterView import RegisterView

class WelcomeView(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        print('LOLOLOL')
        
        #---------------- Startpage ----------------

        self.frame_login = tk.Frame(self)

        self.label_welcome = tk.Label(self.frame_login, text='Welcome to Moneytor', font=('Times New Roman', 15))
        self.label_welcome.pack()
        
        self.label_start_1 = tk.Label(self.frame_login, text='To see your Transactions please log in first', font=('Times New Roman', 10))
        self.label_start_1.pack()
        self.button_login = tk.Button(self.frame_login, text='Log in', command=self.login_pressed)
        self.button_login.pack()
        
        self.label_start_2 = tk.Label(self.frame_login, text='To get started, please create an account', font=('Times New Roman', 10))
        self.label_start_2.pack()
        self.button_signup = tk.Button(self.frame_login, text='Sign up', command=self.register_pressed)
        #button_signup.bind("<Button>", lambda e: RegisterView())
        self.button_signup.pack()
        
        
        
        self.skip_login = tk.Label(self.frame_login, text='Skip (for testing only)')
        self.skip_login.pack()
        self.button_skip_login = tk.Button(self.frame_login, text='Skip', command=self.skip_pressed)
        self.button_skip_login.pack()
        
        
        
                
        self.frame_login.pack()

        # set the controller
        self.controller = None      #TODO why is the controller set to None?
    
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def login_pressed(self):
        if self.controller:
            self.controller.login()
            
    def register_pressed(self):
        if self.controller:
            self.controller.register()
            
    def skip_pressed(self):
        if self.controller:
            self.controller.start_moneytor()
            
    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.label_welcome = tk.Label(self.frame_login, text=message)
        self.label_welcome.pack()
        
    def show_login(self):
        pass
        
    def show_register(self):
        pass
    
    def start_moneytor(self):       #TODO add the code from MenuView.py here
        
        # self.frame_login.destroy()

        # root = tk.Tk()
        # root.withdraw()

        # toplevel = tk.Toplevel(root)

        # # create a toplevel menu
        # menubar = tk.Menu(toplevel)
        # menubar.add_command(label="Hello!")
        # menubar.add_command(label="Quit!", command=root.quit)

        # # display the menu
        # toplevel.config(menu=menubar)

        # root.mainloop()
        
        
        self.a_frame = FrameWithMenu(self)
        self.create_menu()

    def create_menu(self):
        self.menubar = tk.Menu(self)
        self.menubar.add_command(label="Root", command=self.a_frame.replace_menu)
        self['menu'] = self.menubar



class FrameWithMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def replace_menu(self):
        """ Overwrite parent's menu if parent's class name is in _valid_cls_names.
        """

        _parent_cls_name = type(self.master).__name__
        _valid_cls_names = ("Tk", "Toplevel", "Root")
        if _parent_cls_name in _valid_cls_names:
            self.menubar = tk.Menu(self)
            self.menubar.add_command(label="Frame", command=self.master.create_menu)
            self.master['menu'] = self.menubar