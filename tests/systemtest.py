import unittest, os, time
from app import db, create_app
from app.models import User, Question, Answer, Tag, Question_Tag
from config import TestingConfig
from selenium import webdriver
from selenium.webdriver.common.by import By
import multiprocessing

#localHost = "http://localhost:5000/"

class SeleniumTests(unittest.TestCase):
    def setUp(self):
        # Set up the application with testing configuration
        self.testApp = create_app(TestingConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        # Add test data
        users = [User(username=f'user{i}', email=f'user{i}@example.com', profile_pic='male1.png') for i in range(1, 7)]
        [user.set_password('qwerty') for user in users]
        db.session.add_all(users)
        tags = [Tag(tag=tag, category=category) for tag, category in [('Graduate', 'role'),('Microsoft', 'companies'), ('Tech', 'industry'), ('Intern', 'Role'), ('Interview', 'topics'), ('EY', 'companies'), ('Finance', 'disciplines')]]
        db.session.add_all(tags)
        db.session.commit()

        questions = [Question(title=f'Question title {i}', description=f'Question description {i}', user_id=user.id) for i, user in enumerate(users, start=1)]
        db.session.add_all(questions)
        answers = [Answer(answer=f'Answer content {i}', question_id=question.question_id, user_id=user.id) for i, (question, user) in enumerate(zip(questions, users), start=1)]
        db.session.add_all(answers)
        db.session.commit()
        qt=Question_Tag(question_id=1, tag_id=2)
        db.session.add(qt)
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

    def test_login(self):
        # Navigate to the login page
        self.driver.get('http://localhost:5000/login')
        self.driver.implicitly_wait(5)

        # Enter username and password
        # find the form by its ID
        form = self.driver.find_element(By.ID,'loginform')
        form.find_element(By.NAME, 'username_email').send_keys('user1')
        form.find_element(By.NAME, 'password').send_keys('qwerty')
        form.find_element(By.NAME, 'submit').click()

        # Check for login success by finding the profile link
        login_success = self.driver.find_element(By.CLASS_NAME, 'modal-body')
        self.assertTrue('Login Success!' in login_success.text, msg='User should be logged in and see their profile link')

    def test_search(self):
        # Navigate to the login page
        self.driver.get('http://localhost:5000/explore?query=Microsoft')
        self.driver.implicitly_wait(5)

        submit_success = self.driver.find_element(By.CLASS_NAME, 'card')
        self.assertTrue('Question title 1' in submit_success.text, msg='User should have microsoft related posts')

if __name__ == '__main__':
    unittest.main(verbosity=2)