from models.Finance import Finance
from enum import Enum
from models.Users import Users

class Menu(Enum):
    ADD = 1
    DEL = 2
    VIEW = 3


def read(path):
    f = open(path, 'r')
    while True:
        line = f.readline() # Read a line sequentially
        values = line.split(',')

        if values[0] == '':
            print('End of the data')
        else:
            finance = Finance(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
            print(finance)

        if not line:
            break
        
    f.close()

def main():
    path_data = 'data/sample_file.csv'
    path_users = 'data/users.csv'
    while True:

        # ---- ---- ---- Log In / Sign In ---- ---- ----
        print('---- ---- Welcome to MONEYTOR! ---- ----')
        print('The software that makes your life easier')
        start_input = input('Do you want to log in (L) or Sign up (S)?')
        if(start_input.lower() == 's'):
            new_user = Users.sign_up()
            Users.add(new_user, path_users)
        elif(start_input.lower() == 'l'):
            if(Users.log_in(path_users) == True):
                # ---- ---- ---- Menu ---- ---- ----
                print('What to you want to do:\n(1) Add an expense/income\n(2) Delete an expense/income\n(3) View your balance\n(4) Log out')
                userInput = 0
                while(not userInput):
                    userInput = input('Please Select: ')
                    if(int(userInput) == 1 or int(userInput) == 2 or int(userInput) == 3 or int(userInput) == 4):
                        print('\n')
                    else:
                        print('The input is not valid. Please try again!')
                        userInput = 0
                
                if(int(userInput) == 1):     #ADD
                    new_obj = Finance.create()
                    Finance.add(new_obj, path_data)
                elif(int(userInput) == 2):     #DELETE
                    obj = new_obj #TODO put in the correct object to delete please:)
                    # Finance.delete(obj, path) #TODO uncomment; didnt want to fuck something up
                elif(int(userInput) == 3):     #VIEW LIST
                    read(path_data)
                elif(int(userInput) == 4):     #Log out
                    break
                else:
                    print('A mysterious error occured...sorry:/')
            else:   #if log in was wrong
                print('log in was not successfull.')
                userInput = input('Do you want to sign up? (Y/N): ')
                if(userInput.lower() == 'y'):
                    new_user = Users.sign_up()      #TODO not nice that there are 2 points in the code where you can sign up...
                    Users.add(new_user, path_users)
                else:
                    print('What a pitty... :/\n But you are welcome again any time if you change your mind:)')
            

if __name__=="__main__":
    main()


