import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or '02d8a604f76346043d3f9e90f4c57366'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONSUMER_KEY = os.getenv('CONSUMER_KEY') or ''
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET') or ''
    SF_USERNAME = os.getenv('SF_USERNAME') or ''
    SF_PASSWORD = os.getenv('SF_PASSWORD') or ''
    SF_SECURITY_TOKEN = os.getenv('SF_SECURITY_TOKEN') or ''
    SF_ACCESS_TOKEN = os.getenv('SF_ACCESS_TOKEN') or ''
    SF_INSTANCE_URL = os.getenv('SF_INSTANCE_URL') or ''
    SF_OAUTH = os.getenv('SF_OAUTH') or 'https://login.salesforce.com/services/oauth2/token'
    SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN') or ''
    SLACK_BOT_CHANNEL = os.getenv('SLACK_BOT_CHANNEL') or 'unsubscribe'
    SLACK_BOT_USERNAME = os.getenv('SLACK_BOT_USERNAME') or 'trumpeter'
