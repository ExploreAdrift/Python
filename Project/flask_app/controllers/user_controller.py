from flask_app import app

from flask import render_template, request, redirect, session, flash
import requests

from flask_app.models.trip_model import Trip
from flask_app.models.user_model import User

# import bcrypt to hash password info
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_all_present(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'pw_hash': pw_hash
    }
    user_id = User.new_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash('email or password is invalid', "err.log_email")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.pw_hash, request.form['pw']):
        flash('Invalid email or password!', "err.log_pw")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    # we need to make sure there has been a login to render this page
    if 'user_id' not in session:
        # if there is no user_id in our session, no one has logged in or the user has logged out
        flash('You must register or log in to view content.', 'err.log_email')
        return redirect('/')

    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    parks = Trip.new_trip()
    return render_template('dashboard.html', user=user, parks=parks)


@app.route('/logout')
def logout():
    # this will clear all values from session
    # can use session.pop(key) if you need to keep certian session values intact
    # must pop all values in order to clear the session
    session.clear()
    return redirect('/')
