import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or '02d8a604f76346043d3f9e90f4c57366'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    SF_USERNAME = os.getenv('SF_USERNAME')
    SF_PASSWORD = os.getenv('SF_PASSWORD')
    SF_SECURITY_TOKEN = os.getenv('SF_SECURITY_TOKEN')
    SF_ACCESS_TOKEN = os.getenv('SF_ACCESS_TOKEN')
    SF_INSTANCE_URL = os.getenv('SF_INSTANCE_URL')
    SF_OAUTH = os.getenv('SF_OAUTH') or 'https://login.salesforce.com/services/oauth2/token'
