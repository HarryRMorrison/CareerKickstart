from faker import Faker
import lorem
import random
from app import app, db
from app.models import User, Tag, Question, Answer, Question_Tag

questions = []
questionTags = []
answers = []
fake = Faker()
tags = []
users = []

USERS = 2
Q_NUM = 2
A_NUM = 4

def is_unique(name):
    for guy in users:
        if name == guy['username']:
            return is_unique(fake.user_name())
    return name

def is_unique_e(email):
    for guy in users:
        if email == guy['email']:
            return is_unique_e(fake.email())
    return email

# Generate 100 users
for _ in range(USERS):
    username = fake.user_name()
    username = is_unique(username)
    email = fake.email()
    email = is_unique_e(email)
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    profilpic = random.choice(['male1.png','male2.png','male3.png','female1.png','female2.png','female3.png'])
    users.append({'username':username, 'email':email, 'password':password, 'profile_pic': profilpic})

titles = [
    "What are common interview questions for a software engineering position?",
    "How can I make my resume stand out for a competitive internship?",
]
tag = {
'companies': ["Apple","Microsoft","Amazon"],
'topics': ['Assessments','Interviews'],
}


for drop in tag.keys():
    for tagz in tag[drop]:
        tags.append({'category':drop, 'tag':tagz})

descriptions = [lorem.paragraph() for _ in range(Q_NUM)]
answerz = [lorem.paragraph() for _ in range(A_NUM)]

for i in range(len(titles)):
    done = []
    com = random.randint(0, 6)
    comb = {"title":titles[i], "description":descriptions[i], "likes":random.randint(0, 49), "comments":com, 'user_id':random.randint(1, USERS)}
    questions.append(comb)
    for num in [random.randint(1, 45) for _ in range(random.randint(1, 6))]:
        if num in done:
            continue
        else:
            done.append(num)
            questionTags.append({'question_id':i,'tag_id':num})
    for j in [random.randint(1, A_NUM-1) for _ in range(com)]:
        comb = {"answer":answerz[j], "question_id":i, "likes":random.randint(0, 49), 'user_id':random.randint(1, USERS)}
        answers.append(comb)

app.app_context().push()

try:
    for row in tags:
        t = Tag(tag=row['tag'], category=row['category'])
        db.session.add(t)

    for row in users:
        u = User(username=row['username'], email=row['email'], profile_pic=row['profile_pic'])
        u.password_hash = row['password']
        db.session.add(u)

    for row in questions:
        q = Question(title=row['title'], description=row['description'], likes=row['likes'], comments=row['comments'], user_id=row['user_id'])
        db.session.add(q)

    for row in answers:
        a = Answer(answer=row['answer'], likes=row['likes'], user_id=row['user_id'], question_id=row['question_id'])
        db.session.add(a)

    for row in questionTags:
        qt = Question_Tag(question_id=row['question_id'], tag_id=row['tag_id'])
        db.session.add(qt)
except:
    raise Exception("An error occurred.")
else:
    db.session.commit()