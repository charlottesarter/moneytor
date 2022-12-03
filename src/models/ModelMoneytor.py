# Moneytor model (singleton)

from models.Transaction import Transaction
from models.User import User

class ModelMoneytor(object):

    # Initialization of the model (from the files users.csv and transactions.csv)

    def __init__(self):

        # The list of all of the users of the app (users.csv)

        self.users = [] 

        fd = open('data/users.csv', 'r')
        lines = fd.readlines()
        fd.close

        for line in lines:
            # line = line.rstrip()
            self.users.append(User(line))

        # The list of all of the transactions of one user 
        
        self.transactions = []

        fd = open('data/transactions.csv', 'r')
        lines = fd.readlines()
        fd.close

        for line in lines:
            # line = line.rstrip()
            self.transactions.append(Transaction(line))

        self.user_logged = ''

    # Make sure that there is only one model (singleton)

    def __new__(model):
        if not hasattr(model, 'instance'):
            model.instance = super(ModelMoneytor, model).__new__(model)
        return model.instance

    # Add a new user

    def addUser(self, line):
        new_user = User(line)
        new_user.save()
        self.users.append(new_user)

    # Returns the list of all of the users

    def getAllUsers(self):
        return self.users
        
moneytor = ModelMoneytor()

