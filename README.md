# CareerKickstart
Welcome to CareerKickstart, the dedicated platform for interns and graduates seeking guidance in the early stages of their careers. At CareerKickstart, we recognize the challenges that come with transitioning from academic life to professional environments, and we are committed to providing the support necessary for you to navigate this journey effectively.

Our website offers a range of resources specifically designed for those entering the workforce. Whether you're searching for your first internship, a graduate position, or simply exploring different career options, CareerKickstart is here to assist you. We provide practical advice, professional insights, and a wealth of information to help enhance your job search skills.

Explore our database of opportunities, receive career coaching tailored to your needs, and connect with a network of professionals and like-minded peers. CareerKickstart is more than just a job search site; it's a partner in your professional development. Join us today to start shaping your future.

## Getting Started
1. Activate the Virtual Environment
    - <code>source venv/bin/activate</code>

2. Start up server:
    - <code>Flask run</code>

3. Stopping the Server:
    - <code>cntrl + c</code>

4. Deactivating the Virtual Environment:
    - <code>deactivate</code>

## Setup
Set up a virtual environment in Unix:
1. Use pip or another package manager to install virtualenv package <code>pip install virtualenv</code>
3. Install a venv environment <code>python3.12 -m venv venv</code> and install packages <code>pip install -r requirements.txt</code>
2. Start the virtual environment <code>source virtual-environment/bin/activate</code> This should include flask and all the required packages
Install sqlite
4. Install sqlite3 <code>sudo apt-get install sqlite</code>
5. Build the database: <code>flask db init</code>
6. <code>flask run</code>

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
VScode and git

## Source Code
https://github.com/HarryRMorrison/CareerKickstart

## Authors

* **Harry Morrison** 23403634 - [GitHub Profile - HarryRMorrison](https://github.com/HarryRMorrison) & [harryM24](https://github.com/harryM24)
* **Emily** 23374456 - [GitHub Profile - EmilyRuii](https://github.com/EmilyRuii)
* **Jessica** 23367247 - [GitHub Profile - JessicaShindunata](https://github.com/JessicaShindunata)
* **Meg** 23390643 - [GitHub Profile - megGoody](https://github.com/megGoody)

