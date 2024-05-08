from faker import Faker
import lorem
import random
from app import app, db
import sqlalchemy as sa
from app.models import User, Tag, Question, Answer, Question_Tag

questions = []
questionTags = []
answers = []
fake = Faker()
tags = []
users = []

# Generate 100 users
for _ in range(100):
    username = fake.user_name()
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    users.append({'username':username, 'email':email, 'password':password})

titles = [
    "What are common interview questions for a software engineering position?",
    "How can I make my resume stand out for a competitive internship?",
    "Can anyone share tips for succeeding in a virtual interview?",
    "What should I include in a cover letter for a graduate program application?",
    "How can I prepare for a case study interview in consulting?",
    "What are some effective follow-up strategies after a job interview?",
    "Does anyone have experience with the assessment centers for management trainee programs?",
    "What are some good questions to ask at the end of an internship interview?",
    "How do I negotiate a job offer without offending the employer?",
    "Can anyone recommend resources for learning about business analysis for an entry-level position?",
    "What's the best way to explain a gap year to potential employers during an interview?",
    "How do I handle behavioral interview questions effectively?",
    "What are the key skills I should highlight for a business development role?",
    "How do I prepare for a technical assessment involving coding challenges?",
    "What are some project management tools that I should be familiar with before starting an internship?",
    "What are common mistakes people make in job interviews and how can I avoid them?",
    "How do I ask for feedback after an unsuccessful job application?",
    "What are the essentials of an elevator pitch for networking events?",
    "Can anyone explain the importance of internships for business majors?",
    "How do I balance multiple job offers and make the best decision?",
    "What are the best strategies for networking at professional conferences?",
    "How can I improve my public speaking skills for presentations during an internship?",
    "What are some effective ways to manage stress during the job search process?",
    "Can someone explain the difference between an informational interview and a job interview?",
    "What are the benefits of joining a professional association as a graduate student?",
    "How can I use LinkedIn effectively to connect with industry professionals?",
    "What are some common pitfalls in group interviews and how can I prepare for them?",
    "How should I approach answering salary expectation questions during job interviews?",
    "What are some unique challenges of remote internships and how can I overcome them?",
    "Can anyone recommend online courses for enhancing analytical skills for business analysts?",
    "How do I tailor my resume for different industries without losing my personal brand?",
    "What are some signs that an internship will offer valuable learning opportunities?",
    "How do I maintain professional relationships after a networking event?",
    "What should I expect during an internship at a startup versus a large corporation?",
    "How can I effectively demonstrate my leadership skills in a job application?",
    "What are some common legal considerations in business contracts that I should be aware of?",
    "Can anyone share experiences with transitioning from academic research to industry roles?",
    "How should I prepare for a technical interview involving data structures and algorithms?",
    "What are the key considerations when applying for international job positions?",
    "How do I handle questions about future career plans in interviews?",
    "What are effective strategies for time management when balancing a part-time job and studies?",
    "Can someone explain the role of emotional intelligence in workplace success?",
    "What are some essential soft skills for a career in finance?",
    "How can I find mentorship opportunities in my field of interest?",
    "What are some tips for writing a compelling statement of purpose for grad school applications?",
    "How do I approach career fairs to maximize my opportunities for internships?",
    "What are the typical steps in a graduate school application process?",
    "How can I prepare for aptitude tests commonly used in job screenings?",
    "What are some ethical considerations in business management?",
    "How can I effectively use project management software to enhance team collaboration?"
]

tag = {
'companies': ["Apple","Microsoft","Amazon","Google","Facebook","Tesla","Berkshire Hathaway","Johnson & Johnson","Walmart","Visa","PwC","JPMorgan","Deloitte","Intel","KPMG","Telstra","ANZ","Chevron","Boeing","BHP"],
'topics': ['Assessments','Interviews','Advice','Resumes','Cover Letters'],
'industry': ['Health','Banking','Finance','Retail','Investment','Social Media', 'Technology','Automotive'],
'role': ['Intern','Graduate'],
'disciplines': ["Biology","Computer Science","Economics","Mechanical Engineering","Psychology","English Literature","Political Science","Chemistry","History","Mathematics"]
}


for drop in tag.keys():
    for tagz in tag[drop]:
        tags.append({'category':drop, 'tag':tagz})

descriptions = [lorem.paragraph() for _ in range(50)]
answerz = [lorem.paragraph() for _ in range(240)]

for i in range(len(titles)):
    com = random.randint(0, 6)
    comb = {"title":titles[i], "description":descriptions[i], "likes":random.randint(0, 49), "comments":com, 'user_id':random.randint(0, 49)}
    questions.append(comb)
    for num in [random.randint(0, 48) for _ in range(random.randint(1, 6))]:
        questionTags.append({'question_id':i,'tag_id':num})
    for j in [random.randint(0, 239) for _ in range(com)]:
        comb = {"answer":answerz[j], "question_id":i, "likes":random.randint(0, 49), 'user_id':random.randint(0, 49)}
        answers.append(comb)

app.app_context().push()

try:
    for row in tags:
        t = Tag(tag=row['tag'], category=row['category'])
        db.session.add(t)

    for row in users:
        u = User(username=row['username'], email=row['email'], password = row['password'])
        db.session.add(u)

    for row in questions:
        q = Question(title=row['title'], description=row['description'], likes=row['likes'], comments=row['comments'], user_id=row['user_id'])
        db.session.add(q)

    for row in answers:
        a = Answer(answer=row['answer'], likes=row['likes'], user_id=row['user_id'])
        db.session.add(a)

    for row in questionTags:
        qt = Question_Tag(question_id=row['question_id'], tag_id=row['tag_id'])
        db.session.add(qt)
except:
    db.session.rollback()
else:
    db.session.commit()