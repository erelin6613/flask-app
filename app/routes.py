from flask import render_template, url_for, request, redirect, flash
from app.forms import SignupForm, LoginForm, EditProfileForm
from app.models import User
from PIL import Image
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import json
import requests
import secrets
import os

database = 'https://raw.githubusercontent.com/erelin6613/flask-app/master/app/database.json'

r = requests.get(database)

name = 'HireRush'
posts = json.loads(r.text)

posts=posts['posts']

def upload_picture(form_picture):

"""
This one function seems to work as expected, further in update functionality
app fails to render an uploaded picture. This option requires fixing.
"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    #print(picture_fn)
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_fn)
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route('/')
@app.route('/index')
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
    if current_user.is_authenticated:
    	return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
    	user = User.query.filter_by(email=form.email.data).first()
    	if user and bcrypt.check_password_hash(user.password, form.password.data):
    		login_user(user, remember=form.remember.data)
    		next_page = request.args.get('next')
    		return redirect(next_page) if next_page else redirect(url_for('index'))
    	else:
    		flash('Login error: incorrect email or password')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
	#edit_mode = False

	return render_template('profile.html', title='Profile', edit_mode=False)

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = upload_picture(form.picture.data)
            current_user.picture = picture_file
        current_user.phone = form.phone.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile edited', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.phone.data = current_user.phone
        form.email.data = current_user.email
    picture = os.path.join(app.root_path, 'static/profile_pics', current_user.picture)

    return render_template('profile.html', title='Profile',
                           picture=picture, form=form, edit_mode=True)

	#return render_template('profile.html', title='Profile', edit_mode=True)


@app.route('/blog')
def blog():
	selected_post = False
	if selected_post == True:
		return render_template() 
	return render_template('blog.html', title='Blog', posts=posts[:10])


"""
@app.route('/blog/<slug>')
def blog(slug):
	#post = posts
	for post in posts:
		if post.slug == slug:
			return render_template('blog-post.html', title=post.name, post=post)
		else:
			post = None

	if post == None:
		flash('Oops, an error occured.')

"""