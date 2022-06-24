# allows our model to talk to the database
from flask_app.config.mysqlconnection import connectToMySQL

# allows us to flash messages onto our HTML pages
from flask import flash

# allows us to use gloabl DATABASE variable
from flask_app import DATABASE

# import REGEX to validate emails
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

# time to build our class
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_user(cls, data):
        query = 'INSERT INTO register (first_name, last_name, email, pw_hash, created_at, updated_at)' 
        query += 'VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());'
        # send the query to your MySQL database to save the new user in the users table
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM register WHERE email = %(email)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])
    
    @classmethod
    def get_one(cls,data):
        query= "SELECT * FROM register WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])
        

    @staticmethod
    def validate_all_present(user):
        if not len(user['first_name']) > 0:
            flash('You must enter a first name!')
            return False
        if not len(user['last_name']) > 0:
            flash('You must enter a last name!')
            return False
        if not len(user['email']) > 0:
            flash('You must enter an email!')
            return False
        if not len(user['pw']) > 0:
            flash('You must enter a password!')
            return False
        if not len(user['pw1']) > 0:
            flash('You must confirm your password!')
            return False
        return True

    @staticmethod
    def validate_user(user):
        if not len(user['first_name']) >= 2:
            flash('First name must be at least 2 characters!')
            return False
        if not len(user['last_name']) >= 2:
            flash('Last name must be at least 2 characters!')
            return False
        if not user['pw'] == user['pw1']:
            flash('Passwords must match!')
            return False
        return True

    
    @staticmethod
    def validate_email(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!')
            is_valid = False
        return is_valid
    
    
    @staticmethod
    def email_exist(user):
        if User.get_by_email(user):
            flash('This email is already in use!')
            return False
        return True
