class Finance:

    def __init__(self, amount, currency, project, category, description, expense, date):
        self.amount = amount
        self.currency = currency
        self.project = project
        self.category = category
        self.description = description
        self.expense = expense
        self.date = date
    
    def __str__(self):
        return self.amount # TODO: Nice display of the object

    def create():
        amount_new = float(input('Please input the amount: '))
        currency_new = str(input('please input the currency: '))

        new_finance = Finance(amount_new, currency_new, '0', '0', '0', True, 20221121)
        if(new_finance.isinstance()):
            print('New Object has been created')

    def add(new_finance):
        print('bla')
