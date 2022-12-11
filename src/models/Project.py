from forex_python.converter import CurrencyRates

from models.Currency import Currency

class Project:

    def __init__(self, name):

        self.name = name
        self.transactions = [] # A list of Transaction objects
        
    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def getKeyInfo(self):

        key_info = []
        cr = CurrencyRates()

        # Get the prefered currency 

        fd = open('data/user_logged.txt', 'r')
        line = fd.read()
        user_info = line.split(',')

        prefered_currency = user_info[2]

        fd.close()

        if(int(prefered_currency) == Currency['KRW'].value):
            prefered_currency = 'KRW'
        elif(int(prefered_currency) == Currency['USD'].value):
            prefered_currency = 'USD'
        elif(int(prefered_currency) == Currency['EUR'].value):
            prefered_currency = 'EUR'
        else:
            print('Preferred currency not found')

        # 1st info : the name of the project
        key_info.append(self.name)
        
        # 2nd info : the total of expenses
        total_expenses = 0
        for transaction in self.transactions:
            
            # Get the transaction currency
            if(int(transaction.currency) == Currency['KRW'].value):
                trans_currency = 'KRW'
            elif(int(transaction.currency) == Currency['USD'].value):
                trans_currency = 'USD'
            elif(int(transaction.currency) == Currency['EUR'].value):
                trans_currency = 'EUR'

            if transaction.expense == 'True':
                total_expenses += cr.convert(trans_currency, prefered_currency, float(transaction.amount))

        key_info.append(round(total_expenses, 2))

        # 3rd info : the total of incomes
        total_incomes = 0
        for transaction in self.transactions:

            # Get the transaction currency
            if(int(transaction.currency) == Currency['KRW'].value):
                trans_currency = 'KRW'
            elif(int(transaction.currency) == Currency['USD'].value):
                trans_currency = 'USD'
            elif(int(transaction.currency) == Currency['EUR'].value):
                trans_currency = 'EUR'

            if transaction.expense == 'False':
                total_incomes += cr.convert(trans_currency, prefered_currency, float(transaction.amount))

        key_info.append(round(total_incomes, 2))

        # 4th info : the sold of the project
        sold = total_incomes - total_expenses

        key_info.append(round(sold, 2))

        return key_info

