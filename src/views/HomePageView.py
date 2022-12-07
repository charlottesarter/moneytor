from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import Menu, ttk

from ModelMoneytor import ModelMoneytor

class ProjectsView():

    def showProjectsView(self, root):

        frame_projects = tk.Frame(root)

        label_welcome = ttk.Label(frame_projects, text='Welcome to the project page')
        label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

        frame_projects.pack()

class VisualizeView():

    def showVisualizeView(self, root):

        def plot():
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
            canvas = FigureCanvasTkAgg(bar_chart, master = frame_visualize)
            canvas.draw()
            
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().grid(column=0, row=2, sticky=tk.N, padx=5, pady=5)
            
            # creating the Matplotlib toolbar
            # toolbar = NavigationToolbar2Tk(canvas, frame_visualize)
            # toolbar.update()
            # placing the toolbar on the Tkinter window
            # canvas.get_tk_widget().pack()

        frame_visualize = tk.Frame(root)

        label_welcome = ttk.Label(frame_visualize, text='Welcome to the visualize page')
        label_welcome.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

        # button that displays the plot
        plot_button = ttk.Button(master=frame_visualize, command=plot, text = "Plot")
        plot_button.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)

        frame_visualize.pack()

class HomePageView():

    def showHomePageView(self, root):

        # If the user click on the projects button

        def projects():

            # Destroy frame_homepage
            frame_homepage.destroy()

            # Create frame_projects
            projects_view = ProjectsView()
            ProjectsView.showProjectsView(projects_view, root)

        def exp_by_cat():

            # Destroy frame_homepage
            frame_homepage.destroy()

            # Create frame_visualize
            visualize_view = VisualizeView()
            VisualizeView.showVisualizeView(visualize_view, root)

        model = ModelMoneytor()

        # create homepage frame
        frame_homepage = tk.Frame(root)

        text_hello = 'What\'s new today' + model.user_logged + '?'
        label_homepage = tk.Label(frame_homepage, text=text_hello)
        label_homepage.grid(column=0, row=0, sticky=tk.EW, columnspan=4, padx=5, pady=5)

        # create widgets
        # project
        label_project = ttk.Label(frame_homepage, text='Project')
        label_project.grid(column=0, row=1, sticky=tk.N, columnspan=4, padx=5, pady=5)

        # project entry
        project_var = tk.StringVar()
        project_entry = ttk.Entry(frame_homepage, textvariable=project_var, width=30)
        project_entry.grid(column=0, row=2, sticky=tk.N, columnspan=4, padx=5, pady=5)

        # category
        label_category = ttk.Label(frame_homepage, text='Category')
        label_category.grid(column=0, row=3, sticky=tk.N, padx=5, pady=5)

        # category entry
        category_var = tk.StringVar()
        category_entry = ttk.Entry(frame_homepage, textvariable=category_var, width=30)
        category_entry.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

        # description
        label_description = ttk.Label(frame_homepage, text='Description')
        label_description.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

        # category entry
        description_var = tk.StringVar()
        description_entry = ttk.Entry(frame_homepage, textvariable=category_var, width=30)
        description_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        # amount
        label_amount = ttk.Label(frame_homepage, text='Amount')
        label_amount.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)

        # amount entry
        amount_var = tk.StringVar()
        amount_entry = ttk.Entry(frame_homepage, textvariable=category_var, width=30)
        amount_entry.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)

        # currency
        label_currency = ttk.Label(frame_homepage, text='Currency')
        label_currency.grid(column=3, row=3, sticky=tk.N, padx=5, pady=5)

        # currency entry
        currency_var = tk.IntVar()
        currency_entry = ttk.Entry(frame_homepage, textvariable=currency_var, width=30)
        currency_entry.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)

        # expense button
        expense_button = ttk.Button(frame_homepage, text='Expense') # TODO : define the command of the button 
        expense_button.grid(column=0, row=6, sticky=tk.S, columnspan=4, padx=5, pady=30)

        # income button
        income_button = ttk.Button(frame_homepage, text='Income') # TODO : define the command of the button 
        income_button.grid(column=0, row=7, sticky=tk.S, columnspan=4, padx=5, pady=5)
                
        frame_homepage.pack()

        # create a menubar
        menubar = Menu(root)
        root.config(menu=menubar)

        # create the homepage_menu
        homepage_menu = Menu(
            menubar,
            tearoff=0
        )

        # add menu items to the Homepage menu # TODO --> we can remove them if we don't need them
        homepage_menu.add_command(label='New')
        homepage_menu.add_command(label='Open...')
        homepage_menu.add_command(label='Close')
        homepage_menu.add_separator()

        # add Exit menu item (closes the app)
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

        projects_menu.add_command(label='See all', command=projects)

        # add the Projects menu to the menubar
        menubar.add_cascade(
            label="Projects",
            menu=projects_menu,
        )

        # create the Visualize menu
        visualize_menu = Menu(
            menubar,
            tearoff=0
        )

        visualize_menu.add_command(label='Expenses by category', command=exp_by_cat)

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