from app import app, db
from app.models import User, Tag, Question, Answer, Question_Tag
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, jsonify, redirect, url_for, flash
from app.forms import QuestionForm, EditProfileForm, LoginForm, SignupForm, AnswerForm
from random import choice

class PostController():

    def get_top_questions():
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
    
    def get_post_page(pagenum):
        to_load = Question.query.get(pagenum)
        form = AnswerForm()
        return render_template('request.html', question=to_load, form=form)
    
    def get_searched_questions(search):
        form = QuestionForm()
        tag_choices = Tag.query.with_entities(Tag.tag).all()
        form.set_choices([tag[0] for tag in tag_choices])
        q_ids = SearchController.search_func(search)
        top_questions = db.session.query(Question).filter(Question.question_id.in_(q_ids)).order_by((Question.likes + Question.comments).desc()).limit(28).all()
        return render_template("explore.html", posts=top_questions,  form=form, categories=SearchController.get_tags())
    
    def get_next_question_set(page_num):
        next_set = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .offset((page_num*28)-1)
            .limit(28)
            .all()
        )
        next_posts = [question.to_dict() for question in next_set]
        return jsonify(next_posts)
    
    def get_next_searched_questions(arguments, page_num):
        filters = {}
        for opt in arguments:
            if opt != 'page':
                filters[opt] = arguments[opt]
        q_ids = SearchController.search_func(filters)
        next_set = db.session.query(Question).filter(Question.question_id.in_(q_ids)).order_by((Question.likes + Question.comments).desc()).offset((page_num*28)-1).limit(28).all()
        next_posts = [question.to_dict() for question in next_set]
        return jsonify(next_posts)
    
    def create_post():
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
            return redirect('/explore')  # Redirect as necessary
        return render_template('create.html', form=form, categories=SearchController.get_tags())
    
    def create_answer(qid,data):
        submitting_user = User.query.get(int(current_user.get_id()))
        answer = Answer(question_id=qid, answer=data['answer'], likes=0, user_id=int(current_user.get_id()))
        db.session.add(answer)
        db.session.commit()
        return redirect('/post/'+str(qid))
    
class SearchController():

    def get_tags():
        role = db.session.query(Tag.tag).filter(Tag.category == "role").all()
        company = db.session.query(Tag.tag).filter(Tag.category == "companies").all()
        discipline = db.session.query(Tag.tag).filter(Tag.category == "disciplines").all()
        industry = db.session.query(Tag.tag).filter(Tag.category == "industry").all()
        topic = db.session.query(Tag.tag).filter(Tag.category == "topics").all()
        tags = {}
        tags['role'] = [itag[0] for itag in role]
        tags['company'] = [itag[0] for itag in company]
        tags['discipline'] = [itag[0] for itag in discipline]
        tags['industry'] = [itag[0] for itag in industry]
        tags['topic'] = [itag[0] for itag in topic]
        return tags

    def search_func(search):
        tags_checked = [checked.strip(' ') for checked in search if search[checked]=='on']
        valid_tags = db.session.query(Tag.tag).all()
        query = search.get('query','').upper()
        found = [tag[0] for tag in valid_tags if tag[0].upper() in query and tag[0] not in tags_checked]+tags_checked
        
        result = (
            db.session.query(Question_Tag.question_id)
            .join(Tag)
            .filter(Tag.tag.in_(found))
            .group_by(Question_Tag.question_id)
            .having(func.count('*') >= len(found))
            .all()
        )
        return [q_id[0] for q_id in result]
    
class UserController():

    def register(data):
        pfp = choice(['male1.png','male2.png','male3.png','female1.png','female2.png','female3.png'])
        user = User(username=data['username'], email=data['email'], profile_pic=pfp)
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return UserController.login(data)
    
    def login(data):
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
            return 'Invalid username or password'
    
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