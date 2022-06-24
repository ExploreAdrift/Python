from argparse import Action
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect("/users")


@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all_now())


@app.route("/users/new")
def new():
    return render_template("new_user.html")


@app.route("/users/create", methods=["POST"])
def create():
    User.save(request.form)
    return redirect("/users")


@app.route("/users/edit/<int:id>")
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", users=User.get_one(data))


@app.route("/users/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")


@app.route("/users/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")


@app.route("/users/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", users=User.get_one(data))

# table_name_singular/<int:id>/action
# user/new --> displays the form to add new user
# user/create --> action
# user/<int:id> --> displays user info
# user/<int:id>/edit displays form in order to change info
#  user/<int:id>/update --> action --> updates in the db the changes form to the edit route
#  user/<int:id>/delete --> action --> deletes user from database
