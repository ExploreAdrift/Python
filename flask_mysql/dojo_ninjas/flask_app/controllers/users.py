from crypt import methods
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect("/dojos")


@app.route('/dojos')
def users():
    dojos = Dojo.get_all()
    return render_template("dojo.html", dojos=dojos)


@app.route("/dojos/make", methods=["POST"])
def new_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")


@ app.route("/ninjas")
def new():
    dojos = Dojo.get_all()
    return render_template("ninja.html", dojos=dojos)


# COME BACK TO THIS
@ app.route("/dojo/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    ninjas = Ninja.get_ninja_dojo(data)
    dojo = Dojo.get_one(data)
    return render_template("show.html", ninjas=ninjas, dojo=dojo)


@app.route("/ninja/make", methods=["POST"])
def new_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    Ninja.ninja(data)
    print(data)
    return redirect("/dojos")


# table_name_singular/<int:id>/action
# user/new --> displays the form to add new user
# user/create --> action
# user/<int:id> --> displays user info
# user/<int:id>/edit displays form in order to change info
#  user/<int:id>/update --> action --> updates in the db the changes form to the edit route
#  user/<int:id>/delete --> action --> deletes user from database
