class LoginController:

    #TODO Question: do we crate one controller per page? 
    #--> so another one for signup, and one for the main page?
    
    #TODO For login we dont save the data to the file. So What you created is the signup for creating a new account, right?
    
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, username, password, pref_curr):
 
        try:

            # save the model
            self.model.username = username  #TODO check if input is valid
            self.model.password = password
            self.model.pref_curr = pref_curr
            self.model.save()

            # show a success message
            self.view.show_success(f'The account of {username} created!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)