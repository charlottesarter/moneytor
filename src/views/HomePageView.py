import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import END, Menu, ttk
from tkinter import *

import sys

sys.path.insert(1, 'C:/Users/charl/Desktop/moneytor/src/models')

from ModelMoneytor import ModelMoneytor
from Transaction import Transaction

class HomePageView():
    
    def handleMenu(self, root):
        
        ####################### HOMEPAGE #######################
        def showHomePage():

            def addExpense():

                # Build the line to insert in the file
                line = ''

                # 1st : the amount of the transaction
                line += str(getAmount()) + ','

                # 2nd : the currency 
                line += str(getCurrency()) + ','

                # 3rd : the project 
                line += str(getProject()) + ','

                # 4th : the category
                line += str(getCategory()) + ','

                # 5th : the description
                line += str(getDescription()) + ','

                # 6th : expense (true) or income (false)
                line += 'True,'

                # 7th : the date of the day
                line += datetime.datetime.today().strftime('%Y%m%d')

                print(line)

                model.addTransaction(line)

            def getAmount():
                return amount_entry.get()

            def getCurrency():
                cur = currency_var.get()

                if cur == 'EUR':
                    return 1
                elif cur == 'KRW':
                    return 2
                elif cur == 'USD':
                    return 3

            def getProject():
                return project_var.get()
            
            def getCategory():
                return category_var.get()

            def getDescription():
                return description_entry.get()

            for widget in main_frame.winfo_children():
                widget.destroy()
                
            model = ModelMoneytor()
            
            def addFinance():
                pass

            label_homepage = tk.Label(main_frame, text='What\'s new today ' + model.getUserLogged() + ' ?')
            label_homepage.grid(column=0, row=0, sticky=tk.EW, columnspan=4, padx=5, pady=5)

            # create widgets
            # project
            label_project = ttk.Label(main_frame, text='Project')
            label_project.grid(column=0, row=1, sticky=tk.N, columnspan=2, padx=5, pady=5)

            project_var = tk.StringVar()
            # initial menu text
            project_var.set('Daily Life')
            dropdown_project = tk.OptionMenu(main_frame, project_var , *model.getAllProjectsName())  #TODO let the user create a new projects
            dropdown_project.grid(column=0, row=2, sticky=tk.N, columnspan=2, padx=5, pady=5)
            #TODO get the input
            # project entry
            # project_var = tk.StringVar()
            # project_entry = ttk.Entry(main_frame, textvariable=project_var, width=30)
            # project_entry.grid(column=0, row=2, sticky=tk.N, columnspan=4, padx=5, pady=5)

            # category
            label_category = ttk.Label(main_frame, text='Category')
            label_category.grid(column=1, row=1, sticky=tk.N, columnspan=2, padx=5, pady=5)
                
            category_var = tk.StringVar()
            # initial menu text
            category_var.set('Food')
            dropdown_category = tk.OptionMenu(main_frame, category_var, *model.getAllCategories())  #TODO let the user create a new category
            dropdown_category.grid(column=1, row=2, sticky=tk.N, columnspan=2, padx=5, pady=5)
            # category entry
            # category_var = tk.StringVar()
            # category_entry = ttk.Entry(main_frame, textvariable=category_var, width=30)
            # category_entry.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

            # description
            label_description = ttk.Label(main_frame, text='Description')
            label_description.grid(column=0, row=3, sticky=tk.N, padx=5, pady=5)

            # category entry
            description_var = tk.StringVar()
            description_entry = ttk.Entry(main_frame, textvariable=description_var, width=30)
            description_entry.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

            # amount
            label_amount = ttk.Label(main_frame, text='Amount')
            label_amount.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

            # amount entry
            amount_var = tk.IntVar()
            amount_entry = ttk.Spinbox(main_frame, from_=0, to=float('+inf'), textvariable=amount_var, width=30)
            amount_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

            # currency
            label_currency = ttk.Label(main_frame, text='Currency')
            label_currency.grid(column=3, row=3, sticky=tk.N, padx=5, pady=5)

            # currency entry
            currency_var = tk.StringVar()
            currency_var.set('EUR')
            dropdown_currency = tk.OptionMenu(main_frame, currency_var, *['EUR', 'KRW', 'USD'])  #TODO let the user create a new projects
            dropdown_currency.grid(column=2, row=4, sticky=tk.N, columnspan=2, padx=5, pady=5)

            # expense button
            expense_button = ttk.Button(main_frame, text='Expense', command=addExpense) # TODO : define the command of the button 
            expense_button.grid(column=0, row=6, sticky=tk.S, columnspan=4, padx=5, pady=30)

            # income button
            income_button = ttk.Button(main_frame, text='Income') # TODO : define the command of the button 
            income_button.grid(column=0, row=7, sticky=tk.S, columnspan=4, padx=5, pady=5)

        ####################### PROJECTS #######################
        def showProjects():

            for widget in main_frame.winfo_children():
                widget.destroy()

            label_welcome = ttk.Label(main_frame, text='Here is the key information of all of your projects')
            label_welcome.grid(column=0, row=0, sticky=tk.N, columnspan=2, padx=5, pady=5)
            
            my_project = ttk.Treeview(main_frame)

            my_project['columns'] = ('project_name', 'total_expenses', 'total_incomes', 'sold')

            my_project.column("#0", width=0,  stretch=NO)
            my_project.column("project_name",anchor=CENTER, width=80)
            my_project.column("total_expenses",anchor=CENTER,width=80)
            my_project.column("total_incomes",anchor=CENTER,width=80)
            my_project.column("sold",anchor=CENTER,width=80)

            my_project.heading("#0",text="",anchor=CENTER)
            my_project.heading("project_name",text="Name",anchor=CENTER)
            my_project.heading("total_expenses",text="Expenses",anchor=CENTER)
            my_project.heading("total_incomes",text="Incomes",anchor=CENTER)
            my_project.heading("sold",text="Sold",anchor=CENTER)

            # Get all the project and their key information

            model = ModelMoneytor()

            projects_info = []
            for project in model.getAllProjects():
                projects_info.append(project.getKeyInfo())

            for i in range(len(projects_info)):
                my_project.insert(parent='',index='end',iid=i,text='', values=projects_info[i])

            my_project.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)

        ####################### VISUALIZE #######################
        def showVisualize():
            for widget in main_frame.winfo_children():
                widget.destroy()
                
            def exp_by_cat():     #TODO expand the window to match the plot size
                # the figure that will contain the plot
                bar_chart = Figure(figsize = (4, 4), dpi = 100)

                # data
                model = ModelMoneytor()
                exp_by_cat = model.getExpensesByCategory()

                # Here is the code to sort the graph but I don't think it's a good idea because the order of 
                # the list will change all the time so it's impossible to compare it quickly

                # sorted_exp_by_cat = sorted(exp_by_cat.items(), key=lambda x:x[1]) # returns a list
                # sorted_exp_by_cat = dict(sorted_exp_by_cat) # convert the list into a dictionnay

                categories = list(exp_by_cat.keys())
                values = list(exp_by_cat.values())
                
                # adding the subplot
                plot1 = bar_chart.add_subplot(111)
                
                # plotting the graph
                plot1.bar(range(len(exp_by_cat)), values, tick_label=categories)

                # space the x axe labels
                plot1.tick_params(axis='x', which='major', labelsize=6)

                # adding labels for the axes and a title
                plot1.set_title('Expenses by Category')
                plot1.set_xlabel('Category')
                plot1.set_ylabel('Total of Expenses (€)')
                
                # creating the Tkinter canvas containing the Matplotlib figure
                canvas = FigureCanvasTkAgg(bar_chart, master = main_frame)
                canvas.draw()
                
                # placing the canvas on the Tkinter window
                canvas.get_tk_widget().grid(column=1, row=1, sticky=tk.N, rowspan=2, padx=5, pady=5)

            def exp_by_month():     #TODO expand the window to match the plot size
                # the figure that will contain the plot
                bar_chart = Figure(figsize = (4, 4), dpi = 100)

                # data
                model = ModelMoneytor()
                exp_by_month = model.getExpensesByMonth('2022')
                months = list(exp_by_month.keys())
                values = list(exp_by_month.values())
                
                # adding the subplot
                plot1 = bar_chart.add_subplot(111)
                
                # plotting the graph
                plot1.bar(range(len(exp_by_month)), values, tick_label=months)

                # space the x axe labels
                plot1.tick_params(axis='x', which='major', labelsize=8)

                # adding labels for the axes and a title
                plot1.set_title('Expenses by Month')
                plot1.set_xlabel('Month')
                plot1.set_ylabel('Total of Expenses (€)')
                
                # creating the Tkinter canvas containing the Matplotlib figure
                canvas = FigureCanvasTkAgg(bar_chart, master = main_frame)
                canvas.draw()
                
                # placing the canvas on the Tkinter window
                canvas.get_tk_widget().grid(column=1, row=1, sticky=tk.N, rowspan=2, padx=5, pady=5)

            label_welcome = ttk.Label(main_frame, text='Here, you can visualize your data according different settings')
            label_welcome.grid(column=0, row=0, sticky=tk.N, columnspan=2, padx=5, pady=5)

            # button that displays the plot 'expenses by category'
            plot_button = ttk.Button(master=main_frame, command=exp_by_cat, text = "Expenses by category")
            plot_button.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

            # button that displays the plot 'expenses by month'
            plot_button = ttk.Button(master=main_frame, command=exp_by_month, text = "Expenses by month")
            plot_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        
        ####################### ABOUT #######################
        def showAbout():

            for widget in main_frame.winfo_children():
                widget.destroy()
                
            label_amount = ttk.Label(main_frame, text='About')
            label_amount.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)

        ####################### MAIN #######################

        model = ModelMoneytor()

        # create main frame
        main_frame = tk.Frame(root)

        label_main = tk.Label(main_frame, text='Hello, ' + model.getUserLogged() + ', nice to see you on MONEYTOR :)')
        label_main.grid(column=0, row=0, sticky=tk.EW, columnspan=4, padx=5, pady=5)

        main_frame.pack()

        showHomePage()      # to have the Homepage as the first page showing up when opening the app

        #################### Create a menubar ####################
        menubar = Menu(root)
        root.config(menu=menubar)

        # create the homepage_menu
        homepage_menu = Menu(
            menubar,
            tearoff=0
        )
        
        menubar.add_cascade(
            label="Homepage",
            command=showHomePage
        )
        
        menubar.add_cascade(
            label="Projects",
            command=showProjects
        )
        
        menubar.add_cascade(
            label="Visualize",
            command=showVisualize
        )
        
        menubar.add_cascade(
            label="About",
            command=showAbout
        )
        
        menubar.add_cascade(
            label="Exit",
            command=root.destroy
        )