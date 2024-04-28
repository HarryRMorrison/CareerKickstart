import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import Tag, Question, Question_Tag, Answer, User

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'tags': Tag, 'users': User, 'answers': Answer,'questions': Question, 'question_tags': Question_Tag}