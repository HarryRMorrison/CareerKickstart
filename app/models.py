import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.sql import func
from app import db

class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(40), unique=True)
    category = db.Column(db.String(40))

    question_tags = db.relationship('Question_Tag', back_populates='tag', lazy=True)

    def __repr__(self):
        return '[<Tag_id {}> <Tag {}>]'.format(self.tag_id, self.tag)
    
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))

    user_questions = db.relationship('Question', back_populates='user', lazy=True)
    user_answers = db.relationship('Answer', back_populates='user', lazy=True)

    def __repr__(self):
        return '[<User {}> <User_id {}> <Email {}>]'.format(self.username, self.user_id, self.email)
    
class Question(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=func.now())
    likes = db.Column(db.Integer)
    comments = db.Column(db.Integer)

    user = db.relationship('User', back_populates='user_questions')
    tags = db.relationship('Question_Tag', back_populates='question', lazy=True)
    answers = db.relationship('Answer', back_populates='question', lazy=True)

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
    qt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'))

    tag = db.relationship('Tag', back_populates='question_tags')
    question = db.relationship('Question', back_populates='tags')

    def __repr__(self):
        return '[<Tag_id {}> <Question_id {}>]'.format(self.tag_id, self.question_id)
    
class Answer(db.Model):
    __tablename__ = 'answers'
    ans_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    answer = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=func.now())
    likes = db.Column(db.Integer)

    user = db.relationship('User', back_populates='user_answers')
    question = db.relationship('Question', back_populates='answers')

    def __repr__(self):
        return f'''
        [Answer:{self.ans_id}
        Question:{self.question_id},
        User:{self.user_id},
        Answer:{self.answer[:20]},
        Created:{self.date_created},
        Likes:{self.likes}
        ]'''