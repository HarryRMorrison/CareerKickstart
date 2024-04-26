from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/getcard', methods = ['GET'])
def send_card_template():
    question_demo = {
        'title': "demo",
        'description': 'demo',
        'tags': [],
        'likes': 1,
        'comments': 1 
    }
    return render_template('card.html', question=question_demo)

@app.route('/explore')
def load_explorepage():
    posts = [
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        },
        {
            'title': "Hello dfgdrgnoerngoinoinger",
            'description': 'fgieorigneirngoienrgoenrgneorigoekrngoer igoierg oierjgoiehrgoiehr goierh goiehrgoiehrg oeihr goi Beautiful day in Portland!',
            'tags': ["Accounting","Internship","Finance","Deloitte","Interviews"],
            'likes': 4,
            'comments': 1 
        }
    ]
    return render_template("explorePage.html", posts=posts)