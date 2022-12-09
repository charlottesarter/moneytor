from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import Menu, ttk

from ModelMoneytor import ModelMoneytor
#from views.WelcomeView import WelcomeView

class HomePageView():
    
    def handle_Menu(self, root):
        
        ####################### HOMEPAGE #######################
        def show_homepage():
            for widget in main_frame.winfo_children():
                widget.destroy()
                
            model = ModelMoneytor()

            text_hello = 'What\'s new today' + model.user_logged + '?'  # TODO display name
            label_homepage = tk.Label(main_frame, text=text_hello)
            label_homepage.grid(column=0, row=0, sticky=tk.EW, columnspan=4, padx=5, pady=5)

            # create widgets
            # project
            label_project = ttk.Label(main_frame, text='Project')
            label_project.grid(column=0, row=1, sticky=tk.N, columnspan=4, padx=5, pady=5)

            default_project = tk.StringVar()
            # initial menu text
            default_project.set( "Life" )
            dropdown_category = tk.OptionMenu(main_frame, default_project , *model.getAllProjects())  #TODO let the user create a new category
            dropdown_category.grid(column=0, row=2, sticky=tk.N, columnspan=4, padx=5, pady=5)
            # project entry
            # project_var = tk.StringVar()
            # project_entry = ttk.Entry(main_frame, textvariable=project_var, width=30)
            # project_entry.grid(column=0, row=2, sticky=tk.N, columnspan=4, padx=5, pady=5)

            # category
            label_category = ttk.Label(main_frame, text='Category')
            label_category.grid(column=0, row=3, sticky=tk.N, padx=5, pady=5)
                
            default_category = tk.StringVar()
            # initial menu text
            default_category.set( "Food" )
            dropdown_category = tk.OptionMenu(main_frame, default_category , *model.getAllCategories())  #TODO let the user create a new category
            dropdown_category.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
            # category entry
            # category_var = tk.StringVar()
            # category_entry = ttk.Entry(main_frame, textvariable=category_var, width=30)
            # category_entry.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

            # description
            label_description = ttk.Label(main_frame, text='Description')
            label_description.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

            # category entry
            description_var = tk.StringVar()
            description_entry = ttk.Entry(main_frame, textvariable=description_var, width=30)
            description_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

            # amount
            label_amount = ttk.Label(main_frame, text='Amount')
            label_amount.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)

            # amount entry
            amount_var = tk.StringVar()
            amount_entry = ttk.Entry(main_frame, textvariable=amount_var, width=30)
            amount_entry.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)

            # currency
            label_currency = ttk.Label(main_frame, text='Currency')
            label_currency.grid(column=3, row=3, sticky=tk.N, padx=5, pady=5)

            # currency entry
            currency_var = tk.IntVar()
            currency_entry = ttk.Entry(main_frame, textvariable=currency_var, width=30)
            currency_entry.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)

            # expense button
            expense_button = ttk.Button(main_frame, text='Expense') # TODO : define the command of the button 
            expense_button.grid(column=0, row=6, sticky=tk.S, columnspan=4, padx=5, pady=30)

            # income button
            income_button = ttk.Button(main_frame, text='Income') # TODO : define the command of the button 
            income_button.grid(column=0, row=7, sticky=tk.S, columnspan=4, padx=5, pady=5)

        ####################### PROJECTS #######################
        def show_projects():
            for widget in main_frame.winfo_children():
                widget.destroy()

            label_welcome = ttk.Label(main_frame, text='Welcome to the project page')
            label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

            main_frame.pack()

        ####################### VISUALIZE #######################
        def show_exp_by_cat():
            for widget in main_frame.winfo_children():
                widget.destroy()
                
            def plot():     #TODO expand the window to match the plot size
                # the figure that will contain the plot
                bar_chart = Figure(figsize = (5, 5), dpi = 100)

                # data
                model = ModelMoneytor()
                exp_by_cat = model.getExpensesByCategory()
                categories = list(exp_by_cat.keys())
                values = list(exp_by_cat.values())
                
                # adding the subplot
                plot1 = bar_chart.add_subplot(111)
                
                # plotting the graph
                plot1.bar(range(len(exp_by_cat)), values, tick_label=categories)

                # space the x axe labels
                plot1.tick_params(axis='x', which='major', labelsize=8)

                # adding labels for the axes and a title
                plot1.set_title('Expenses by Category')
                plot1.set_xlabel('Category')
                plot1.set_ylabel('Total of Expenses (€)')
                
                # creating the Tkinter canvas containing the Matplotlib figure
                canvas = FigureCanvasTkAgg(bar_chart, master = main_frame)
                canvas.draw()
                
                # placing the canvas on the Tkinter window
                canvas.get_tk_widget().grid(column=0, row=2, sticky=tk.N, padx=5, pady=5)
                
                # creating the Matplotlib toolbar
                # toolbar = NavigationToolbar2Tk(canvas, main_frame)
                # toolbar.update()
                # placing the toolbar on the Tkinter window
                # canvas.get_tk_widget().pack()

            label_welcome = ttk.Label(main_frame, text='Welcome to the visualize page')
            label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

            # button that displays the plot
            plot_button = ttk.Button(master=main_frame, command=plot, text = "Plot")
            plot_button.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)
        
        ####################### ABOUT #######################
        def show_about():
            for widget in main_frame.winfo_children():
                widget.destroy()
                
            label_amount = ttk.Label(main_frame, text='About')
            label_amount.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)
        
        ####################### LOGOUT #######################
        def show_logout():
            # welcome_view = WelcomeView()
            # WelcomeView.showWelcomeView(self)
            root.destroy    #TODO redirect to welcome view instead of closing the window

        model = ModelMoneytor()

        # create homepage frame
        main_frame = tk.Frame(root)

        label_homepage = tk.Label(main_frame, text='this is the main frame')
        label_homepage.grid(column=0, row=0, sticky=tk.EW, columnspan=4, padx=5, pady=5)

        main_frame.pack()


        ############# create a menubar #############
        menubar = Menu(root)
        root.config(menu=menubar)

        # create the homepage_menu
        homepage_menu = Menu(
            menubar,
            tearoff=0
        )
        
        menubar.add_cascade(
            label="Homepage",
            command=show_homepage
        )
        
        menubar.add_cascade(
            label="Projects",
            command=show_projects
        )
        
        menubar.add_cascade(
            label="Visualize",
            command=show_exp_by_cat
        )
        
        menubar.add_cascade(
            label="About",
            command=show_about
        )
        
        menubar.add_cascade(
            label="Logout",
            command=show_logout
        )