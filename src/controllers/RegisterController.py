import sys

# setting path
sys.path.append('../models')

from models.User import User

class RegisterController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, username, password, pref_curr):
 
        try:

            # save the model
            self.model.username = str(username)
            self.model.password = str(password)
            self.model.pref_curr = str(pref_curr)
            self.model.save()

            # show a success message
            self.view.show_success(f'The account of {username} has been successfully created!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)