from models.Transaction import Transaction
from enum import Enum


from models.User import User
import tkinter as tk
from tkinter import ttk


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
            finance = Transaction(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
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
            new_user = User.sign_up()
            User.add(new_user, path_users)
        elif(start_input.lower() == 'l'):
            if(User.log_in(path_users) == True):
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
                    new_obj = Transaction.create()
                    Transaction.add(new_obj, path_data)
                elif(int(userInput) == 2):     #DELETE
                    obj = new_obj #TODO put in the correct object to delete please:)
                    # Transaction.delete(obj, path) #TODO uncomment; didnt want to fuck something up
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
                    new_user = User.sign_up()      #TODO not nice that there are 2 points in the code where you can sign up...
                    User.add(new_user, path_users)
                else:
                    print('What a pitty... :/\n But you are welcome again any time if you change your mind:)')
                    break
    
    
    
    
def login_interface():
    root = tk.Tk()
    root.minsize(height=200, width=300)
    def tab_start():
        #------------- LOGIN ---------------
        def login():
            def login_success():
                frame_login.destroy()
                frame_login_success = tk.Frame(root)
                
                label_login_success = tk.Label(frame_login_success, text='Log in complete!')
                label_login_success.pack()
                
                frame_login_success.pack()
                def back():
                    frame_login_success.destroy()
                    login()
                button_back = tk.Button(frame_login_success, text='Back', command=back)
                button_back.pack(side='bottom')    
            
                           
            frame_startpage.destroy()
            frame_login = tk.Frame(root)
            
            label_login = tk.Label(frame_login, text='Please Log in with your user data')
            label_login.pack()
            
            label_first_name = tk.Label(frame_login, text='First Name:')
            label_first_name.pack()
            entry_first_name = tk.Entry(frame_login)
            entry_first_name.pack()
            first_name = entry_first_name.get()
            label_password = tk.Label(frame_login, text='Password:')
            label_password.pack()
            entry_password = tk.Entry(frame_login)
            entry_password.pack()
            password = entry_password.get()
            
            button_next = tk.Button(frame_login, text='Log In', command=login_success)
            button_next.pack()
            
            frame_login.pack()
            
            def back():
                frame_login.destroy()
                tab_start()
            button_back = tk.Button(frame_login, text='Back', command=back)
            button_back.pack(side='bottom')
        #------------- SIGNUP --------------
        def signup():
            def signup_password():
                def signup_currency():
                    def finish():
                        frame_signup_currency.destroy()
                        frame_signup_finish = tk.Frame(root)
                        
                        label_finish = tk.Label(frame_signup_finish, text='Signup Successful!')
                        label_finish.pack()
                        
                        button_start = tk.Button(frame_signup_finish, text='Back to Start', command=login_interface)
                        button_start.pack()
                        
                        frame_signup_finish.pack()
                        def back():
                            frame_signup_finish.destroy()
                            signup_currency()
                        button_back = tk.Button(frame_signup_finish, text='Back', command=back)
                        button_back.pack(side='bottom')
                    
                    
                    frame_signup_password.destroy()
                    frame_signup_currency = tk.Frame(root)
                    
                    label_currency = tk.Label(frame_signup_currency, text='Preferred Currency:')
                    label_currency.pack()
                    entry_currency = tk.Entry(frame_signup_currency)
                    entry_currency.pack()
                    currency = entry_currency.get()
                    
                    button_next = tk.Button(frame_signup_currency, text='Finish', command=finish)
                    button_next.pack()
                    
                    frame_signup_currency.pack()
                    def back():
                        frame_signup_currency.destroy()
                        signup_password()
                    button_back = tk.Button(frame_signup_currency, text='Back', command=back)
                    button_back.pack(side='bottom')
                

                frame_signup.destroy()
                frame_signup_password = tk.Frame(root)
                
                label_password = tk.Label(frame_signup_password, text='Create Password:')
                label_password.pack()
                entry_password = tk.Entry(frame_signup_password)
                entry_password.pack()
                password = entry_password.get()
                
                button_next = tk.Button(frame_signup_password, text='Last Step', command=signup_currency)
                button_next.pack()
                
                frame_signup_password.pack()
                def back():
                    frame_signup_password.destroy()
                    signup()
                button_back = tk.Button(frame_signup_password, text='Back', command=back)
                button_back.pack(side='bottom')
            
            
            frame_startpage.destroy()
            frame_signup = tk.Frame(root)
            
            label_happy = tk.Label(frame_signup, text='Hello, we are pleased to see you!')
            label_happy.pack()
            label_signup = tk.Label(frame_signup, text='Please type in your data to create an account')
            label_signup.pack()
            
            label_first_name = tk.Label(frame_signup, text='First Name:')
            label_first_name.pack()
            entry_first_name = tk.Entry(frame_signup)
            entry_first_name.pack()
            first_name = entry_first_name.get()
            label_last_name = tk.Label(frame_signup, text='Last Name:')
            label_last_name.pack()
            entry_last_name = tk.Entry(frame_signup)
            entry_last_name.pack()
            last_name = entry_last_name.get()
            
            button_next = tk.Button(frame_signup, text='Next', command=signup_password)
            button_next.pack()
            
            frame_signup.pack()
            def back():
                frame_signup.destroy()
                tab_start()
            button_back = tk.Button(frame_signup, text='Back', command=back)
            button_back.pack(side='bottom')
        
        #---------------- Startpage ----------------
        frame_startpage = tk.Frame(root)
        
        label_welcome = tk.Label(frame_startpage, text='----> ----> Welcome to Moneytor <---- <----', font=('Times New Roman', 15))
        label_welcome.pack()
        label_start_1 = tk.Label(frame_startpage, text='To see your Transactions please log in first', font=('Times New Roman', 10))
        label_start_1.pack()
        
        button_login = tk.Button(frame_startpage, text='Log in', command=login)
        button_login.pack()
        button_signup = tk.Button(frame_startpage, text='Sign up', command=signup)
        button_signup.pack()
        
        frame_startpage.pack()
    
    tab_start()
    root.mainloop()



     

if __name__=="__main__":
    #main()
    login_interface()
    
    #this escalated way too quick...I need help please :/
    