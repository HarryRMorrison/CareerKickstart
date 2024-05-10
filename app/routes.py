from flask import render_template, redirect, url_for
from app import app
from app.controller import PostController

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/explore')
def load_explorepage():
    return PostController.get_top_questions()

@app.route('/explore/<int:page>')
def get_next_questions(page):
    return PostController.get_next_question_set(page)