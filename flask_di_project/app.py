from flask import Flask, jsonify
from flask_injector import FlaskInjector, inject, singleton

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

# Dependency configurations
def configure(binder):
    binder.bind(Database, to=Database(), scope=singleton)
    binder.bind(Logger, to=Logger(), scope=singleton)
    binder.bind(DataService, to=DataService(Database(), Logger()), scope=singleton)

if __name__ == '__main__':
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=True)
