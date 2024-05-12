from app import app, db
from app.models import Question, Tag
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request
from app.controller import PostController, SearchController

@app.route('/api/explore/', methods=['GET'])
def get_next_questions():
    arguments = request.args
    if len(arguments)>1:
        return PostController.get_next_searched_questions(arguments,int(arguments.get('page','')))
    else:
        return PostController.get_next_question_set(int(arguments.get('page','')))

@app.route('/api/filter-retrieve', methods=['GET'])
def get_filters():
    return SearchController.get_tags()

@app.route('/api/likeadjust/', methods=['PUT'])
def adjust_likes():
    questionid = request.args.get('qid', type=int)
    num = request.args.get('num', type=int)

    if not questionid or not num:
        return jsonify({"error": "Missing parameters"}), 400
    print(Question.query.filter_by(question_id=questionid).first().likes)
    post = Question.query.filter_by(question_id=questionid).first()
    if post is None:
        return jsonify({"error": "Question not found"}), 404
    try:
        post.likes += num
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    print(Question.query.filter_by(question_id=questionid).first().likes)
    return jsonify({"likes": post.likes})