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

        # 2nd info : the total of expenses
        total_expenses = 0
        for transaction in self.transactions:
            if transaction.expense:
                total_expenses += float(transaction.amount)

        key_info.append(total_expenses)

        # 3rd info : the total of incomes
        total_incomes = 0
        for transaction in self.transactions:
            if not transaction.expense:
                total_incomes += float(transaction.amount)

        key_info.append(total_incomes)

        # 4th info : the sold of the project
        sold = total_incomes - total_expenses

        key_info.append(sold)

        return key_info

