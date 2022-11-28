import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class LoginView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # username
        self.label = ttk.Label(self, text='Username:')
        self.label.grid(row=1, column=0)

        # password
        self.label = ttk.Label(self, text='Password:')
        self.label.grid(row=2, column=0)

        # username entry
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(self, textvariable=self.username_var, width=30)
        self.username_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # password entry
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, width=30)
        self.password_entry.grid(row=2, column=1, sticky=tk.NSEW)

        # currency
        self.label = ttk.Label(self, text='Prefered currency:')
        self.label.grid(row=3, column=0)

        # currency entry
        self.currency_var = tk.StringVar()
        self.currency_entry = ttk.Entry(self, textvariable=self.currency_var, width=30)
        self.currency_entry.grid(row=3, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=5, column=0, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=4, column=0, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
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

        self.currency_entry['foreground'] = 'black'
        self.currency_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''