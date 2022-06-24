from flask_app import app

# import all features we will need to run the app routes
from flask import render_template, redirect, request, session, flash

# import all models we will need to access for class/static methods
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


# import bcrypt to hash password info
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# app route for first visit page
@app.route('/')
def index():
    # checks if a user is currently logged in
    if 'user_id' in session:
        # if a user_id is found, we send them to the dashboard page
        return redirect('/dashboard')
    return render_template('index.html')

# app route to register users
# DONT FORGET TO ADD POST, USE A COMMA, AND PROPER BRACKETS/QUOTES
@app.route('/register', methods=['POST'])
def register():
    # call static method to check all values and return true if criteria is met
    # returning true will allow us to continue to the next check, returning false see below
    # if return is False, we will redirect to homepage and flash messages with unmet criteria
    if not User.validate_all_present(request.form):
        return redirect('/')
    # the following static methods for validations have been consolidated into validate_all_present
    # see the user model for more info

    # if not User.validate_user(request.form):
    #     return redirect('/')
    # if not User.validate_email(request.form):
    #     return redirect('/')
    # if not User.email_exist(request.form):
    #     return redirect('/')
    
    # if we pass all of these checks we can now create a new user
    # for security reasons, we need to hash the password before we can store it
    # this will hash the password and allow us to pass a hash instead of a raw password to the db
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    # we need to make a data dictionary to pass into the classmethod that includes our hashed password
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'pw_hash' : pw_hash
    }
    #  we can now safely send the data dict to the db because it contains a hash and not the raw password
    # now we call the class method and send our data dict to the db
    # we set the user id to the id of our new instance of user
    user_id = User.new_user(data)
    # now we set the session id so that we can tell there has been a successful login
    session['user_id'] = user_id
    return redirect('/dashboard')

# This app route will check the login credentials
@app.route('/login', methods=['POST'])
def login():
    # first we set a data dictionary to hold the submitted information
    data ={
        'email':request.form['email']
    }
    # check our database to see if the email exists
    user_in_db = User.get_by_email(data)
    # send the email into our classmethod and check if the user exists
    if not user_in_db:
        # if the user does not exist (returns False), we will send a message and redirect
        flash('email is not registered!')
        return redirect('/')
    # if we pass that check, we need to see if passwords match
    # we compare the hash values to see if the passwords match
    if not bcrypt.check_password_hash(user_in_db.pw_hash, request.form['pw']):
        # if the hash values do not match we send a message and redirect
        flash('Invalid email or password!')
        return redirect('/')
    # now we set the session id so that we can tell if there has been a successful login
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # we need to make sure there has been a login to render this page
    if 'user_id' not in session:
        # if there is no user_id in our session, no one has logged in or the user has logged out
        flash('You must register or log in to view content.')
        return redirect('/')
    # retrieve all recipes for our list and user info
    # we need to create a data dict to send through
    # we have set the id we are sending to the db equal to the session id stored at our user registration or login
    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    # we need to retrieve all the recipes in our database and pass it to our html
    recipes = Recipe.get_all_recipes()
    # we need to pass the user info and recipe info through to be used in our html
    return render_template('dashboard.html', user = user, recipes = recipes)

@app.route('/logout')
def logout():
    # this will clear all values from session
    # can use session.pop(key) if you need to keep certian session values intact
    # must pop all values in order to clear the session
    session.clear()
    return redirect('/')