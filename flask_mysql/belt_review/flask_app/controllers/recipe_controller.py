from sqlite3 import DatabaseError
from flask_app import app

# import all features we will need to run app_routes
from flask import render_template, request, redirect, session, flash


# import all models will need for class/static method
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/edit_recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        flash('You must register or log in to view content.')
        return redirect('/')
    data = {
        'id': recipe_id
    }
    recipe = Recipe.get_one_recipe(data)
    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/send_edit/<int:id>', methods=['POST'])
def send_edit(id):
    # this is going to check that all fields are filled in and have at least 3 characters
    if not Recipe.validate_recipe_present(request.form):
        return redirect(f'/edit_recipe/{id}')
    if not Recipe.recipe_length(request.form):
        return redirect(f'/edit_recipe/{id}')
    # if we pass the validations we can now send the edits to the database
    # we need a data dict because the id is not in the request form
    data = {
        'id': id,
        'name': request.form['name'],
        'under_30': request.form['under_30'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made']
    }
    Recipe.edit_recipe(data)
    # after we have update the recipe we will return the user to the dashboard
    return redirect('/dashboard')


@app.route('/create_recipe')
def create_recipe():
    # this will make sure you're logged in to view the page
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    # we need to pass the user id through so that new recipes have a creator
    user_id = session['user_id']
    return render_template('new_recipe.html', user_id=user_id)


@app.route('/new_recipe', methods=['POST'])
def submit_new():
    # this is going to check that all recipe fields are filled in and more than 3 characters
    if not Recipe.validate_recipe_present(request.form):
        return redirect('/create_recipe')
    if not Recipe.recipe_length(request.form):
        return redirect('/create_recipe')
    # if the form passes validation we can now send it to the db
    Recipe.new_recipe(request.form)
    # after we have created the new recipe we send them back to the dashboard
    return redirect('/dashboard')


@app.route('/show_recipe/<int:id>')
def show_recipe(id):
    # check if user is logged in
    if 'user_id' not in session:
        flash('You must register or login to view content.')
        return redirect('/')
    # we need to grab the recipe information, we have passed through the id from the url
    # we need to set the data dictionary to pass that through
    data = {
        'id': id
    }
    # we call the classmethod to get the dictionary for this id and set a variable to pass to html
    recipe = Recipe.get_one_recipe(data)
    # now we pass the data to the html to render the recipe information
    # we need to get the user data to display the right name
    # we use the variable user to pass the user info dict to the html
    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template('show_recipe.html', recipe=recipe, user=user)


@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    # this classmethod is being called to delete the recipe specified by the id in the url
    # we are using a data dict to pass the id to the database
    data = {
        'id': id
    }
    # this method sends the delete function to the database
    Recipe.delete(data)
    return redirect('/dashboard')
