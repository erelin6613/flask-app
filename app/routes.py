from flask import render_template, url_for, request, redirect, flash, abort, Blueprint
from app.forms import SignupForm, LoginForm, EditProfileForm, ServiceRequestForm
from app.models import User, ServiceRequest
from PIL import Image
from app import app, mongo, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import json
import requests
import secrets
import os

routes = Blueprint('routes', __name__) 
database = 'https://raw.githubusercontent.com/erelin6613/flask-app/master/app/database.json'
#pictures = UploadSet('profile_pictures', IMAGES)

r = requests.get(database)

name = 'HireRush'
posts = json.loads(r.text)

posts=posts['posts']


beta = True

def upload_picture(form_picture):

# This one function seems to work as expected, further in update functionality
# app fails to render an uploaded picture. This option requires fixing.

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

beta = True

@app.route('/')
@app.route('/index')
def index():
	flash(mongo)
	return render_template('index.html', name=name, beta=beta)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = request.form
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        rand_id = int.from_bytes(os.getrandom(8), 'big')
        user = User(id=rand_id, first_name=form.first_name.data, last_name=form.last_name.data, 
                    email=form.email.data, phone=form.phone.data, password=hashed_pass, picture='')
        db.session.add(user)
        db.session.commit()
        flash('Sign up step is finished!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form, beta=beta)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
    	return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
    	user = mongo.db.hirerush.users.find_one({"email": form.email.data})
    	if user and bcrypt.check_password_hash(user.password, form.password.data):
    		login_user(user, remember=form.remember.data)
    		next_page = request.args.get('next')
    		return redirect(next_page) if next_page else redirect(url_for('index'))
    	else:
    		flash('Login error: incorrect email or password')
    return render_template('login.html', title='Login', form=form, beta=beta)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
	#edit_mode = False

	return render_template('profile.html', title='Profile', edit_mode=False, beta=beta)

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit():

    form = request.form
    if form.validate_on_submit():
        if form.picture.data:
            # for now the problem with image is solved with hard coding the path, 
            # altough this logic breaks down quickly. Further inspection needed.
            picture_file = 'static/profile_pictures/' + upload_picture(form.picture.data)
            current_user.picture = picture_file
        current_user.phone = form.phone.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile edited', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.phone.data = current_user.phone
        form.email.data = current_user.email
    picture = 'static/profile_pictures/' + current_user.picture

    return render_template('profile.html', title='Profile',
                           picture=picture, form=form, edit_mode=True, beta=beta)

	#return render_template('profile.html', title='Profile', edit_mode=True)


@app.route('/blog')
def blog():
	selected_post = False
	if selected_post == True:
		return render_template() 
	return render_template('blog.html', title='Blog', posts=posts[:10], beta=beta)

@app.route('/service-request', methods=['GET', 'POST'])
def service_request():

    form = request.form
    try:
        form.phone.data = current_user.phone
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    except Exception:
        pass
    if form.validate_on_submit():
        service_request = ServiceRequest(service=form.service.data, add_info=form.add_info.data,
                                            first_name=form.first_name.data, last_name=form.last_name.data,
                                            email=form.email.data, phone=form.phone.data)
        db.session.add(service_request)
        if not User.query.filter(email=form.email.data):
            rand_id = int.from_bytes(os.getrandom(8), 'big')
            rand_pass = int.from_bytes(os.getrandom(16), 'big')
            hashed_pass = bcrypt.generate_password_hash(rand_pass).decode('utf-8')
            user = User(id=rand_id, first_name=form.first_name.data, last_name=form.last_name.data, 
                        email=form.email.data, phone=form.phone.data, password=hashed_pass, picture='')
            db.session.add(user)        

        db.session.commit()
        flash('Request created! Let our pros a bit of time to respond with a quote.', 'success')
        return redirect(url_for('index'))
    return render_template('service-request.html', title='Find Pros', form=form, beta=beta)



@app.route('/leads')
def leads():
    leads = mongo.db.hirerush.ServiceRequest.find()
    return render_template('leads.html', leads=leads)

@app.route('/lead/<int:lead_id>', methods=['GET', 'PUT'])
def lead(lead_id):
    lead = mongo.db.hirerush.ServiceRequest.find_one({"_id": lead_id})
    return render_template('lead.html', lead=lead)
