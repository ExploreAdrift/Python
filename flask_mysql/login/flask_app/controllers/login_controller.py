from flask_app import app

# import all features we will need to run the app routes
from flask import render_template, redirect, request, session, flash

# import all models we will need to access for class/static methods

from flask_app.models.login_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    # checks if a user is currently logged in
    if 'id' in session:
        # if a user_id is found, we send them to the dashboard page
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_all_present(request.form):
        return redirect('/')
    if not User.validate_user(request.form):
        return redirect('/')
    if not User.validate_email(request.form):
        return redirect('/')
    if not User.email_exist(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'pw_hash' : pw_hash
    }
    id = User.new_user(data)
    session['id'] = id
    return redirect('/dashboard')

# This app route will check the login credentials
@app.route('/login', methods=['POST'])
def login():
    data ={
        'email':request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('email is not registered!')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.pw_hash, request.form['pw']):
        flash('Invalid email or password!')
        return redirect('/')
    session['id'] = user_in_db.id
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    if "id" not in session:
        flash("You must register or login to view content.")
        return redirect("/")
    
    data = {
        "id": session["id"]
    }
    id = User.get_one(data)
    return render_template("dashboard.html", id = id)

@app.route ("/logout")
def logout():
    session.clear()
    return redirect("/")