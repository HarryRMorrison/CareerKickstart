from flask import render_template, redirect, url_for, request
from app import app
from app.controller import PostController, SearchController

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/explore', methods=['GET'])
def load_explorepage():
    arguments = ['query','company','role','topic','discipline','industry']
    if any(params in arguments for params in request.args):
        return SearchController.search_func(request.args)
    else:
        return PostController.get_top_questions()

@app.route('/explore<int:page>')
def get_next_questions(page):
    return PostController.get_next_question_set(page)

@app.route('/filter-retrieve')
def get_filters():
    return SearchController.get_tags()