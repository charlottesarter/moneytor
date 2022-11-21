from Finance import Finance
from enum import Enum

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
    path = 'data/sample_file.csv'
    while True:
        # ---- ---- ---- Menu ---- ---- ----
        print('---- ---- Welcome to MONEYTOR! ---- ----')
        print('The software that makes your life easier')
        print('What to you want to do:\n(1) Add an expense/income\n(2) Delete an expense/income\n(3) View your balance')
        userInput = 0
        while(not userInput):
            userInput = input('Please Select: ')
            if(int(userInput) == 1 or int(userInput) == 2 or int(userInput) == 3):
                print('\n')
            else:
                print('The input is not valid. Please try again!')
                userInput = 0
        
        if(int(userInput) == 1):     #ADD
            new_obj = Finance.create()
            Finance.add(new_obj, path)
        elif(int(userInput) == 2):     #DELETE
            obj = new_obj #TODO put in the correct object to delete please:)
            # Finance.delete(obj, path) #TODO uncomment; didnt want to fuck something up
        elif(int(userInput) == 3):     #VIEW LIST
            read(path)
        else:
            print('A mysterious error occured...sorry:/')

if __name__=="__main__":
    main()


