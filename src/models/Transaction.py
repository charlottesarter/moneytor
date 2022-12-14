from models.Currency import Currency
from datetime import date

class Transaction:

    def __init__(self, line):

        infos = line.split(',')

        self.amount = infos[0]
        self.currency = infos[1]
        self.project = infos[2]
        self.category = infos[3]
        self.description = infos[4]
        self.expense = infos[5]
        self.date = infos[6]
        self.year = self.date[:4]

        if self.date[4:6] == '01':
            self.month = 'jan'
        elif self.date[4:6] == '02':
            self.month = 'feb'
        elif self.date[4:6] == '03':
            self.month = 'march'
        elif self.date[4:6] == '04':
            self.month = 'april'
        elif self.date[4:6] == '05':
            self.month = 'may'
        elif self.date[4:6] == '06':
            self.month = 'june'
        elif self.date[4:6] == '07':
            self.month = 'july'
        elif self.date[4:6] == '08':
            self.month = 'aug'
        elif self.date[4:6] == '09':
            self.month = 'sept'
        elif self.date[4:6] == '10':
            self.month = 'oct'
        elif self.date[4:6] == '11':
            self.month = 'nov'
        elif self.date[4:6] == '12':
            self.month = 'dec'

        self.day = self.date[6:]

    # Return a finance the way it should be in the csv file
    def asInFile(self):
        return self.amount + ',' + self.currency + ',' + self.project + ',' + self.category + ',' + self.description + ',' + self.expense + ',' + self.date

    def __str__(self):

        expense = ''

        if self.expense == True:
            expense = '+'
        else:
            expense = '-'

        # To show currency behind the amount

        cur = ''
        if self.currency == str(Currency['EUR'].value):
            cur = '€'
        elif self.currency == str(Currency['KRW'].value):
            cur = 'W'
        elif self.currency == str(Currency['USD'].value):
            cur = '$'

        return 'Amount : ' + expense + str(self.amount) + ' ' + cur + '\nDescription : ' + self.project + ' --> ' + self.category + ' --> ' + self.description + '\nDate : ' + str(self.date) + '\n'

    def initialize(path):

        f = open(path, 'r')
        while True:
            line = f.readline() # Read a line sequentially
            values = line.split(',')

            if values[0] == '':
                print('End of the data')
            else:
                finance = Transaction(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
                #print(finance)

            if not line:
                break
            
        f.close()

    # Multiply the amount by getSign() to obtain the true value of the transaction (positive if income or negative if expense)

    def getSign(self):
        if self.expense:
            return -1
        else:
            return 1


    def create(): # TODO adapt this function for the gui
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