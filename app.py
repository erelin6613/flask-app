from flask import Flask, render_template, url_for, request, redirect, flash
#from flasksqlalchemy import SQLAlchemy
from datetime import datetime
import json

from forms import SignupForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '357d8ecf84df959408e2ab4a5cd3c453'

name = 'HireRush'
with open('database.json') as file:
	posts = json.loads(file.read())

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
	return render_template('blog.html', title='Blog', posts=posts)

if __name__ == '__main__':
	app.run(debug=True)

