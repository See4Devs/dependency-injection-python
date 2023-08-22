from flask import Flask, jsonify
from flask_injector import FlaskInjector, inject

app = Flask(__name__)

class Database:
    def __init__(self):
        self.data = {"message": "Data from the Database!"}

class Logger:
    def log(self, message):
        print("Logging:", message)

class DataService:
    def __init__(self, database: Database, logger: Logger):
        self.database = database
        self.logger = logger

    def fetch_data(self):
        self.logger.log("Fetching data...")
        return self.database.data

@app.route('/')
@inject
def index(data_service: DataService):
    return jsonify(data_service.fetch_data())

if __name__ == '__main__':
    FlaskInjector(app=app)
    app.run(debug=True)
