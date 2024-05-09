from flask import render_template
from app import app
from app.controller import PostController

@app.route('/')
@app.route('/home')
def index():
    return "Hello, World!"

@app.route('/explore')
def load_explorepage():
    return PostController.get_top_questions()

@app.route('/explore/<int:page>')
def get_next_questions(page):
    return PostController.get_next_question_set(page)