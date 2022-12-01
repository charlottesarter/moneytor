class MoneytorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def login(self):
        self.view.login()
        
    def signup(self):
        self.view.signup()
        
    def start_moneytor(self):
        self.view.start_page()
        
    