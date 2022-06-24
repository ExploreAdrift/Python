from flask_app import app

# import all features we will need to run app_routes
from flask import render_template, request, redirect, session, flash

# import all models will need for class/static method
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

# import bcrypt to hash password info
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# app route for first visit page


@app.route('/')
def index():
    # checks if a user currently logged in
    if "user_id" in session:
        # if a user is found, we send them to log in page
        return redirect("/dashboard")
    return render_template("index.html")

# app route to register users
# DONT FORGET TO ADD POST AND A COMMA AND PROPER BRACKETS


@app.route('/register', methods=["POST"])
def register():
    # CALL STATIC METHOD TO CHECK ALL VALUES AND RETURN TRUE IF CRITERIA IS MET
    # RETURNING TRUE WILL ALLOW US TO CONTINUE TO NEXT CHECK, RETURNING FALSE SEE BELOW
    # IF RETURN IS FALSE, WE WILL REDIRECT RO HOMEPAGE AND FLASH MESSAGES

    if not User.validate_all_present(request.form):
        return redirect("/")
    if not User.validate_user(request.form):
        return redirect("/")
    if not User.validate_email(request.form):
        return redirect("/")
    if not User.email_exist(request.form):
        return redirect("/")
    # if we pass all checks they can create a new user
    # for security reasons we need to hash the password before we store it
    # it will hash the PW instead of putting raw PW into DB
    pw_hash = bcrypt.generate_password_hash(request.form["pw"])
    # we need to make a data dictionary to pass into the classmethod that includes our hashed password
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "pw_hash": pw_hash
    }
    # We can now safely send the data dict to the db because it contains a hash and not the raw password
    # now we call the classmethod and send our data dict to DB.
    # we set the user id to the id of our new instance of user
    user_id = User.new_user(data)
    # set session id to track successful login
    session["user_id"] = user_id
    print(request.form)
    print(session["user_id"])
    return redirect("/dashboard")

# This app will check the login credentials


@app.route("/login", methods=["POST"])
def login():
    # first we set a data dictionary to hold the submitted information
    data = {
        "email": request.form["email"]
    }
    # check our DB to see if email exists
    user_in_db = User.get_by_email(data)
    # send the email into our classmethod to check if it exists
    if not user_in_db:
        # if the user doesnt exist (returns flase) we will send a message and redirect.
        flash("email is not registered")
        return redirect("/")
    # if we pass check we need to see that PWs match #
    # we compare hash values to see if the PW match #
    if not bcrypt.check_password_hash(user_in_db.pw_hash, request.form["pw"]):
        # if the hash values do not match we send a message and redirect
        flash("invalid email or password")
        return redirect("/")
    # now we set the session id so that we can tell if there has beena successful login
    session["user_id"] = user_in_db.id
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    # we need to make sure there has been a login to render to this page
    if "user_id" not in session:
        # if there is not user_id in our session, no one has logged in or the user has logged out
        flash("You must register or login to view content.")
        return redirect("/")
    # retrieve all recipes for our list and user into
    # we need to create a data dict to send through
    # we have set the id we are sending to the db equal to the session id stored at our registration or login
    data = {
        "id": session["user_id"]
    }
    user = User.get_one(data)
    # we need to retrieve all the recipes in our database and pass it on to our HTML
    recipes = Recipe.get_all_recipes()
    # we need to pass the user info through to be used in our HTML
    return render_template("dashboard.html", user=user, recipes=recipes)


@app.route("/logout")
def logout():
    # this will clear out all Values
    # can use session.pop(key) if you need to keep certain session values intact
    # must pop all values in order to clear the session
    session.clear()
    return redirect("/")
