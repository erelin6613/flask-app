from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import Select
from flask_wtf.file import FileField, FileAllowed
from app.models import User
import re

class SignupForm(FlaskForm):


	def check_phone(self, phone):
		if not re.search(r'.*[0-9]{3}\D?[0-9]{3}\D?[0-9]{4}\D?', str(phone)):
			raise ValidationError('Invalid phone number')

	def check_email_exists(self, email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise  ValidationError('The email is already signed up.')

	def check_phone_exists(self, phone):
		user = User.query.filter_by(phone=phone.data).first()

		if user:
			raise  ValidationError('The phone is already signed up.')

	roles = ['Owner', 'CEO', 'Representative']
	first_name = StringField('First Name', 
							validators=[DataRequired(), 
										Length(min=2, max=40)])
	last_name = StringField('Last Name', 
							validators=[DataRequired(), 
										Length(min=2, max=40)])
	email = StringField('Email', validators=[DataRequired(), Email(), check_email_exists])
	phone = StringField('Phone', validators=[DataRequired(), check_phone, check_phone_exists])
	password = PasswordField('Password', validators=[DataRequired()])
	conf_pass = PasswordField('Confirm Password', 
								validators=[DataRequired(), 
											EqualTo('password')])
	role = Select('Role in organization')

	submit_step_1 = SubmitField('Next')





class LoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')


class EditProfileForm(FlaskForm):

	def check_phone(self, phone):
		if not re.search(r'.*[0-9]{3}\D?[0-9]{3}\D?[0-9]{4}\D?', str(phone)):
			raise ValidationError('Invalid phone number')

	def check_email_exists(self, email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise  ValidationError('The email is already signed up.')

	def check_phone_exists(self, phone):
		user = User.query.filter_by(phone=phone.data).first()

		if user:
			raise  ValidationError('The phone is already signed up.')

	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = StringField('Phone', validators=[DataRequired(), check_phone])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
	submit = SubmitField('Edit')

