# allows our model to talk to the database
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User

# allows us to flash messages onto our HTML pages
from flask import flash

# allows us to use gloabl DATABASE variable
from flask_app import DATABASE


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_recipe(cls, data):
        query = "INSERT INTO recipes (name,under_30, description,instructions,date_made, created_at, updated_at)"
        query += "VALUES ( %(name)s, %(under_30)s, %(description)s, %(instructions)s, %(date_made)s, NOW(), NOW()"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = name)s,under_30 = %(under_30)s, description = %(description)s, instruction = %(instructions)s, date_made = %(date_made)s, updated_at = NOW() where id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete_recipe(cla, data):
        query = "DELETE FROM recipes where id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_user_recipe(cls, data):
        query = 'SELECT * FROM pies where user_id= %(user_id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        recipe = []
        if not result:
            return False
        for row in result:
            recipe.append(cls(row))
        return recipe
