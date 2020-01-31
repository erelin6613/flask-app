from flask import render_template, url_for, request, redirect, flash
from app.forms import SignupForm, LoginForm
from app.models import User
from app import app, db, bcrypt
import json
import requests

database = 'https://raw.githubusercontent.com/erelin6613/flask-app/master/app/database.json'

r = requests.get(database)

name = 'HireRush'
posts = json.loads(r.text)

posts=posts['posts']

@app.route('/')
@app.route('/home')
def index():
	beta=True
	return render_template('index.html', name=name, beta=beta)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(first_name=form.first_name.data, last_name=form.last_name.data, \
					email=form.email.data, phone=form.phone.data, password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash('Sign up step is finished!', 'success')
		return redirect(url_for('login'))
	return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

@app.route('/blog')
def blog():
	return render_template('blog.html', title='Blog', posts=posts[:10])

