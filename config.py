import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hq+sdDENkKS(pksPwF]I]"W;mD6L.DF$hEs@<@vQ4OzHSHn8Ge=fQV<Cy)|aPfl'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
	ENV='development'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'CKapp.db')
	FALSK_DEBUG=1

class TestingConfig(Config):
	ENV='testing'
	TESTING=True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'