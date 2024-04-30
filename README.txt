Setup:
Requirements:
•	pip install -r requirements.txt
Start up server:
•	Flask run
Upgrade to most recent db:
•	flask db upgrade
Downgrade to no tables:
•	flask db downgrade base
Upgrade to all tables:
•	flask db upgrade


Cases:
Start the python interpreter in context of application (pre-import “app”)
•	flask shell
This is registering the function in the shell context, so “app” isn’t passed into each function:
•	@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
Create migration repository:
•	flask db init
Each time a table is added:
•	flask db migrate -m "users table"


