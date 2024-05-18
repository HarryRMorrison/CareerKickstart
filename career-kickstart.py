import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, db
from flask_migrate import Migrate
from app.models import Tag, Question, Question_Tag, Answer, User

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'tags': Tag, 'users': User, 'answers': Answer,'questions': Question, 'question_tags': Question_Tag}