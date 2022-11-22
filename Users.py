from Currency import Currency
import numpy as np

FIRST_NAME = 0
PASSWORD = 2

class Users:

    def __init__(self, first_name, last_name, password, pref_curr):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.pref_curr = pref_curr

    def __str__(self):
        return 'Name: ' + self.first_name + ' ' + self.last_name + ', Password: ' + self.password + 'Preferred Currency: ' + self.pref_curr

    def sign_in():
        print('-- WELCOME --\nPlease Start by creating an account')
        first_name = float(input('Whats your first name? '))
        last_name = float(input('Whats your last name? '))
        password = float(input('Please chose a password: '))    #TODO check if name and password are valid

        pref_curr = 0
        while(not(pref_curr)):
            pref_curr = float(input('What is your preferred currency? '))
            if(pref_curr.lower() == 'won'):
                pref_curr = Currency['KRW'].value    
            elif(pref_curr.lower() == 'eur' or pref_curr.lower() == 'euro'):
                pref_curr = Currency['EUR'].value
            elif(pref_curr.lower() == 'usd' or pref_curr.lower() == 'dollar'):
                pref_curr = Currency['USD'].value
            else:
                print('Unfortunately the selected currency is not supported yet. We are working hard to implement it as fast as possible')
                print('Please input a valid currency')
                currency_new = 0
            
        new_user = Users(first_name, last_name, password, pref_curr)
        #if(new_finance.isinstance()):
        #    print('New Object has been created')   #TODO check if object was created successfully
        return new_user

    def add(new_user, path):
        f = open(path, 'a') #'a' for append; 'w' will overwrite the existing data
        f.write('\n' + str(new_user.first_name) + ',' + str(new_user.last_name) + ',' + str(new_user.password) + ',' + str(new_user.pref_curr))

    def log_in(path):
        # ---- read user file ----
        f = open(path, 'r') #open user file 


        users_list = np.loadtxt(f, delimiter=",")
        print(users_list)


        # users_list = [[],[]]
        # row = 0
        # while True:
        #     line = f.readline() # Read a line sequentially
        #     values = line.split(',')

        #     if values[0] == '':
        #         print('User File read. You can now log in.')
        #     else:
        #         for n in range(0, (len(values)-1)):         #safe users data in a 2D array


        #             print('values[]: ', values)

                   
        #             users_list[row],[n] = values[n]
        #     row += row  #safe one row after the other   

        #     if not line:
        #         break    




        # ---- get user input ----
        print('For Log-In please enter your data:')
        first_name = str(input('First Name: '))
        password = str(input('Password: '))
        login_correct = False
        amt_tries = 0

        while(not(login_correct) and (amt_tries < 3)):
            for row in range(0, range(len(users_list))):
                if((users_list[[row],[FIRST_NAME]] == first_name) and (users_list[[row],[PASSWORD]] == password)):
                    print('Login successful!')
                    login_correct = True
                else:
                    print('The Name or Password was not correct! Please try again!')
                    login_correct = False
                    amt_tries += amt_tries
         
        f.close()
        return login_correct