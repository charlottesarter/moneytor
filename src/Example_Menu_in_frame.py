import tkinter as tk
LARGE_FONT = ("Verdana", 12)

class Window(tk.Tk):
    """ Main class """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in (Main, Checker):
            current_frame = frame(container, self)
            self.frames[frame] = current_frame
            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):
        """ Raises a particular frame, bringing it into view """

        frame = self.frames[cont]
        frame.tkraise()

def qprint(quick_print):
    """ Function to print a string """
    print(quick_print)

class Main(tk.Frame):
    """ Main frame of program """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        menubar = tk.Menu(controller)
        menubar.add_command(label="Checker", command=lambda: controller.show_frame(Checker))
        controller.config(menu=menubar)

class Checker(tk.Frame):
    """ Password Strength Checker """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Password Checker", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


APP = Window()
APP.geometry("350x200")
APP.mainloop()