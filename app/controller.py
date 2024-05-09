from app import app, db
from app.models import User, Tag, Question, Answer, Question_Tag
import sqlalchemy as sa
from flask import render_template

class PostController():

    def get_top_questions():
        top_questions = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .limit(30)
            .all()
        )
        return render_template("explorePage.html", posts=top_questions)
    
    def get_next_question_set(page_num):
        next_set = (
            db.session.query(Question)
            .order_by((Question.likes + Question.comments).desc())
            .offset((page_num*30)-1)
            .limit(30)
            .all()
        )
        next_posts = [question.to_dict() for question in next_set]
        return next_posts