import requests

from crypt import methods
from urllib import response
from flask_app import app

from flask import render_template, request, redirect, session, flash, jsonify, json


from flask_app.models.trip_model import Trip
from flask_app.models.user_model import User

api_key = "KM6GVGPUq1KIgRdQQ0reDxraYdKvOqnDy3Rwcy0G"


@app.route('/create_trip')
def park():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    user_id = session['user_id']
    return render_template('create_trip.html', user_id=user_id)


@app.route('/create_new_trip', methods=["POST"])
def submit_new_trip():
    session["state"] = request.form["state"]
    data = {
        "user_id": session["user_id"],
        "start_trip_date": request.form["start_trip_date"],
        "end_trip_date": request.form["end_trip_date"],
        "num_people": request.form["num_people"]
    }
    trip_id = Trip.new_trip(data)
    print(trip_id)
    session["trip_id"] = trip_id
    return redirect("/choose_park")


@app.route('/park_info')
def wildlife():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    user_id = session['user_id']
    return render_template('park_info.html', user_id=user_id)


@app.route('/edit_trip')
def edit_trip():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    user_id = session['user_id']
    return render_template('edit_trip.html', user_id=user_id)


@app.route('/dashboard')
def view_trip():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    parks = Trip.new_trip(data)
    return render_template('dashboard.html', user=user, parks=parks)


@app.route('/choose_park')
def choose_park():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    user_id = session['user_id']
    return render_template('choose_park.html')


@app.route('/api/choose_park')
def api_choose_park():
    state = session["state"]
    state_parks = f"https://developer.nps.gov/api/v1/parks?stateCode={state}&api_key={api_key}"
    response = requests.get(url=state_parks)
    data = response.json()
    return jsonify(data)


@app.route("/api/show_park")
def api_show_park():
    park_id = session["park_id"]
    state_park = f"https://developer.nps.gov/api/v1/parks?parkCode={park_id}&stateCode=&api_key={api_key}"
    response = requests.get(url=state_park)
    data = response.json()
    return jsonify(data)


@app.route("/submit_park", methods=["POST"])
def submit_park():
    print(request.form)
    data = {
        "park_id": request.form["park_id"],
        "id": session["trip_id"]
    }
    session["park_id"] = request.form["park_id"]
    Trip.add_park(data)
    return redirect("/trip/plans")


@app.route("/trip/plans")
def trip_plans():

    return render_template("trip_plans.html")
