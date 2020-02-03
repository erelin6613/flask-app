import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_mongoalchemy import MongoAlchemy
#from flask.ext.mongoalchemy import BaseQuery
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '357d8ecf84df959408e2ab4a5cd3c453'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hirerush.db'
#app.config['MONGOALCHEMY_DATABASE'] = 'hirerush'
#app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://hirerushapp-vlxag.gcp.mongodb.net/hirerush'
#app.config['MONGOALCHEMY_SERVER_AUTH'] = True
#app.config['MONGOALCHEMY_SERVER'] = 'mongodb://hirerushapp-shard-00-02-vlxag.gcp.mongodb.net:27017'
#with open('/home/val/mongo_cred.txt', 'r') as file:
#	app.config['MONGOALCHEMY_USER'], app.config['MONGOALCHEMY_PASSWORD'] = file.read().split('\n')

db = SQLAlchemy(app)
#database = MongoAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'success'

from app import routes