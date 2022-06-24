from flask_app import app

from flask import render_template, request, redirect, session, flash


from flask_app.models.pypie_model import Pypie
from flask_app.models.user_model import User


@app.route('/edit_pypie/<int:pypie_id>')
def edit_pypie(pypie_id):
    if 'user_id' not in session:
        flash('You must register or log in to view content.')
        return redirect('/')
    data = {
        'id': pypie_id
    }
    pypie = Pypie.get_one_pie(data)
    return render_template('edit_pypie.html', pypie=pypie)


@app.route('/send_edit/<int:id>', methods=['POST'])
def send_edit(id):
    if not Pypie.validate_pypie_present(request.form):
        return redirect(f'/edit_pypie/{id}')

    data = {
        'id': id,
        'location': request.form['location'],
        'what_happened': request.form['what_happened'],
        'date_pypie': request.form['date_pypie'],
        'num_sasq': request.form['num_sasq'],
    }
    Pypie.edit_pypie(data)
    return redirect('/dashboard')


# @app.route('/create_pypie')
# def create_pypie():
#     if 'user_id' not in session:
#         flash('You must register or login to view content.')
#         return redirect('/')
#     user_id = session['user_id']
#     return render_template('new_pypie.html', user_id=user_id)


@app.route('/creae_pypie', methods=['POST'])
def submit_new():
    if not Pypie.validate_pypie_present(request.form):
        return redirect('/create_pypie')
    Pypie.add_new_pie(request.form)
    return redirect(f'/edit_pypie/{id}')


@app.route('/show_pypie/<int:id>')
def show_pypie(id):
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    data = {
        'id': id
    }
    # we call the classmethod to get the dictionary for this id and set a variable to pass to html
    pypie = Pypie.get_one_pie(data)

    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template('show_pypie.html', user=user, pypie=pypie)


@app.route('/delete_pypie/<int:id>')
def delete_pypie(id):

    data = {
        'id': id
    }
    Pypie.delete(data)
    return redirect('/dashboard')
