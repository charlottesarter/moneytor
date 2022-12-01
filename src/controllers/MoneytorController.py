class MoneytorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def login(self):
        self.view.show_login()
        print('login was pressed')
        
    def register(self):
        self.view.show_register()
        print('register was pressed')
        
    def start_moneytor(self):
        self.view.start_moneytor()
        
    