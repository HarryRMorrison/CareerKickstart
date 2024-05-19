# Importing necessary modules from SQLAlchemy, Werkzeug, hashlib, and Flask-Login
from sqlalchemy.sql import func
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from sqlalchemy import text
from flask_login import UserMixin

# User loader callback for Flask-Login to load a user given an ID
@login.user_loader
def load_student(id):
  return User.query.get(int(id))

# Tag model definition
class Tag(db.Model):
    __tablename__ = 'tags' # Specifies the table name in the database
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key
    tag = db.Column(db.String(40), unique=True) # Unique tag name
    category = db.Column(db.String(40)) # Category of the tag

    # Establishing a relationship to Question_Tag for accessing associated questions
    question_tags = db.relationship('Question_Tag', back_populates='tag', lazy=True)

    def __repr__(self):
        return '[<Tag_id {}> <Tag {}>]'.format(self.tag_id, self.tag)

# User model definition, inheriting from UserMixin for authentication methods
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    profile_pic = db.Column(db.String(12))
    about_me = db.Column(db.String(200), nullable=True)

    # Relationships to questions and answers authored by the user
    user_questions = db.relationship('Question', back_populates='user', lazy=True) 
    user_answers = db.relationship('Answer', back_populates='user', lazy=True)

    # Set user password with a hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password match with a hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '[<User {}> <id {}> <Email {}> <Password {}>]'.format(self.username, self.id, self.email, self.password_hash)
    
    def to_dict_pfp(self):
        # Helper function to serialize user data for API responses
        numQ = Question.query.filter_by(user_id=self.id).count()
        numA = Answer.query.filter_by(user_id=self.id).count()
        return {'id':str(self.id),'username':self.username, 'email':self.email, 'aboutme':self.about_me, 'numQ':numQ, 'numA':numA, 'pfp':self.profile_pic}

# Question model definition
class Question(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=func.now())
    likes = db.Column(db.Integer)
    comments = db.Column(db.Integer)

    # Relationships to the user who posted the question and related tags and answers
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
    
    # Helper function for Question and answer retrieval for request page responses
    def to_dict(self):
        return {
            'question_id': self.question_id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'username': self.user.username,
            'profile_photo': self.user.profile_pic,
            'votes': self.likes,
            'answers': [answer.to_dict() for answer in self.answers]
        }
    
    # Helper function to retrieve tags for a question for server and API responses
    def associated_tags(self):
        return [itag.tag.tag for itag in self.tags]

    # Helper function to retrieve question information for a question for API responses
    def to_dict(self):
        tagz = [itag.tag.tag for itag in self.tags]
        return {'question_id':self.question_id,'title':self.title,'description':self.description,'likes':self.likes,'comments':self.comments,'tags':tagz,'user':self.user.username,'profile_pic':self.user.profile_pic,'date':self.date_created.strftime('%Y-%m-%d')}
    
    # Helper function to retrieve user associated with the question
    def get_user(self):
        return self.user.username

# Question_Tag model definition for many-to-many relationship between questions and tags
class Question_Tag(db.Model):
    __tablename__ = 'question_tags'
    qt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'))

    # Relationships back to the Tag and Question models
    tag = db.relationship('Tag', back_populates='question_tags')
    question = db.relationship('Question', back_populates='tags')

    def __repr__(self):
        return '[<QT_id {}> <Tag_id {}> <Question_id {}>]'.format(self.qt_id ,self.tag_id, self.question_id)
    
# Answer model definition
class Answer(db.Model):
    __tablename__ = 'answers'
    ans_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    answer = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=func.now())
    likes = db.Column(db.Integer)

    # Relationships to the user who authored the answer and the question it answers
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
    
    # Helper function for Answer retrieval for request page responses
    def to_dict(self):
        return {
            'ans_id': self.ans_id,
            'question_id': self.question_id,
            'user_id': self.user_id,
            'username': self.user.username,
            'profile_photo': self.user.profile_pic,  # Modify this to use the actual profile photo path
            'answer': self.answer,
            'created': self.date_created,
            'likes': self.likes
        }