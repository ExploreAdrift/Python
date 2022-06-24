from flask_app import app

from flask import render_template, request, redirect, session, flash


from flask_app.models.band_model import Band
from flask_app.models.user_model import User


@app.route('/create_band')
def create_band():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    user_id = session['user_id']
    return render_template('new_band.html', user_id=user_id)


@app.route('/new_band', methods=['POST'])
def submit_new():
    if not Band.validate_band(request.form):
        return redirect('/create_band')
    Band.new_band(request.form)
    return redirect('/dashboard')


@app.route('/show_band/<int:id>')
def show_band(id):
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    data = {
        'id': id
    }
    # we call the classmethod to get the dictionary for this id and set a variable to pass to html
    band = Band.get_one(data)

    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template('show_band.html', user=user, band=band)


@app.route('/delete_band/<int:id>')
def delete(id):

    data = {
        'id': id
    }
    Band.delete(data)
    return redirect('/dashboard')


@app.route('/edit_band/<int:band_id>')
def edit_band(band_id):
    if 'user_id' not in session:
        flash('You must register or log in to view content.')
        return redirect('/')
    data = {
        'id': band_id
    }
    band = Band.get_one(data)
    return render_template('edit_band.html', band=band)


@app.route('/send_edit/<int:id>', methods=['POST'])
def send_edit(id):
    if not Band.validate_band(request.form):
        return redirect(f'/edit_band/{id}')

    data = {
        'id': id,
        'band_name': request.form['band_name'],
        'genre': request.form['genre'],
        'home_city': request.form['home_city'],

    }
    Band.edit_band(data)
    return redirect('/dashboard')
