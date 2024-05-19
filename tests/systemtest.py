import unittest, os, time
from app import db, create_app
from app.models import User, Question, Answer, Tag, Question_Tag
from config import TestingConfig
from selenium import webdriver
import multiprocessing 

class SeleniumTests(unittest.TestCase):
    def setUp(self):
        # Set up the application with testing configuration
        self.testApp = create_app(TestingConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        # Add test data
        users = [User(username=f'user{i}', email=f'user{i}@example.com') for i in range(1, 7)]
        [user.set_password('qwerty') for user in users]
        db.session.add_all(users)
        tags = [Tag(tag=tag, category=category) for tag, category in [('Microsoft', 'Company'), ('Tech', 'Industry'), ('Intern', 'Role'), ('Interview', 'Topic'), ('EY', 'Company'), ('Finance', 'Discipline')]]
        db.session.add_all(tags)
        db.session.commit()

        questions = [Question(title=f'Question title {i}', description=f'Question description {i}', user_id=user.id) for i, user in enumerate(users, start=1)]
        db.session.add_all(questions)
        answers = [Answer(answer=f'Answer content {i}', question_id=question.question_id, user_id=user.id) for i, (question, user) in enumerate(zip(questions, users), start=1)]
        db.session.add_all(answers)
        db.session.commit()

         # Start the Flask app in a separate process for testing
        self.server_thread = multiprocessing.Process(target=self.testApp.run, kwargs={'use_reloader': False})
        self.server_thread.start()

        # Setting up a Chrome WebDriver in headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.server_thread.terminate()
        self.driver.quit()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        # Navigate to the login page
        self.driver.get('http://localhost:5000/login')
        self.driver.implicitly_wait(5)

        # Enter username and password
        self.driver.find_element(by_id('username_email').send_keys('user1')
        self.driver.find_element(by_name('password').send_keys('qwerty')
        self.driver.find_element(by_name('submit').click()

        # Check for login success by finding the profile link
        profile_link = self.driver.find_element_by_partial_link_text('Profile')
        self.assertTrue('Profile' in profile_link.text, msg='User should be logged in and see their profile link')

if __name__ == '__main__':
    unittest.main(verbosity=2)