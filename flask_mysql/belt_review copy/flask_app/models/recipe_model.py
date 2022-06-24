from flask_app.config.mysqlconnection import connectToMySQL
# allows us flash messages onto html page (EX email doesnt exist)

from flask import flash


from flask_app import DATABASE


class Recipe:
    def __init__(self, data):
        # ALWAYS REFERECE THE TABLE IN MYSQL TO ENSURE YOU ARENT MISSING AN COLUMNS
        # ENSURE ALL ATRRIBUTE NAMES ARE THE SAME AS THE COLUMN NAMES IN SAME ORDER
        self.id = data["id"]
        self.name = data["name"]
        self.under_30 = data["under_30"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

# individual methods will go here (recipe. do_something())

    # classmethods here
    # this method will allow us to make a recipe and save it in the db
    @classmethod
    def new_recipe(cls, data):
        query = 'INSERT INTO recipes (name, under_30, description, instructions, date_made, created_at, updated_at, user_id)'
        query += 'VALUES (%(name)s, %(under_30)s, %(description)s, %(instructions)s, %(date_made)s, NOW(), NOW(), %(user_id)s);'
        # send this query line to the database, this will return the recipe id
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # this method will allow us to get a list of dictionaries containing all recipes
    @classmethod
    def get_all_recipes(cls):
        query = 'SELECT * FROM recipes;'
        result = connectToMySQL(DATABASE).query_db(query)
        # we need a blank list to put our dictionaries into
        recipes = []
        # we are going to check each row in the table
        for row in result:
            # for every row we return, we want to append the dictionary into the recipes list
            recipes.append(cls(row))
        # we are going to send back the list of dictionaries to the controller
        return recipes

    # this method will allow us to edit the recipe entry
    @classmethod
    def edit_recipe(cls, data):
        # make sure to check all your mogrify text to ensure it matches the column names in the table
        query = 'UPDATE recipes SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s,'
        query += 'instructions = %(instructions)s, date_made = %(date_made)s, updated_at = NOW() WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # this method will allow us to get the information for 1 recipe
    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # we are taking the first dictionary and returning that as our value
        return cls(result[0])

    # this method will delete the recipe given the id
    @classmethod
    def delete(cls, data):
        # we do be deletin shit tho
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # this will not return anything as delete queries do not return a value
        return result

    # static methods for validations
    # this method will check that the all the fields are filled out

    @staticmethod
    def validate_recipe_present(user):
        if not len(user['name']) > 0:
            flash('You must enter a name!')
            return False
        if not len(user['description']) > 0:
            flash('You must enter a description!')
            return False
        if not len(user['instructions']) > 0:
            flash('You must enter instructions!')
            return False
        if not user['date_made']:
            flash('You must enter a date made on!')
            return False
        if not user['under_30']:
            flash('You must select if this is under 30 minutes!')
            return False
        return True

    # this will check if if all fields have at least 3 characters
    @staticmethod
    def recipe_length(user):
        if not len(user['name']) > 2:
            flash('Name must be at least 3 charaters!')
            return False
        if not len(user['description']) > 2:
            flash('Description must be at least 3 charaters!')
            return False
        if not len(user['instructions']) > 2:
            flash('Instructions must be at least 3 charaters!')
            return False
        return True
