import os
import base64
import logging
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from .momentjs import momentjs
from flask_login import LoginManager
from flask_webpack import Webpack
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

FLASK_ENV = os.getenv('FLASK_ENV')

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
webpack = Webpack()
login.login_view = 'main.login'

if (FLASK_ENV == 'production'):
    SENTRY_DSN = base64.b64decode(os.getenv('SENTRY_DSN')).decode('utf-8')
    sentry_sdk.init(
       dsn=SENTRY_DSN,
       integrations=[FlaskIntegration()],
    )

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    webpack.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    app.jinja_env.globals['momentjs'] = momentjs

    if __name__ != '__main__':
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)    

    return app

from app import models
