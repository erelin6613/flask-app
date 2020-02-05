from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from secrets import token_bytes
#from flask.ext.mongoalchemy import BaseQuery

@login_manager.user_loader
def find_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):

	def __init__(self, id, first_name, last_name, email,
					phone, picture, password):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone
		self.picture = picture
		self.password = password

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
			"{self.email}", "{self.phone}", "{self.picture}")'

class Provider(User):

	def __init__(self, id, first_name, last_name, email,
					phone, picture, password, profile_id,
					business_name, location, role, services):
		super().__init__(id, first_name, last_name, email,
							phone, picture, password)
		self.profile_id = profile_id
		self.business_name = business_name
		self.location = location
		self.role = role
		self.services = services

	profile_id = db.Column(db.Integer)
	business_name = db.Column(db.String())
	location = db.Column(db.String())
	role = db.Column(db.String())
	services = db.Column(db.String())

	def __repr__(self):
		return f'Profile("{self.business_name}", "{self.services}")'


class Requestor(User):

	def __init__(self, id, first_name, last_name, email,
					phone, picture, password, requests):
		super().__init__(id, first_name, last_name, email,
							phone, picture, password)
		self.requests = requests

	requests = db.Column(db.String())

	def __repr__(self):
		return f'User("{self.first_name}", "{self.last_name}", \
			"{self.email}", "{self.phone}", "{self.requests}")'




class ServiceRequest(db.Model, UserMixin):

	id = db.Column(db.Integer, primary_key=True)
	service = db.Column(db.String(), nullable=False)
	add_info = db.Column(db.String())
	first_name = db.Column(db.String(), nullable=False)
	last_name = db.Column(db.String(), nullable=False)
	email = db.Column(db.String(), nullable=False)
	phone = db.Column(db.String(), nullable=False)





#class BlogPost(db.Model):

#	slug = db.Column(db.String(), primary_key=True)
	
