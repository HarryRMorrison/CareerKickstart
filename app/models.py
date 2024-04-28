import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.sql import func
from app import db

class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    tag = sa.Column(sa.String(40), unique=True)
    questions = so.relationship('Question', secondary='question_tags')

    def __repr__(self):
        return '<Tag {}>'.format(self.tag)
    
class User(db.Model):
    __tablename__ = 'users'
    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(30))
    email = sa.Column(sa.String(100))
    password = sa.Column(sa.String(50))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Question(db.Model):
    __tablename__ = 'questions'
    question_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey(User.user_id), nullable=False)
    title = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.String(2000), nullable=False)
    date_created = sa.Column(sa.DateTime, default=func.now())
    likes = sa.Column(sa.Integer)
    comments = sa.Column(sa.Integer)
    tags = so.relationship('Tag', secondary='question_tags')

    def __repr__(self):
        return f'''[
        User:{self.user_id} 
        Question:{self.question_id}, 
        Title:{self.title}, 
        Description:{self.description[:20]},
        Created:{self.date_created},
        Likes:{self.likes},
        Comments:{self.comments}
        ]'''
    
    
class Question_Tag(db.Model):
    __tablename__ = 'question_tags'
    question_id = sa.Column(sa.Integer, sa.ForeignKey(Question.question_id))
    tag_id = sa.Column(sa.Integer, sa.ForeignKey(Tag.tag_id))

    def __repr__(self):
        return '<Tag_id {}> <Question_id {}>'.format(self.tag_id, self.question_id)
    
class Answer(db.Model):
    __tablename__ = 'answers'
    ans_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    question_id = sa.Column(sa.Integer, sa.ForeignKey('questions.question_id'), nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'), nullable=False)
    answer = sa.Column(sa.String(2000), nullable=False)
    date_created = sa.Column(sa.DateTime, default=func.now())
    likes = sa.Column(sa.Integer)

    def __repr__(self):
        return f'''
        [Answer:{self.ans_id}
        Question:{self.question_id},
        User:{self.user_id},
        Answer:{self.answer[:20]},
        Created:{self.date_created},
        Likes:{self.likes}
        ]'''