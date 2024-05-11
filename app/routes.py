from flask import render_template, redirect, url_for, request
from app import app, db
from app.controller import PostController, SearchController

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/explore', methods=['GET'])
def load_explorepage():
    arguments = request.args
    print(len(arguments))
    if len(arguments)>0:
        if len(arguments)==1 and arguments.get('query','') == '':
            return PostController.get_top_questions()
        else:
            return PostController.get_searched_questions(arguments)
    else:
        return PostController.get_top_questions()

@app.route('/explore/', methods=['GET'])
def get_next_questions():
    arguments = request.args
    if len(arguments)>1:
        return PostController.get_next_searched_questions(arguments,int(arguments.get('page','')))
    else:
        return PostController.get_next_question_set(int(arguments.get('page','')))

@app.route('/filter-retrieve')
def get_filters():
    return SearchController.get_tags()