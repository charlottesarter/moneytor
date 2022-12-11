from forex_python.converter import CurrencyRates
from models.ModelMoneytor import ModelMoneytor

class Project:

    def __init__(self, name):

        self.name = name
        self.transactions = [] # A list of Transaction objects
        
    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def getKeyInfo(self):

        key_info = []

        # 1st info : the name of the project
        key_info.append(self.name)
        
        cr = CurrencyRates()
        model = ModelMoneytor()

        # 2nd info : the total of expenses
        total_expenses = 0
        for transaction in self.transactions:
            if transaction.expense == 'True':
                total_expenses += cr.convert(transaction.currency, model.getPreferedCurrecy, float(transaction.amount))

        key_info.append(round(total_expenses, 2))

        # 3rd info : the total of incomes
        total_incomes = 0
        for transaction in self.transactions:
            if transaction.expense == 'False':
                total_incomes += cr.convert(transaction.currency, model.getPreferedCurrecy, float(transaction.amount))

        key_info.append(round(total_incomes, 2))

        # 4th info : the sold of the project
        sold = total_incomes - total_expenses

        key_info.append(round(sold, 2))

        return key_info

