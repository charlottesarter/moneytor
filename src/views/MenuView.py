import tkinter as tk
from tkinter import Tk, Frame, Menu, ttk

class MenuView(ttk.Frame):

    # root window
    root = Tk()
    root.geometry('320x150')
    root.title('Moneytor')


    # create a menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    # create the homepage_menu
    homepage_menu = Menu(
        menubar,
        tearoff=0
    )

    # add menu items to the Homepage menu
    homepage_menu.add_command(label='New')
    homepage_menu.add_command(label='Open...')
    homepage_menu.add_command(label='Close')
    homepage_menu.add_separator()

    # add Exit menu item
    homepage_menu.add_command(
        label='Exit',
        command=root.destroy
    )

    # add the Homepage menu to the menubar
    menubar.add_cascade(
        label="Homepage",
        menu=homepage_menu
    )

    # create the Projects menu
    projects_menu = Menu(
        menubar,
        tearoff=0
    )

    # add the Projetcs menu to the menubar
    menubar.add_cascade(
        label="Projects",
        menu=projects_menu
    )

    # create the Visualize menu
    visualize_menu = Menu(
        menubar,
        tearoff=0
    )

    # add the Visualize menu to the menubar
    menubar.add_cascade(
        label="Visualize",
        menu=visualize_menu
    )

    # create the Help menu
    help_menu = Menu(
        menubar,
        tearoff=0
    )

    help_menu.add_command(label='Welcome')
    help_menu.add_command(label='About...')

    # add the Help menu to the menubar
    menubar.add_cascade(
        label="Help",
        menu=help_menu
    )

    root.mainloop()

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller