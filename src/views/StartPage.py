from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import Menu, ttk

#from ModelMoneytor import ModelMoneytor


root = tk.Tk()
root.geometry('800x450')
root.title('Moneytor Application')

def showProjectsView():

    frame_projects = tk.Frame(main_frame)

    label_welcome = ttk.Label(frame_projects, text='Welcome to the project page')
    label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

    frame_projects.pack()


def showVisualizeView():
    frame_visualize = tk.Frame(main_frame)

    label_welcome = ttk.Label(frame_visualize, text='Welcome to the visualize page')
    label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

    frame_visualize.pack()


def showHomePageView():
    #model = ModelMoneytor()

    # create homepage frame
    frame_homepage = tk.Frame(main_frame)

    label_welcome = ttk.Label(frame_homepage, text='Homepage')
    label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)
            
    frame_homepage.pack()
    
def showAboutView():
    frame_about = tk.Frame(main_frame)

    label_welcome = ttk.Label(frame_about, text='About')
    label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)
            
    frame_about.pack()

def indicate(lb, page): # hide indicator after clicking to the next page
    hide_indicators()
    lb.configure(bg='#158aff')
    delete_pages()
    page()  # showing the next page
    
def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    menu_indicate.config(bg='#c3c3c3')
    contact_indicate.config(bg='#c3c3c3')
    about_indicate.config(bg='#c3c3c3')
        
def delete_pages(): # clear page before dispalying the next one
    for frame in main_frame.winfo_children():
        frame.destroy()

options_frame = tk.Frame(root, bg='#c3c3c3')

#the button itself
home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, showHomePageView))
home_btn.place(x=10,y=50)
#the coloured indicator on the left
home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3,y=50,width=5,height=40)

menu_btn = tk.Button(options_frame, text='Menu', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(menu_indicate, showProjectsView))
menu_btn.place(x=10,y=100)
menu_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
menu_indicate.place(x=3,y=100,width=5,height=40)

contact_btn = tk.Button(options_frame, text='Contact', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(contact_indicate, showVisualizeView))
contact_btn.place(x=10,y=150)
contact_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
contact_indicate.place(x=3,y=150,width=5,height=40)

about_btn = tk.Button(options_frame, text='About', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(about_indicate, showAboutView))
about_btn.place(x=10,y=200)
about_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
about_indicate.place(x=3,y=200,width=5,height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=400)

root.mainloop()