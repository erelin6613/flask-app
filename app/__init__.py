import json
from flask import Flask
from flask_pymongo import PyMongo
from mongoengine import connect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)

app.config['SECRET_KEY'] = '357d8ecf84df959408e2ab4a5cd3c453'

app.config['MONGO_URI'] = 'mongodb://localhost:27017'


mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'success'

from app import routes