import unittest, os, time
from app import db, create_app
from app.models import User, Question, Answer, Tag, Question_Tag
from config import TestingConfig
from selenium import webdriver
import multiprocessing 

class SeleniumTests(unittest.TestCase):
    def setUp(self):
        self.testApp = create_app(TestingConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        # Create 6 users
        users = [User(username=f'user{i}', email=f'user{i}@example.com') for i in range(1, 7)]
        [user.set_password('qwerty') for user in users]
        db.session.add_all(users)
        # Create 6 tags
        tags = [
            Tag(tag='Microsoft', category='Company')
            Tag(tag='Tech', category='Industry')
            Tag(tag='Intern', category='role')
            Tag(tag='Interview', category='topic')
            Tag(tag='EY', category='Company')    
        ]
        db.session.add_all(tags)
        # Committing users and tags to ensure they have IDs for the foreign key relationships
        db.session.commit()
        # Create 6 questions, each linked to a user and some tags
        questions = [
            Question(title=f'Question title {i}',description=f'Question description {i}', user_id=users[i-1].id)
            for i in range(1, 7)
        ]
        db.session.add_all(questions)
        # Create 6 answers, each linked to a question and a user
        answers = [
            Answer(answer=f'Answer content {i}', question=questions[i-1].question_id, user_id=users[i-1].id)
            for i in range(1, 7)
        ]
        db.session.add_all(answers)
        # Commit questions and answers to ensure they have IDs
        db.session.commit()
        # Link each question with a unique tag (for simplicity, 1 tag per question in this example)
        question_tags = [
            Question_Tag(question_id=questions[i-1].question_id, tag_id=tags[i-1].tag_id)
            for i in range(1, 7)
        ]
        db.session.add_all(question_tags)
        # Commit all changes to the database
        db.session.commit()

        self.server_thread = multiprocessing.Process(target=self.testApp.run)
        self.server_thread.start()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.server_thread.terminate()  # Stops the server thread
        self.driver.close()  # Stops the webdriver
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
 
    def test_register(self):
        u = User.query.get('1')
        self.assertEqual(s.first_name,'Test',msg='student exists in db')
        self.driver.get('http://localhost:5000/login')
        self.driver.implicitly_wait(5)
        name = self.driver.find_element_by_id('username_email')
        name.send_keys(u.username)
        passwrd = self.driver.find_element_by_id('loginform').find_element_by_tag_name("input")[1]
        passwrd.send_keys('qwerty')
        time.sleep(1)
        self.driver.implicitly_wait(5)
        submit = self.driver.find_element_by_id('loginform').find_element_by_tag_name("input")[2]
        submit.click()
        #check login success
        self.driver.implicitly_wait(5)
        time.sleep(1)
        logout = self.driver.find_element_by_partial_link_text('Profile')
        self.assertEqual(logout.get_attribute('innerHTML'), 'Profile', msg='Logged in')


if __name__=='__main__':
  unittest.main(verbosity=2)