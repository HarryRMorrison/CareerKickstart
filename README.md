# CareerKickstart
Welcome to CareerKickstart, the dedicated platform for interns and graduates seeking guidance in the early stages of their careers. At CareerKickstart, we recognize the challenges that come with transitioning from academic life to professional environments, and we are committed to providing the support necessary for you to navigate this journey effectively.

Our website offers a range of resources specifically designed for those entering the workforce. Whether you're searching for your first internship, a graduate position, or simply exploring different career options, CareerKickstart is here to assist you. We provide practical advice, professional insights, and a wealth of information to help enhance your job search skills.

Explore our database of opportunities, receive career coaching tailored to your needs, and connect with a network of professionals and like-minded peers. CareerKickstart is more than just a job search site; it's a partner in your professional development. Join us today to start shaping your future.

## Design
The design of a Flask application involves setting up a Python-based web framework that is both simple and extensible. Initially, you would set up a virtual environment and install Flask. The core of a Flask application includes an application file, 'carreer-kickstart.py', which configures and creates an instance of the Flask class. Routes are defined in this file or in associated modules using decorators to link view functions to URLs, handling web page requests and determining the content to be displayed. The application uses Jinja2 templates for HTML content rendering, allowing dynamic generation of web pages with placeholders for data filled during runtime. Static files like CSS, JavaScript, and images are stored separately to manage presentation and functionality. Blueprints are used to organize the application into modular components, each capable of functioning independently. The application configuration might include details such as database connections, secret keys, and third-party services, often loaded from a configuration object or file. Flask can integrate with databases using extensions like SQLAlchemy and manage errors through custom handlers, ensuring robustness. SQLalchemy is good as it implements user authentication using Flask-Login, avoids CSS attacks and together with WTForms, it avoids CRSF attacks. Running the Flask app involves starting a development server with 'flask run', which serves the application to users.

The database was designed on the components other help forums have incommon. Questions, answers, tags and users. These form the base components. A relationship table was set up for Question tags as it increased efficiency and decreased storage capacity. Numerous help functions are used through the application.

## Setup
Set up a virtual environment in Unix:
1. Use pip or another package manager to install virtualenv package <code>pip install virtualenv</code>
3. Install a venv environment <code>python -m venv venv</code> and install packages <code>pip install -r requirements.txt</code>
2. Start the virtual environment <code>source virtual-environment/bin/activate</code> This should include flask and all the required packages
Install sqlite
4. Install sqlite3 <code>sudo apt-get install sqlite</code>
5. Build the database: <code>flask db init</code>
6. To create a database sample with data <code>python "sample-data-generation"</code>

## Getting Started
1. Activate the Virtual Environment
    - <code>source venv/bin/activate</code>

2. Start up server:
    - <code>Flask run</code>

3. Stopping the Server:
    - <code>^C</code>

4. Deactivating the Virtual Environment:
    - <code>deactivate</code>

## Running the tests
To run unit tests: <code>python -m tests.unittest</code>

To run selenium tests: <code>python -m tests.systemtest</code>
- You may find issues in your environment, if so run this Unix line <code>sudo apt install chromium-chromedriver</code>

## Useful Functions
Start the python interpreter in context of application (pre-import “app”)
- <code>flask shell</code>

Create migration repository:
- <code>flask db init</code>

Each time a table is added:
- <code>flask db migrate -m "users table"</code>

Upgrade to most recent db:
- <code>flask db upgrade</code>

Downgrade to no tables:
- <code>flask db downgrade base</code>

Upgrade to all tables:
- <code>flask db upgrade</code>

## Deployment
via localhost

## Built With
VScode, git, flask

## Source Code
https://github.com/HarryRMorrison/CareerKickstart

## Authors

* **Harry Morrison** 23403634 - [GitHub Profile - HarryRMorrison](https://github.com/HarryRMorrison) & [harryM24](https://github.com/harryM24)
* **Emily** 23374456 - [GitHub Profile - EmilyRuii](https://github.com/EmilyRuii)
* **Jessica** 23367247 - [GitHub Profile - JessicaShindunata](https://github.com/JessicaShindunata)
* **Meg** 23390643 - [GitHub Profile - megGoody](https://github.com/megGoody)

