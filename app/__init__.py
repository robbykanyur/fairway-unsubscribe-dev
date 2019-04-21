from os import path
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from .momentjs import momentjs
from flask_login import LoginManager
from flask_webpack import Webpack

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
webpack = Webpack()
webpack.init_app(app)
app.jinja_env.globals['momentjs'] = momentjs

from app import routes, models
