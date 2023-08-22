from injector import inject

class DataService:
    @inject
    def __init__(self):
        self.message = "Hello from Dynamic DataService in Django!"

    def fetch_data(self):
        return {"message": self.message}
