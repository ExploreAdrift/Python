from flask_app import app

from flask import render_template, request, redirect, session, flash


from flask_app.models.sight_model import Sight
from flask_app.models.user_model import User


@app.route('/edit_sight/<int:sight_id>')
def edit_sight(sight_id):
    if 'user_id' not in session:
        flash('You must register or log in to view content.')
        return redirect('/')
    data = {
        'id': sight_id
    }
    sight = Sight.get_one(data)
    return render_template('edit_sight.html', sight=sight)


@app.route('/send_edit/<int:id>', methods=['POST'])
def send_edit(id):
    if not Sight.validate_sight_present(request.form):
        return redirect(f'/edit_sight/{id}')

    data = {
        'id': id,
        'location': request.form['location'],
        'what_happened': request.form['what_happened'],
        'date_sight': request.form['date_sight'],
        'num_sasq': request.form['num_sasq'],
    }
    Sight.edit_sight(data)
    return redirect('/dashboard')


@app.route('/create_sight')
def create_sight():
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    user_id = session['user_id']
    return render_template('new_sight.html', user_id=user_id)


@app.route('/new_sight', methods=['POST'])
def submit_new():
    if not Sight.validate_sight_present(request.form):
        return redirect('/create_sight')
    Sight.new_sight(request.form)
    return redirect('/dashboard')


@app.route('/show_sight/<int:id>')
def show_sight(id):
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    data = {
        'id': id
    }
    # we call the classmethod to get the dictionary for this id and set a variable to pass to html
    sight = Sight.get_one(data)

    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template('show_sight.html', user=user, sight=sight)


@app.route('/delete_sight/<int:id>')
def delete_sight(id):

    data = {
        'id': id
    }
    Sight.delete(data)
    return redirect('/dashboard')
