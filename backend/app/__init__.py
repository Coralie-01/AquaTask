from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

# Initialize Flask app
app = Flask(__name__)
# Allow CORS to handle cross-origin requests
CORS(app) 
# Configure the app using the Config class in config.py
app.config.from_object(Config)
# Initialize the database
db = SQLAlchemy(app)

from app import routes, models


