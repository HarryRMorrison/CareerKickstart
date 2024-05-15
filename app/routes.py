from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.controller import PostController, SearchController
from flask_login import login_required, current_user
import sqlalchemy as sa
from app.models import User
from app.forms import EditProfileForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/explore', methods=['GET'])
def load_explorepage():
    arguments = request.args
    if len(arguments)>0:
        if len(arguments)==1 and arguments.get('query','') == '':
            return PostController.get_top_questions()
        else:
            return PostController.get_searched_questions(arguments)
    else:
        return PostController.get_top_questions()
    
@app.route('/create', methods=['GET', 'POST'])
def load_createpage():
    return PostController.create_post()

@app.route('/login', methods=['GET','POST'])
def load_login():
    return render_template('login.html')    

@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)
