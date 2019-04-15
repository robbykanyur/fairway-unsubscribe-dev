from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import Unsubscribe

class UnsubscribeForm(FlaskForm):
    email = HiddenField('Email', validators=[DataRequired(), Email()])
    address = HiddenField('Address', validators=[DataRequired()])
    submit = SubmitField('Unsubscribe')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Authenticate')
