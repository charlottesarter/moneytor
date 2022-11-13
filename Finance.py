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
        


    