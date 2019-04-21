import sys
import os
from app import app, db
from flask import render_template, redirect, url_for, request, flash, jsonify, send_file, Response
from app.forms import UnsubscribeForm, LoginForm
from app.models import Unsubscribe, User
from app.salesforce import unsubscribe_user
from app.trumpeter import send_trumpet
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
import json
import csv
from requests import Response

@app.route('/')
def index():
    script_id = 'home'
    address = request.remote_addr
    email = request.args.get('email')
    form = UnsubscribeForm(email=email, address=address)
    return render_template('home.html', script_id=script_id, email=email, form=form, address=address, title="Unsubscribe")

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    form = UnsubscribeForm()
    if form.validate_on_submit():
        sf_response = unsubscribe_user(form.email.data)
        previously = False
        if ('previously' in sf_response.keys()):
            previously = sf_response['previously']
        unsubscribe = Unsubscribe(email=form.email.data, address=form.address.data,
                                  sf_response=sf_response['status_code'],
                                  previously=previously)
        db.session.add(unsubscribe)
        db.session.commit()

        data = {'email': form.email.data, 'previously': previously}
        if sf_response['status_code'] == 200:
            return jsonify(data), 200
        else:
            return jsonify(data), 500
    else:
        return '', 500

@app.route('/trumpeter', methods=['POST'])
def trumpeter():
    send_trumpet(request.json)
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    page = request.args.get('page', 1, type=int)
    unsubscribes = db.session.query(Unsubscribe).order_by(Unsubscribe.timestamp.desc()).paginate(page, 10, False)
    next_url = url_for('admin', page=unsubscribes.next_num) if unsubscribes.has_next else None
    prev_url = url_for('admin', page=unsubscribes.prev_num) if unsubscribes.has_prev else None
    return render_template('admin.html', unsubscribes=unsubscribes.items, title="Admin", prev_url=prev_url,
                           next_url=next_url, page=page, total_pages=unsubscribes.pages)

@app.route('/admin/csv')
@login_required
def admin_csv():
    csv_path = os.path.join(app.instance_path, 'unsubscribe.csv')
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    records = db.session.query(Unsubscribe).all()
    f = open(csv_path, 'w')
    out = csv.writer(f)
    [out.writerow([column.name for column in Unsubscribe.__mapper__.columns])]
    [out.writerow([getattr(curr, column.name) for column in Unsubscribe.__mapper__.columns]) for curr in records]
    f.close()
    return send_file(csv_path, mimetype="text/csv", as_attachment=True, attachment_filename='unsubscribe.csv')

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
            next_page = url_for('admin')
        return redirect(next_page)
    return render_template('login.html', title='Authenticate', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
