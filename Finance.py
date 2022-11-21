from Currency import Currency
from datetime import date

class Finance:

    def __init__(self, amount, currency, project, category, description, expense, date):
        self.amount = amount
        self.currency = currency
        self.project = project
        self.category = category
        self.description = description
        self.expense = expense
        self.date = date

    def asInFile(self):
        return self.amount + ',' + self.currency + ',' + self.project + ',' + self.category + ',' + self.description + ',' + self.expense + ',' + self.date

    def __str__(self):

        expense = ''

        if self.expense == True:
            expense = '+'
        else:
            expense = '-'

        return 'Amount : ' + expense + self.amount + '\nCurrency : ' + self.currency + '\nProject : ' + self.project + '\nCategory : ' + self.category + '\nDescription : ' + self.description + '\nDate : ' + self.date

    def create():
        amount_new = float(input('Please input the amount: '))

        currency_new = 0
        while(not(currency_new)):
            currency_new = str(input('please input the currency: '))
            if(currency_new == 'won'):
                currency_new = Currency['KRW'].value    #to store the value of the currency
            elif(currency_new == 'eur'):
                currency_new = Currency['EUR'].value
            else:
                print('Unfortunately the selected currency is not supported yet. We are working hard to implement it as fast as possible')
                print('Please input a valid currency')
                currency_new = 0

        project_new = str(input('please input the name of the project: '))
        category_new = str(input('please input the category: '))
        description_new = str(input('please input a short description: '))

        expense_new = 2
        while(expense_new == 2):
            expense_new = str(input('please input (0) for income or (1) for an expense: '))
            if(int(expense_new) == (0 or 1)):
                expense_new = bool(expense_new)
            else:
                print('The input was not valid')
                expense_new = 2

        today = date.today()
        date_new = today.strftime("%Y%m%d")
            
        new_finance = Finance(amount_new, currency_new, project_new, category_new, description_new, expense_new, date_new)
        
        #if(new_finance.isinstance()):
        #    print('New Object has been created')   #TODO check if object was created successfully

        return new_finance


    def add(new_finance, path):
        f = open(path, 'a') #'a' for append; 'w' will overwrite the existing data
        f.write('\n' + str(new_finance.amount) + ',' + str(new_finance.currency) + ',' + str(new_finance.project) + ',' + str(new_finance.category) + ',' + str(new_finance.description) + ',' + str(new_finance.expense) + ',' + str(new_finance.date))

    def delete(finance, path):

        with open(path, "r") as fp:
            lines = fp.readlines()

        with open(path, "w") as fp:
            for line in lines:
                if line.strip("\n") != finance.asInFile():
                    fp.write(line)