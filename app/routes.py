from app import app, db
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    email = request.args.get('email')
    return render_template('index.html', email=email)
