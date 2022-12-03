# from models.Currency import Currency
#import numpy as np
#import pandas as pd

# FIRST_NAME = 0
# PASSWORD = 2

class User:

    def __init__(self, line):
       
        infos = line.split(',')

        self.username = infos[0]
        self.password = infos[1]
        self.prefered_currency = infos[2]

    def __str__(self):
        return 'Username: ' + self.username + ', Password: ' + self.password + ', Preferred Currency: ' + str(self.prefered_currency)

    def save(self):
        with open('data/users.csv', 'a') as f:
            f.write('\n' + self.username + ',' + self.password + ',' + self.prefered_currency)

    # def sign_up():  #TODO check, that the person isn't signed up already
    #     print('-- WELCOME --\nPlease Start by creating an account')
    #     first_name = input('Whats your first name? ')
    #     last_name = input('Whats your last name? ')
    #     password = input('Please chose a password: ')    #TODO check if name and password are valid

    #     pref_curr = 0

    #     while(not(pref_curr)):
    #         pref_curr = input('What is your preferred currency? (eur, won or usd) ')
    #         if(type(pref_curr) != str):
    #             print('Please enter a string')
    #             pref_curr = 0
    #         elif(pref_curr.lower() == 'won'):
    #             pref_curr = Currency['KRW'].value    
    #         elif(pref_curr.lower() == 'eur' or pref_curr.lower() == 'euro'):
    #             pref_curr = Currency['EUR'].value
    #         elif(pref_curr.lower() == 'usd' or pref_curr.lower() == 'dollar'):
    #             pref_curr = Currency['USD'].value
    #         else:
    #             print('Unfortunately the selected currency is not supported yet. We are working hard to implement it as fast as possible')
    #             print('Please input a valid currency')
    #             pref_curr = 0
            
    #     new_user = User(first_name, last_name, password, pref_curr)
    #     #if(new_finance.isinstance()):
    #     #    print('New Object has been created')   #TODO check if object was created successfully
    #     return new_user

    # def add(new_user, path):
    #     f = open(path, 'a') #'a' for append; 'w' will overwrite the existing data
    #     #TODO edit string so that it has the correct notation (no space(' ') in it, name type = str etc.)
    #     f.write('\n' + str(new_user.first_name) + ',' + str(new_user.last_name) + ',' + str(new_user.password) + ',' + str(new_user.pref_curr))

    # def log_in(path):
    #     # ---- read user file ----
    #     f = open(path, 'r') #open user file 

    #     rowcount  = 0
    #     for row in open(path):
    #         rowcount+= 1
    #     users_list = [[0 for i in range(rowcount)] for j in range(3)]
        
    #     row = 0
    #     while True:
    #         line = f.readline() # Read a line sequentially
    #         values = line.split(',')

    #         if values[0] == '':
    #             print('User File read. You can now log in.')
    #         else:
    #             for n in range(0, (len(values)-1)):         #safe users data in a 2D array
    #                 users_list[row][n] = values[n]
    #         row += row  #safe one row after the other   

    #         if not line:
    #             break    


    #     # ---- get user input ----
    #     print('For Log-In please enter your data:')
    #     login_correct = False
    #     amt_tries = 0

    #     while(not(login_correct) and (amt_tries < 3)):
    #         first_name = str(input('First Name: '))
    #         password = str(input('Password: '))
    #         for row in range(0, len(users_list)):
    #             if((users_list[row][FIRST_NAME] == first_name) and (users_list[row][PASSWORD] == password)):
    #                 print('Login successful!')
    #                 login_correct = True
    #                 break
    #             elif(amt_tries >= 2):
    #                 print('3 wrong tries!')
    #                 login_correct = False
    #                 break
    #             else:
    #                 if(row == len(users_list)-1):     #Error only gets printed when last row is reached
    #                     print('The Name or Password was not correct! Please try again!')
    #                 login_correct = False
    #         amt_tries += 1
         
    #     f.close()
    #     return login_correct