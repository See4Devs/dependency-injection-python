from fastapi import FastAPI, Depends
 
app = FastAPI()
 
class DataService:
    def fetch_data(self):
        return {"message": "Greetings from the Dynamic DataService in the World of FastAPI!"}
 
def get_data_service():
    return DataService()
 
@app.get('/')
def index(data_service: DataService = Depends(get_data_service)):
    data = data_service.fetch_data()
    return {"result": data, "info": "Fetched from the Dynamic DataService in FastAPI!"}
