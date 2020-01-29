from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import Select

class SignupForm(FlaskForm):

	roles = ['Owner', 'CEO', 'Representative']

	first_name = StringField('First Name', 
							validators=[DataRequired(), 
										Length(min=2, max=40)])

	last_name = StringField('First Name', 
							validators=[DataRequired(), 
										Length(min=2, max=40)])

	email = StringField('Email', validators=[DataRequired(), Email()])

	phone = StringField('Phone', validators=[DataRequired()])

	password = PasswordField('Password', validators=[DataRequired()])

	conf_pass = PasswordField('Confoirm Password', 
								validators=[DataRequired(), 
											EqualTo('password')])

	role = Select('Role in organization')

	submit_step_1 = SubmitField('Next')

	def check_phone(form, field):
		if not re.search(r'.*[0-9]{3}\D?[0-9]{3}\D?[0-9]{4}\D?'):
			raise ValidationError('Invalid phone number')




class LoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember me')

	submit = SubmitField('Login')