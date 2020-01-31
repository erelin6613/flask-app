import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '357d8ecf84df959408e2ab4a5cd3c453'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hirerush.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes