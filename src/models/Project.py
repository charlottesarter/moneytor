from forex_python.converter import CurrencyRates

from models.Currency import Currency

class Project:

    def __init__(self, name):

        self.name = name
        self.transactions = [] # A list of Transaction objects
        
    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def getKeyInfo(self):

        def getRate(from_currency, to_currency):

            # EUR
            if from_currency == 'EUR' and to_currency == 'EUR':
                return 1
            elif from_currency == 'EUR' and to_currency == 'KRW':
                return 1369.54
            elif from_currency == 'EUR' and to_currency == 'USD':
                return 1.05

            # KRW
            elif from_currency == 'KRW' and to_currency == 'EUR':
                return 0.00073
            elif from_currency == 'KRW' and to_currency == 'KRW':
                return 1
            elif from_currency == 'KRW' and to_currency == 'USD':
                return 0.000767

            # USD
            elif from_currency == 'USD' and to_currency == 'EUR':
                return 0.95
            elif from_currency == 'USD' and to_currency == 'KRW':
                return 1302.37
            elif from_currency == 'USD' and to_currency == 'USD':
                return 1

        def getCurrencyName(currency):

            if(int(currency) == Currency['KRW'].value):
                return 'KRW'
            elif(int(currency) == Currency['USD'].value):
                return 'USD'
            elif(int(currency) == Currency['EUR'].value):
                return 'EUR'
            else:
                print('Preferred currency not found')
                return 0

        key_info = []
        cr = CurrencyRates()

        # Get the prefered currency 

        fd = open('data/user_logged.txt', 'r')
        line = fd.read()
        user_info = line.split(',')

        prefered_currency = getCurrencyName(user_info[2])

        fd.close()

        # 1st info : the name of the project
        key_info.append(self.name)
        
        # 2nd info : the total of expenses
        total_expenses = 0
        for transaction in self.transactions:
            
            # Get the transaction currency
            trans_currency = getCurrencyName(transaction.currency)

            rate = getRate(trans_currency, prefered_currency)

            if transaction.expense == 'True':
                total_expenses += float(transaction.amount) * rate

        key_info.append(round(total_expenses, 2))

        # 3rd info : the total of incomes
        total_incomes = 0
        for transaction in self.transactions:

            # Get the transaction currency
            trans_currency = getCurrencyName(transaction.currency)

            rate = getRate(trans_currency, prefered_currency)

            if transaction.expense == 'False':
                total_incomes += float(transaction.amount) * rate

        key_info.append(round(total_incomes, 2))

        # 4th info : the sold of the project
        sold = total_incomes - total_expenses

        key_info.append(round(sold, 2))

        return key_info
    



        

