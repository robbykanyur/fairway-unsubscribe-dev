from os import path
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from .momentjs import momentjs
from flask_login import LoginManager
from flask_webpack import Webpack

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
webpack = Webpack()
login.login_view = 'main.login'

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

    return app

from app import models
