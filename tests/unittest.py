import unittest, os
from app import db, create_app
from app.models import User, Question, Answer, Tag, Question_Tag
from config import TestingConfig

class UserModelCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username='testuser1', email='test1@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(user.username, 'testuser1')

    def test_set_password(self):
        user = User(username='testuser2', email='test2@example.com')
        user.set_password('securepassword')
        self.assertTrue(user.check_password('securepassword'))
        self.assertFalse(user.check_password('wrongpassword'))

    def test_tag_creation(self):
        tag = Tag(tag='Science', category='Disciplines')
        db.session.add(tag)
        db.session.commit()
        self.assertEqual(tag.tag, 'Science')
        self.assertEqual(tag.category, 'Disciplines')

    def test_question_creation(self):
        user = User(username='testuser3', email='test3@example.com')
        db.session.add(user)
        db.session.commit()
        question = Question(title='New Question', description='Detailed description', user_id=user.id)
        db.session.add(question)
        db.session.commit()
        self.assertEqual(question.title, 'New Question')
        #self.assetEqual()

    def test_answer_creation(self):
        user = User(username='testuser4', email='test4@example.com')
        db.session.add(user)
        db.session.commit()
        question = Question(title='New Question', description='Detailed description', user_id=user.id)
        db.session.add(question)
        db.session.add(question)
        answer = Answer(answer='New Answer', question_id=question.question_id, user_id=user.id)
        db.session.add(answer)
        db.session.commit()
        self.assertEqual(answer.answer, 'New Answer')
    
    def test_tag_link(self):
        tag1 = Tag(tag='Microsoft', category='company')
        tag2 = Tag(tag='Artificial Intelligence', category='topic')
        tag3 = Tag(tag='Intern', category='role')
        question = Question(user_id=1,title='test',description='testtest',likes=0,comments=0)
        db.session.add_all([tag1,tag2,tag3,question])
        db.session.commit()
        qt1 = Question_Tag(tag_id=tag1.tag_id,question_id=question.question_id)
        qt2 = Question_Tag(tag_id=tag2.tag_id,question_id=question.question_id)
        qt3 = Question_Tag(tag_id=tag3.tag_id,question_id=question.question_id)
        db.session.add_all([qt1,qt2,qt3])
        db.session.commit()
        all=Question.query.filter_by(question_id=question.question_id).first().associated_tags()
        self.assertEqual(len(all), 3)
        self.assertEqual(all[0], 'Microsoft')

    def test_user_post_link(self):
        user = User(username='testuser69', email='test69@example.com')
        db.session.add(user)
        db.session.commit()
        question = Question(user_id=user.id,title='test',description='testtest',likes=0,comments=0)
        db.session.add(question)
        db.session.commit()
        test = Question.query.filter_by(question_id=question.question_id).first()
        self.assertEqual(test.get_user(), 'testuser69')

    def test_tag_repr(self):
        tag1 = Tag(tag='Microsoft', category='company')
        db.session.add(tag1)
        db.session.commit()
        tag = Tag.query.filter_by(tag='Microsoft').first()
        self.assertEqual(repr(tag), f'[<Tag_id {tag.tag_id}> <Tag Microsoft>]')

if __name__ == '__main__':
    unittest.main(verbosity=2)