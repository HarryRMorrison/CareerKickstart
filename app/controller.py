# Import necessary Flask extensions and Python libraries
from app import db
from app.blueprints import main
from app.models import User, Tag, Question, Answer, Question_Tag
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, jsonify, redirect, url_for, flash
from app.forms import QuestionForm, EditProfileForm, LoginForm, SignupForm, AnswerForm
from random import choice

# Define a class to handle post-related actions
class PostController():

    # Retrieves top questions for display
    def get_top_questions():
        # Initialize form and fetch tag choices from database
        # Query top questions based on likes and comments, then render the page
        form = QuestionForm()
        tag_choices = Tag.query.with_entities(Tag.tag).all()
        form.set_choices([tag[0] for tag in tag_choices])
        top_questions = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .limit(28)
            .all()
        )
        return render_template("explore.html", posts=top_questions, form=form, categories=SearchController.get_tags())
    
    # Returns the detail page of a specific post
    def get_post_page(question_id):
        # Fetch the question or return 404, render question detail page
        to_load = Question.query.get_or_404(question_id)
        form = AnswerForm()
        return render_template('request.html', question=to_load, form=form)
    
    # Returns search results based on user input
    def get_searched_questions(search):
        # Similar structure to get_top_questions but filters by search results
        form = QuestionForm()
        tag_choices = Tag.query.with_entities(Tag.tag).all()
        form.set_choices([tag[0] for tag in tag_choices])
        q_ids = SearchController.search_func(search)
        top_questions = db.session.query(Question).filter(Question.question_id.in_(q_ids)).order_by((Question.likes + Question.comments).desc()).limit(28).all()
        return render_template("explore.html", posts=top_questions,  form=form, categories=SearchController.get_tags())

    # Paginates to the next set of questions
    def get_next_question_set(page_num):
        # Queries the next set of questions based on pagination, returns JSON data
        next_set = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .offset((page_num*28)-1)
            .limit(28)
            .all()
        )
        next_posts = [question.to_dict() for question in next_set]
        return jsonify(next_posts)
    
    # Similar to get_next_question_set but for searched questions
    def get_next_searched_questions(arguments, page_num):
        # Filters the next set of questions by search criteria
        filters = {}
        for opt in arguments:
            if opt != 'page':
                filters[opt] = arguments[opt]
        q_ids = SearchController.search_func(filters)
        next_set = db.session.query(Question).filter(Question.question_id.in_(q_ids)).order_by((Question.likes + Question.comments).desc()).offset((page_num*28)-1).limit(28).all()
        next_posts = [question.to_dict() for question in next_set]
        return jsonify(next_posts)

    # Handles the creation of a new post/question
    def create_post():
        # Initializes form, fetches tags, validates submission, and handles database operations
        form = QuestionForm()
        tag_choices = Tag.query.with_entities(Tag.tag).all()
        form.set_choices([tag[0] for tag in tag_choices])
        if form.validate_on_submit():
            # Process the validated data
            submitting_user = User.query.get(int(current_user.get_id()))
            new_question = Question(title=form.data['title'], description=form.data['description'], likes=0, comments=0,user=submitting_user)
            db.session.add(new_question)
            db.session.commit()
            q_id = new_question.question_id
            # Creates the Question Tag entries
            try:
                for tag in form.data['tags']:
                    t_id = db.session.query(Tag).filter(Tag.tag==tag).first()
                    qt=Question_Tag(question_id=q_id,tag_id=t_id.tag_id)
                    print(qt)
                    db.session.add(qt)
                db.session.commit()
            except:
                db.session.rollback()
            print('Question posted:', form.data)
            flash("Question posted!")
            # returns to explore
            return redirect('/explore')  # Redirect as necessary
        # Rendsers creat.html page
        return render_template('create.html', form=form, categories=SearchController.get_tags())
    
    # Handles the creation of a new answer to a question
    def create_answer(qid,data):
        # Processes and stores the answer in the database
        submitting_user = User.query.get(int(current_user.get_id()))
        answer = Answer(question_id=qid, answer=data['answer'], likes=0, user_id=int(current_user.get_id()))
        db.session.add(answer)
        db.session.commit()
        return redirect('/question/'+str(qid))

# Defines a class for handling search functionality
class SearchController():

    # Fetches tags for various filters
    def get_tags():
        # Queries distinct tag categories and compiles them into a dictionary
        role = db.session.query(Tag.tag).filter(Tag.category == "role").all()
        company = db.session.query(Tag.tag).filter(Tag.category == "companies").all()
        discipline = db.session.query(Tag.tag).filter(Tag.category == "disciplines").all()
        industry = db.session.query(Tag.tag).filter(Tag.category == "industry").all()
        topic = db.session.query(Tag.tag).filter(Tag.category == "topics").all()
        tags = {}
        # Puts tags into readable format
        tags['role'] = [itag[0] for itag in role]
        tags['company'] = [itag[0] for itag in company]
        tags['discipline'] = [itag[0] for itag in discipline]
        tags['industry'] = [itag[0] for itag in industry]
        tags['topic'] = [itag[0] for itag in topic]
        return tags

    # Executes the actual search based on user queries and selected tags
    def search_func(search):
        # Processes search criteria and returns matching question IDs
        tags_checked = [checked.strip(' ') for checked in search if search[checked]=='on']
        valid_tags = db.session.query(Tag.tag).all()
        query = search.get('query','').upper()
        found = [tag[0] for tag in valid_tags if tag[0].upper() in query and tag[0] not in tags_checked]+tags_checked
        # Queries for the search that user has requested by splitting the search to find tags
        result = (
            db.session.query(Question_Tag.question_id)
            .join(Tag)
            .filter(Tag.tag.in_(found))
            .group_by(Question_Tag.question_id)
            .having(func.count('*') >= len(found))
            .all()
        )
        return [q_id[0] for q_id in result]

# Class to handle user-related functionalities
class UserController():

    # Registers a new user and logs them in
    def register(data):
        # Processes registration data, saves new user, and handles login
        pfp = choice(['male1.png','male2.png','male3.png','female1.png','female2.png','female3.png'])
        user = User(username=data['username'], email=data['email'], profile_pic=pfp)
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return UserController.login(data)
    
    # Handles user login
    def login(data):
        # Authenticates user and redirects based on success or failure
        try:
            user = User.query.filter_by(username=data['username_email']).first()
        except:
            user = User.query.filter_by(username=data['username']).first()
        if user is not None and user.check_password(data['password']):
            # User exists and password is correct
            login_user(user)  # Log in user and remember them
            flash("Login Success!")
            return redirect('/home')
        else:
            flash("Password doesn't match")
            return redirect(url_for('main.login'))
    
    # Allows users to edit their profile
    def edit_profile(Username):
        # Fetches and updates user data based on form input
        form=EditProfileForm()
        user_info = User.query.filter_by(username=Username).first()
        if user_info is None:
            return jsonify({"error": "Question not found"}), 404
        user_q = Question.query.filter_by(user_id=user_info.id).all()
        user_a = Answer.query.filter_by(user_id=user_info.id).all()
        posts = user_q
        for ans in user_a:
            posts.append(ans.question)
        
        # Validates profile form and determines if the user has entered data or not
        if form.validate_on_submit():
            user = User.query.get(current_user.get_id())
            if form.about_me.data != '':
                user.about_me = form.about_me.data
                print('Changed User about me:'+form.about_me.data)
            if form.username.data != '':
                user.username = form.username.data
                print('Changed User name:'+form.username.data)
            if form.new_password.data != '':
                user.set_password(form.new_password.data)
                print('Changed User password:'+form.new_password.data)
            db.session.commit()
            form=EditProfileForm()
            # renders new form for submission if user needs to change pfp again
            return render_template('profilePage.html',posts=posts,form=form,user=user_info.to_dict_pfp())
        return render_template('profilePage.html',posts=posts,form=form,user=user_info.to_dict_pfp())