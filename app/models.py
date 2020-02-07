from app import mongo, login_manager
from flask_login import UserMixin
from datetime import datetime
from secrets import token_bytes
from datetime import datetime
#from flask.ext.mongoalchemy import BaseQuery

@login_manager.user_loader
def find_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin):

	def __init__(self, id, first_name, last_name, email,
					phone, picture, password):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone
		self.picture = picture
		self.password = password

	#service_requests = db.relationship('Request')

	def __repr__(self):
		return f'User("{self.first_name}", "{self.last_name}", \
			"{self.email}", "{self.phone}", "{self.picture}")'


"""
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

	profile_id = db.IntField()
	business_name = db.StringField()
	location = db.StringField()
	role = db.StringField()
	services = db.StringField()

	def __repr__(self):
		return f'Profile("{self.business_name}", "{self.services}")'



class Requestor(User):

	def __init__(self, id, first_name, last_name, email,
					phone, picture, password, requests):
		super().__init__(id, first_name, last_name, email,
							phone, picture, password)
		self.requests = requests

	requests = db.StringField()

	def __repr__(self):
		return f'User("{self.first_name}", "{self.last_name}", \
			"{self.email}", "{self.phone}", "{self.requests}")'

"""



class ServiceRequest(UserMixin):

	def __init__(self, id, service, add_info, first_name,
					last_name, email, phone, creation_time):
		self.id = id
		self.service = service
		self.add_info = add_info
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone
		self.creation_time = creation_time

	def __repr__(self):
		return f'ServiceRequest("{self.service}", "{self.first_name}",\
				"{self.last_name}", "{self.phone}")'





#class BlogPost(db.Model):

#	slug = db.Column(db.String(), primary_key=True)
	
