from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
#from flask.ext.mongoalchemy import BaseQuery

@login_manager.user_loader
def find_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(), nullable=False)
	last_name = db.Column(db.String(), nullable=False)
	email = db.Column(db.String(), nullable=False, unique=True)
	phone = db.Column(db.String(), unique=True)
	picture = db.Column(db.String(), default='https://www.hirerush.com/bundles/theme/images/how-brand.png')
	password = db.Column(db.String())
	#service_requests = db.relationship('Request')

	def __repr__(self):
		return f'User("{self.first_name}", "{self.last_name}", \
			"{self.picture}")'
"""
class Provider(User):

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(), nullable=False)
	last_name = db.Column(db.String(), nullable=False)
	email = db.Column(db.String(), nullable=False, unique=True)
	phone = db.Column(db.String(), unique=True)
	picture = db.Column(db.String(), default='https://www.hirerush.com/bundles/theme/images/how-brand.png')
	password = db.Column(db.String())
	location = db.Column(db.String())
"""

#class BlogPost(db.Model):

#	slug = db.Column(db.String(), primary_key=True)
	
