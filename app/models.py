import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.sql import func
from app import db

class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    tag = sa.Column(sa.String(40), unique=True)
    question_tags = db.relationship('Question_Tag', backref='on_question', lazy=True)

    def __repr__(self):
        return '[<Tag_id {}> <Tag {}>]'.format(self.tag_id, self.tag)
    
class User(db.Model):
    __tablename__ = 'users'
    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(30))
    email = sa.Column(sa.String(100))
    password = sa.Column(sa.String(50))
    questions = db.relationship('Question', backref='q_author', lazy=True)
    answers = db.relationship('Answer', backref='a_author', lazy=True)

    def __repr__(self):
        return '[<User {}> <User_id {}> <Email {}>]'.format(self.username, self.user_id, self.email)
    
class Question(db.Model):
    __tablename__ = 'questions'
    question_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey(User.user_id), nullable=False)
    title = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.String(2000), nullable=False)
    date_created = sa.Column(sa.DateTime, default=func.now())
    likes = sa.Column(sa.Integer)
    comments = sa.Column(sa.Integer)
    tags = db.relationship('Question_Tag', backref='has_tags', lazy=True)
    answers = db.relationship('Answer', backref='has_answers', lazy=True)

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
    qt_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    question_id = sa.Column(sa.Integer, sa.ForeignKey(Question.question_id))
    tag_id = sa.Column(sa.Integer, sa.ForeignKey(Tag.tag_id))

    def __repr__(self):
        return '[<Tag_id {}> <Question_id {}>]'.format(self.tag_id, self.question_id)
    
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