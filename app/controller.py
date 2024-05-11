from app import app, db
from app.models import User, Tag, Question, Answer, Question_Tag
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask import render_template

class PostController():

    def get_top_questions():
        top_questions = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .limit(28)
            .all()
        )
        return render_template("explore.html", posts=top_questions)
    
    def get_searched_questions(search):
        q_ids = SearchController.search_func(search)
        top_questions = db.session.query(Question).filter(Question.question_id.in_(q_ids)).order_by((Question.likes + Question.comments).desc()).limit(28).all()
        return render_template("explore.html", posts=top_questions)
    
    def get_next_question_set(page_num):
        next_set = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .offset((page_num*28)-1)
            .limit(28)
            .all()
        )
        next_posts = [question.to_dict() for question in next_set]
        return next_posts
    
    def get_next_searched_questions(arguments, page_num):
        filters = {}
        for opt in arguments:
            if opt != 'page':
                filters[opt] = arguments[opt]
        q_ids = SearchController.search_func(filters)
        next_set = db.session.query(Question).filter(Question.question_id.in_(q_ids)).order_by((Question.likes + Question.comments).desc()).offset((page_num*28)-1).limit(28).all()
        next_posts = [question.to_dict() for question in next_set]
        return next_posts
    
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