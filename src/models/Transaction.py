from models.Currency import Currency
from datetime import date

class Transaction:

    def __init__(self, amount, currency, project, category, description, expense, date):
        self.amount = amount
        self.currency = currency
        self.project = project
        self.category = category
        self.description = description
        self.expense = expense
        self.date = date

    # Return a finance the way it should be in the csv file
    def asInFile(self):
        return self.amount + ',' + self.currency + ',' + self.project + ',' + self.category + ',' + self.description + ',' + self.expense + ',' + self.date

    def __str__(self):

        expense = ''

        if self.expense == True:
            expense = '+'
        else:
            expense = '-'

        cur = 'upsiiis'            # to show currency behind the amount
        if self.currency == str(Currency['EUR'].value):
            cur = '€'
        elif self.currency == str(Currency['KRW'].value):
            cur = 'W'
        elif self.currency == str(Currency['USD'].value):
            cur = '$'

        #return 'Amount : ' + expense + self.amount + ' ' + cur + '\nProject : ' + self.project + '\nCategory : ' + self.category + '\nDescription : ' + self.description + '\nDate : ' + self.date
        return 'Amount : ' + expense + self.amount + ' ' + cur + '\nDescription : ' + self.project + ' --> ' + self.category + ' --> ' + self.description + '\nDate : ' + self.date

    def initialize(path):

        f = open(path, 'r')
        while True:
            line = f.readline() # Read a line sequentially
            values = line.split(',')

            if values[0] == '':
                print('End of the data')
            else:
                finance = Transaction(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
                print(finance)

            if not line:
                break
            
        f.close()

    def create():
        amount_new = float(input('Please input the amount: '))

        currency_new = 0
        while(not(currency_new)):
            currency_new = str(input('please input the currency: '))
            if(currency_new.lower() == 'won'):
                currency_new = Currency['KRW'].value    #to store the value of the currency
            elif(currency_new.lower() == 'eur' or currency_new.lower() == 'euro'):
                currency_new = Currency['EUR'].value
            elif(currency_new.lower() == 'usd' or currency_new.lower() == 'dollar'):
                currency_new = Currency['USD'].value
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
            if(int(expense_new) == 0 or int(expense_new) == 1):
                expense_new = bool(expense_new)
            else:
                print('The input was not valid')
                expense_new = 2

        today = date.today()
        date_new = today.strftime("%Y%m%d")
            
        new_finance = Transaction(amount_new, currency_new, project_new, category_new, description_new, expense_new, date_new)
        #if(new_finance.isinstance()):
        #    print('New Object has been created')   #TODO check if object was created successfully
        return new_finance
    
    def create(amount_new, currency_new, project_new, category_new, description_new, expense_new, date_new):
        new_finance = Transaction(amount_new, currency_new, project_new, category_new, description_new, expense_new, date_new)
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