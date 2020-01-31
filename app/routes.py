from flask import render_template, url_for, request, redirect, flash
from app.forms import SignupForm, LoginForm
from app.models import User
from app import app
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
	return render_template('index.html', name=name)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		flash('First step is finished!', 'success')
	return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

@app.route('/blog')
def blog():
	return render_template('blog.html', title='Blog', posts=posts[:10])

