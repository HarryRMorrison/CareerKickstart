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

USERS = 200
Q_NUM = 500
A_NUM = 1000

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
    "How can I effectively use project management software to enhance team collaboration?",
    "What strategies can I use to improve my networking skills?",
    "How important are personal projects in tech job applications?",
    "Can anyone provide advice on handling panel interviews?",
    "What are effective ways to showcase soft skills on a resume?",
    "How do I prepare for a marketing role interview?",
    "What should I know about the corporate culture before joining a company?",
    "Can anyone suggest how to create a professional portfolio for a creative industry?",
    "What are some strategies for succeeding in asynchronous video interviews?",
    "How do I handle rejections after several job interviews?",
    "What are some best practices for virtual networking?",
    "How can I enhance my problem-solving skills for technical interviews?",
    "What are the latest trends in AI and machine learning job roles?",
    "Can someone share effective ways to research a company before an interview?",
    "How do I manage career growth expectations in my first job?",
    "What are some tips for transitioning from a non-tech role to a tech role?",
    "How can I negotiate benefits in addition to salary?",
    "What are the key considerations for accepting a job offer abroad?",
    "How do I approach career development in a small company versus a large corporation?",
    "What are some tips for maintaining work-life balance in high-pressure jobs?",
    "How can I improve my interview skills over video calls?",
    "What are some common errors in CVs and resumes?",
    "How do I leverage alumni networks for job search success?",
    "What are some questions to ask a future manager during an interview?",
    "How do I write a cover letter for a career change?",
    "What are the best practices for using social media in job searches?",
    "How can I develop leadership skills early in my career?",
    "What are some effective negotiation techniques for entry-level positions?",
    "How do I prepare for a performance review?",
    "What are some effective ways to increase visibility in my current role?",
    "How can I ask for a promotion or raise in a professional way?",
    "What are some challenges of working remotely and how can I overcome them?",
    "How do I set realistic career goals?",
    "What are some tips for effective email communication in professional settings?",
    "How can I ensure continuous professional development in my field?",
    "What are some best practices for conducting informational interviews?",
    "How do I handle job application follow-ups?",
    "What are some tips for cold emailing potential employers?",
    "How do I build confidence for public speaking?",
    "What are some common behavioral interview questions and effective responses?",
    "How can I use volunteer experience to enhance my resume?",
    "What are some strategies for developing a professional brand?",
    "How can I handle unexpected questions in a job interview?",
    "What are some effective strategies for stress management during job transitions?",
    "How can I effectively manage a team remotely?",
    "What are some tips for successful project management in cross-functional teams?",
    "How do I balance detail-oriented tasks with big-picture strategy in my job?",
    "What are some effective conflict resolution strategies in the workplace?",
    "How can I develop a strong professional network early in my career?",
    "What are some advanced tips for LinkedIn networking and job search?",
    "How do I transition from a technical role to a management role?"
]
titles = titles * 5

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
        a = Answer(answer=row['answer'], likes=row['likes'], user_id=row['user_id'])
        db.session.add(a)

    for row in questionTags:
        qt = Question_Tag(question_id=row['question_id'], tag_id=row['tag_id'])
        db.session.add(qt)
except:
    raise Exception("An error occurred.")
else:
    db.session.commit()