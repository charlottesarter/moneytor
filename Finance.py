import Currency
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

        return 'Amount : ' + expense + self.amount + '\nCurrency : ' + self.currency.name + '\nProject : ' + self.project + '\nCategory : ' + self.category + '\nDescription : ' + self.description + '\nDate : ' + self.date  

    def create():
        amount_new = float(input('Please input the amount: '))
        currency_new = str(input('please input the currency: '))

        new_finance = Finance(amount_new, currency_new, '0', '0', '0', True, 20221121)
        if(new_finance.isinstance()):
            print('New Object has been created')

    def add(new_finance):
        print('bla')

    def delete(finance, path):

        with open(path, "r") as fp:
            lines = fp.readlines()
        
        with open(path, "w") as fp:
            for line in lines:
                if line.strip("\n") != finance.asInFile():
                    fp.write(line)


