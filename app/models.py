from app import db
from datetime import datetime

class User(db.Model):

	id_ = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(), nullable=False)
	last_name = db.Column(db.String(), nullable=False)
	email = db.Column(db.String(), nullable=False, unique=True)
	phone = db.Column(db.String(), unique=True)
	picture = db.Column(db.String(), default='img.jpeg')
	password = db.Column(db.String())
	#service_requests = db.relationship('Request')

	def __repr__(self):
		return f'User("{self.first_name}", "{self.last_name}", \
			"{self.picture}")'