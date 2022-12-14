import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import END, Menu, ttk
from tkinter import *

import sys
sys.path.insert(1, './src/models')

from ModelMoneytor import ModelMoneytor
from Transaction import Transaction
from models.Currency import Currency

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
                line += datetime.datetime.today().strftime('%Y%m%d') + '\n'

                if(str(getAmount()) == '' or str(getDescription()) == ''):
                    showInputError()
                else:
                    # Add the expense to the model
                    model.addTransaction(line)
                    showAddSuccess('Your Expense has been added successfully!')

            def addIncome():

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
                line += 'False,'

                # 7th : the date of the day
                line += datetime.datetime.today().strftime('%Y%m%d') + '\n'


                if(str(getAmount()) == '' or str(getDescription()) == ''):
                    showInputError()
                else:
                    # Add the income to the model
                    model.addTransaction(line)
                    showAddSuccess('Your Income has been added successfully!')
                    
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
            
            def showAddSuccess(text):
                label_add_sucess = tk.Label(main_frame, text=text, fg='green')
                label_add_sucess.grid(column=0, row=10, sticky=tk.S, columnspan=3, padx=5, pady=5)
                label_add_sucess.after(3000, label_add_sucess.destroy)
                
            def showInputError():
                label_add_sucess = tk.Label(main_frame, text='One or more fields are empty!', fg='red')
                label_add_sucess.grid(column=0, row=10, sticky=tk.S, columnspan=3, padx=5, pady=5)
                label_add_sucess.after(4000, label_add_sucess.destroy)
                
            def addCategory():

                popup = tk.Tk()
                popup.withdraw()

                # the input dialog
                USER_INP = tk.simpledialog.askstring(title="New Category", prompt="Which Category would you like to create?")
                if(USER_INP):   # to make sure a new one was added
                    category_var.set(USER_INP)
                
            def addProject():

                popup = tk.Tk()
                popup.withdraw()

                USER_INP = tk.simpledialog.askstring(title="New Project", prompt="Which Project would you like to create?")
                if(USER_INP):
                    project_var.set(USER_INP)

            for widget in main_frame.winfo_children():  #destroying the old frame
                widget.destroy()
                
            model = ModelMoneytor()
            
            label_homepage = tk.Label(main_frame, text='What\'s new today ' + model.getUserLogged() + ' ?')
            label_homepage.grid(column=0, row=0, sticky=tk.EW, columnspan=2, padx=5, pady=5)

            # create widgets
            # project
            label_project = ttk.Label(main_frame, text='Project')
            label_project.grid(row=1, column=0, sticky=tk.N, columnspan=2, padx=5, pady=5)

            project_var = tk.StringVar()
            # initial menu text
            project_var.set('Daily Life')
            dropdown_project = tk.OptionMenu(main_frame, project_var , *model.getAllProjectsName()) 
            dropdown_project.grid(row=2, column=0, sticky=tk.E, padx=2, pady=5)
            
            add_project_button = ttk.Button(main_frame, text='New project', command=addProject) 
            add_project_button.grid(row=2, column=1, sticky=tk.W, padx=2, pady=5)

            # category
            label_category = ttk.Label(main_frame, text='Category')
            label_category.grid(row=3, column=0, sticky=tk.N, padx=5, pady=5)
                
            category_var = tk.StringVar()
            # initial menu text
            category_var.set('Food')
            dropdown_category = tk.OptionMenu(main_frame, category_var, *model.getAllCategories())  
            dropdown_category.grid(row=4, column=0, sticky=tk.NW, pady=5, padx=15)
            
            add_category_button = ttk.Button(main_frame, text='New category', command=addCategory) 
            add_category_button.grid(row=4, column=0, sticky=tk.NE, pady=5, padx=15)

            # description
            label_description = ttk.Label(main_frame, text='Description')
            label_description.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)

            # description entry
            description_var = tk.StringVar()
            description_entry = ttk.Entry(main_frame, textvariable=description_var, width=30)
            description_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

            # amount
            label_amount = ttk.Label(main_frame, text='Amount')
            label_amount.grid(column=0, row=5, sticky=tk.N, padx=5, pady=5)

            # amount entry
            amount_var = tk.IntVar()
            amount_entry = ttk.Spinbox(main_frame, from_=0, to=float('+inf'), textvariable=amount_var, width=30)
            amount_entry.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)

            # currency
            label_currency = ttk.Label(main_frame, text='Currency')
            label_currency.grid(column=1, row=5, sticky=tk.N, padx=5, pady=5)

            # currency entry
            currency_var = tk.StringVar()
            currency_var.set('EUR')
            dropdown_currency = tk.OptionMenu(main_frame, currency_var, *['EUR', 'KRW', 'USD']) 
            dropdown_currency.grid(column=1, row=6, sticky=tk.N, padx=5, pady=5)

            # expense button
            expense_button = ttk.Button(main_frame, text='Expense', command=addExpense)  
            expense_button.grid(column=0, row=8, sticky=tk.S, columnspan=2, padx=5, pady=30)

            # income button
            income_button = ttk.Button(main_frame, text='Income', command=addIncome) 
            income_button.grid(column=0, row=9, sticky=tk.N, columnspan=2, padx=5)

        ####################### PROJECTS #######################
        def showProjects():

            for widget in main_frame.winfo_children():
                widget.destroy()
                
            model = ModelMoneytor()
            
            if(model.getPreferedCurrecy() == Currency['KRW'].value):
                pref_curr = ' (KRW)'
            elif(model.getPreferedCurrecy() == Currency['USD'].value):
                pref_curr = ' (USD)'
            elif(model.getPreferedCurrecy() == Currency['EUR'].value):
                pref_curr = ' (EUR)'
            else:
                pref_curr = '(We are experiencing some currency issues... Sorry :/)'

            label_welcome = ttk.Label(main_frame, text='Here is the key information of all of your projects')
            label_welcome.grid(column=0, row=0, sticky=tk.NS, columnspan=2, padx=5, pady=5)
            
            label_curr = ttk.Label(main_frame, text='All transactions are displayed in' + pref_curr)
            label_curr.grid(column=0, row=1, sticky=tk.NS, columnspan=2, padx=5, pady=5)
            
            my_project = ttk.Treeview(main_frame)

            my_project['columns'] = ('project_name', 'total_expenses', 'total_incomes', 'total')

            my_project.column("#0", width=0,  stretch=NO)
            my_project.column("project_name",anchor=CENTER, width=150)
            my_project.column("total_expenses",anchor=CENTER,width=150)
            my_project.column("total_incomes",anchor=CENTER,width=150)
            my_project.column("total",anchor=CENTER,width=150)

            my_project.heading("#0",text="",anchor=CENTER)
            my_project.heading("project_name",text="Name",anchor=CENTER)
            my_project.heading("total_expenses",text="Expenses",anchor=CENTER)
            my_project.heading("total_incomes",text="Incomes",anchor=CENTER)
            my_project.heading("total",text="Sold",anchor=CENTER)

            # Get all the project and their key information

            projects_info = []
            for project in model.getAllProjects():
                projects_info.append(project.getKeyInfo())

            for i in range(len(projects_info)):
                my_project.insert(parent='',index='end',iid=i,text='', values=projects_info[i])

            my_project.grid(column=0, row=2, sticky=tk.N, padx=5, pady=5)

        ####################### VISUALIZE #######################
        def showVisualize():
            for widget in main_frame.winfo_children():
                widget.destroy()

            def getYear():
                return year_var.get()
                
            def exp_by_cat():     #TODO expand the window to match the plot size
                # the figure that will contain the plot
                bar_chart = Figure(figsize = (7, 4), dpi = 100)

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
                
                if(model.getPreferedCurrecy() == Currency['KRW'].value):
                    pref_curr = ' (KRW)'
                elif(model.getPreferedCurrecy() == Currency['USD'].value):
                    pref_curr = ' (USD)'
                elif(model.getPreferedCurrecy() == Currency['EUR'].value):
                    pref_curr = ' (EUR)'
                else:
                    pref_curr = '(We are experiencing some currency issues... Sorry :/)'

                plot1.set_ylabel('Total of Expenses' + pref_curr)
                
                # creating the Tkinter canvas containing the Matplotlib figure
                canvas = FigureCanvasTkAgg(bar_chart, master = main_frame)
                canvas.draw()
                
                # placing the canvas on the Tkinter window
                canvas.get_tk_widget().grid(column=1, row=2, sticky=tk.N, rowspan=2, padx=5, pady=5)

            def exp_by_month():     #TODO expand the window to match the plot size
                # the figure that will contain the plot
                bar_chart = Figure(figsize = (7, 4), dpi = 100)

                # data
                model = ModelMoneytor()
                exp_by_month = model.getExpensesByMonth(getYear())
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
                
                if (model.getPreferedCurrecy() == Currency['KRW'].value):
                    pref_curr = ' (KRW)'
                elif (model.getPreferedCurrecy() == Currency['USD'].value):
                    pref_curr = ' (USD)'
                elif (model.getPreferedCurrecy() == Currency['EUR'].value):
                    pref_curr = ' (EUR)'
                else:
                    pref_curr = '(We are experiencing some currency issues... Sorry :/)'

                plot1.set_ylabel('Total of Expenses' + pref_curr)
                
                # creating the Tkinter canvas containing the Matplotlib figure
                canvas = FigureCanvasTkAgg(bar_chart, master = main_frame)
                canvas.draw()
                
                # placing the canvas on the Tkinter window
                canvas.get_tk_widget().grid(column=1, row=2, sticky=tk.N, rowspan=2, padx=5, pady=5)

            model = ModelMoneytor()

            if (model.getPreferedCurrecy() == Currency['KRW'].value):
                pref_curr = ' (KRW)'
            elif (model.getPreferedCurrecy() == Currency['USD'].value):
                pref_curr = ' (USD)'
            elif (model.getPreferedCurrecy() == Currency['EUR'].value):
                pref_curr = ' (EUR)'
            else:
                pref_curr = '(We are experiencing some currency issues... Sorry :/)'

            label_welcome = ttk.Label(main_frame, text='Here, you can visualize your data according different settings')
            label_welcome.grid(column=0, row=0, sticky=tk.NS, columnspan=2, padx=5, pady=5)
            
            label_sorry_for_the_wait = ttk.Label(main_frame, text='This can take up to 10s because we are using real time data to transfer all of the transactions in ' + pref_curr)
            label_sorry_for_the_wait.grid(column=0, row=1, sticky=tk.NS, columnspan=2, padx=5, pady=5)

            # button that displays the plot 'expenses by category'
            plot_button = ttk.Button(master=main_frame, command=exp_by_cat, text = "Expenses by category")
            plot_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

            # button that displays the plot 'expenses by month'
            plot_button = ttk.Button(master=main_frame, command=exp_by_month, text = "Expenses by month")
            plot_button.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

            # year
            year_var = tk.StringVar()
            # initial year text
            year_var.set('2022')
            dropdown_category = tk.OptionMenu(main_frame, year_var, *model.getAllYears())  
            dropdown_category.grid(row=4, column=0, sticky=tk.NW, pady=5, padx=15)
        
        ####################### ABOUT #######################
        def showAbout():

            for widget in main_frame.winfo_children():
                widget.destroy()

            about_title1 = 'ABOUT MONEYTOR\n'
            label_title1 = ttk.Label(main_frame, text=about_title1)
            label_title1.grid(column=0, row=0, sticky=tk.NS, padx=10, pady=10)
                
            about_text1 = 'Welcome in the new product of our young startup, MONEYTOR!\n\nMONEYTOR is an application that help you manage and organize your transactions.\nIt allows you to easily track your expenses and see where your money is going.\nWith MONEYTOR, you can set budgets, see your spending habits, and stay on top of your financial goals.\nWhether you are trying to save money, pay off debt, or just want to gain control of your transactions, MONEYTOR is here to help.\nGive it a try and see how easy it is to take control of your money with our app.'
            label_about1 = ttk.Label(main_frame, text=about_text1)
            label_about1.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

            about_title2 = '\nOUR TEAM\n'
            label_title2 = ttk.Label(main_frame, text=about_title2)
            label_title2.grid(column=0, row=2, sticky=tk.NS, padx=10, pady=10)
            
            about_text2 = 'Our team consists of two members who are passionate about helping people take control of their transactions.\nBoth of us have experience in the finance industry and have a deep understanding of the challenges that come with managing money.\nWe created MONEYTOR because we saw a need for a simple and effective way to track expenses and stay on top of your financial goals.\nWe believe that with the right tools, anyone can master their transactions and achieve their financial dreams.\nWe are excited to share our app with you and hope it helps you on your financial journey.'
            label_about2 = ttk.Label(main_frame, text=about_text2)
            label_about2.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

            info_title = '\nINFORMATION\n'
            label_info_title = ttk.Label(main_frame, text=info_title)
            label_info_title.grid(column=0, row=4, sticky=tk.NS, padx=10, pady=10)
            
            impressum_text = 'Impressum: MONEYTOR is a fictional company created for the purpose of this exercise.\nHeadquarters: London, UK\nContact: info@moneytor.com\nFounders: Charlotte Sarter & Max Eberlein\nRegistration number: 31415926\nVAT number: 27182818\nDisclaimer: MONEYTOR is not a real company and does not offer any products or services.\nThe information provided in this impressum is for illustrative purposes only.'
            label_impressum = ttk.Label(main_frame, text=impressum_text)
            label_impressum.grid(column=0, row=5, sticky=tk.W, padx=10, pady=10)
            
            disclaimer_text = 'The text for this "About" page was generated only using the open AI ChatGPT.\nmore Information: https://openai.com/blog/chatgpt/'
            label_diclaimer = ttk.Label(main_frame, text=disclaimer_text, foreground='blue')
            label_diclaimer.grid(column=0, row=10, sticky=tk.W, padx=5, pady=5)

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