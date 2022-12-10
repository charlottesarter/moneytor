# Moneytor model (singleton)

from models.Project import Project
from models.Currency import Currency
from models.Transaction import Transaction
from models.User import User
from forex_python.converter import CurrencyRates    # please install: pip install forex-python

class ModelMoneytor(object):

    # Initialization of the model (from the files users.csv and transactions.csv)
    def __init__(self):

        # The list of all of the users of the app (users.csv)
        self.users = [] 

        fd = open('data/users.csv', 'r')
        lines = fd.readlines()
        fd.close

        for line in lines:
            # line = line.rstrip()
            self.users.append(User(line))

        # The list of all of the transactions of one user 
        
        self.transactions = []

        fd = open('data/transactions.csv', 'r')
        lines = fd.readlines()
        fd.close

        for line in lines:
            # line = line.rstrip()
            self.transactions.append(Transaction(line))

        # Remove the titles of the file transactions.csv
        self.transactions.pop(0)

        # The list of all the projects of one user 

        projects_names = []
        self.projects = []

        for transaction in self.transactions:
            if transaction.project not in projects_names:
                projects_names.append(transaction.project) # Add the name of the project in the list of projects' names
                self.projects.append(Project(transaction.project)) # Create a new project and add it to the model

        # Add all the corresponding transactions to the projects

        for transaction in self.transactions:
            for project in self.projects:
                if transaction.project == project.name:
                    project.addTransaction(transaction)
            
        # Save the current user who is logged in the app
        self.user_logged = ''

    # Make sure that there is only one model (singleton)

    def __new__(model):
        if not hasattr(model, 'instance'):
            model.instance = super(ModelMoneytor, model).__new__(model)
        return model.instance

    # Add a new user

    def addUser(self, line):
        new_user = User(line)
        new_user.save()
        self.users.append(new_user)

    # Returns the list of all of the users

    def getAllUsers(self):
        return self.users

    # Returns the list of all of the transactions

    def getAllTransactions(self):
        return self.transactions

    # Returns the list of all the categories of expenses

    def getAllCategories(self):
        
        categories = []

        for transaction in self.transactions:
            
            if transaction.category not in categories:
                categories.append(transaction.category)
        
        return categories
    
    def getAllProjects(self):  
        return self.projects

    # Returns a dictionary : {'category':total of expenses in this category}

    def getExpensesByCategory(self):

        exp_by_cat = {}

        for transaction in self.transactions:
            if transaction.category in exp_by_cat:
                if transaction.expense:
                    # We have to convert all the expenses in the same currency (EUR)
                    if int(transaction.currency) == Currency['KRW'].value:
                        exp_by_cat[transaction.category] += float(transaction.amount) * 0.000722 # current rate from the 7th of december
                    elif int(transaction.currency) == Currency['USD'].value:
                        exp_by_cat[transaction.category] += float(transaction.amount) * 0.9503275 # current rate from the 7th of december
                    elif int(transaction.currency) == Currency['EUR'].value:
                        exp_by_cat[transaction.category] += float(transaction.amount)
            else:
                if transaction.expense:
                    # We have to convert all the expenses in the same currency (EUR)
                    if int(transaction.currency) == Currency['KRW'].value:
                        exp_by_cat[transaction.category] = float(transaction.amount) * 0.000722 # current rate from the 7th of december
                    elif int(transaction.currency) == Currency['USD'].value:
                        exp_by_cat[transaction.category] = float(transaction.amount) * 0.9503275 # current rate from the 7th of december
                    elif int(transaction.currency) == Currency['EUR'].value:
                        exp_by_cat[transaction.category] = float(transaction.amount)
  
        print(exp_by_cat)
        return exp_by_cat
    
    def getExpensesByCategory2(self):
        #get preferred currency
        if(self.user_logged.preferred_currency == Currency['KRW'].value):               #I don't know how to get the preferred currency here
            to_currency = 'KRW'
        elif(self.user_logged.preferred_currency == Currency['USD'].value):
            to_currency = 'USD'
        elif(self.user_logged.preferred_currency == Currency['EUR'].value):
            to_currency = 'EUR'
        else:
            print('preferred currency not found')
          
        cr = CurrencyRates()
        exp_by_cat = {}

        for transaction in self.transactions:
            if transaction.category in exp_by_cat:
                if transaction.expense:
                    # We have to convert all the expenses in the preferred currency
                    if int(transaction.currency) == Currency['KRW'].value:
                        from_currency = 'KRW'
                    elif int(transaction.currency) == Currency['USD'].value:
                        from_currency = 'USD'
                    elif int(transaction.currency) == Currency['EUR'].value:
                        from_currency = 'EUR'
                    
                    exp_by_cat[transaction.category] += cr.convert(from_currency, to_currency, transaction.amount)  # converts to the preferred currency
            else:
                if transaction.expense:
                    # We have to convert all the expenses in the preferred currency
                    if int(transaction.currency) == Currency['KRW'].value:
                        from_currency = 'KRW'
                    elif int(transaction.currency) == Currency['USD'].value:
                        from_currency = 'USD'
                    elif int(transaction.currency) == Currency['EUR'].value:
                       from_currency = 'EUR'
                       
                    exp_by_cat[transaction.category] += cr.convert(from_currency, to_currency, transaction.amount)  # converts to the preferred currency
                
        print(exp_by_cat)
        return exp_by_cat
        

moneytor = ModelMoneytor()