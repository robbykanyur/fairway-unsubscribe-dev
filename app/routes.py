from app import app, db
from flask import render_template, redirect, url_for, request, flash
from app.forms import UnsubscribeForm, LoginForm
from app.models import Unsubscribe, User
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.route('/')
def index():
    address = request.remote_addr
    email = request.args.get('email')
    form = UnsubscribeForm(email=email, address=address)
    return render_template('index.html', email=email, form=form, address=address)

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    form = UnsubscribeForm()
    if form.validate_on_submit():
        unsubscribe = Unsubscribe(email=form.email.data, address=form.address.data)
        db.session.add(unsubscribe)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    unsubscribes = Unsubscribe.query.all()
    return render_template('admin.html', unsubscribes=unsubscribes, title="Authenticate")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Authenticate', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
