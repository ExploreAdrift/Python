# allows our model to talk to db
from flask_app.config.mysqlconnection import connectToMySQL
# allows us flash messages onto html page (EX email doesnt exist)
from flask import flash

# allows us to use global DATABASE variable
from flask_app import DATABASE

# allows REGEX to validate emails
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

# time to build class


# time to build our class
class User:
    def __init__(self, data):
        # refer to tables in db to ensure you have all required columns/attributes
        # all attributes must refer to the variable passed (data) and a key
        # use [] and quotes to give key
        # ensure all attribute names match the column name in db
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # put any individual methods here
    # these are actions that a single instance of the class performs (user.do_something)

    # write any class methods here (all methods will pass through cls at a minimum)

    # classmethod to create a new user, requires us to pass user information in using data
    @classmethod
    def new_user(cls, data):
        # query is the exact query you would enter into MySQL inside of the quotes
        # use the %()s to mogrify the data and prevent SQL injection into the db
        query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at)'
        query += 'VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());'
        # send the query to your MySQL database to save the new user in the users table
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # this will retrieve user id
    @classmethod
    def get_one(cls, data):
        # we need to query the database to grab the instance of user by id
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        # here we want to return only the first row as a dicitonary with the data from the selected id
        return cls(result[0])

    # This method will get user by email address
    # if the email does not exist in the database it will return false
    # if the email exists it will return the row with the user information
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    # Static methods here (static methods apply to instance of the class, without effecting the instance)
    # Usually used for validation and to check data in the class without changing the data

    # This method checks that all fields have something entered
    # flashses a message if there is nothing entered into that field
    @staticmethod
    def validate_all_present(user):
        is_valid = True
        if not len(user['first_name']) > 0:
            # the first quotes are the message text, the second are the message category
            flash('You must enter a first name!', 'err.first_name')
            is_valid = False
        if not len(user['last_name']) > 0:
            flash('You must enter a last name!', 'err.last_name')
            is_valid = False
        if not len(user['email']) > 0:
            flash('You must enter an email!', 'err.email')
            is_valid = False
        if not len(user['pw']) > 0:
            flash('You must enter a password!', 'err.pw')
            is_valid = False
        if not len(user['pw1']) > 0:
            flash('You must confirm your password!', 'err.pw')
            is_valid = False
        if not len(user['first_name']) >= 2:
            flash('First name must be at least 2 characters!', 'err.first_name')
            is_valid = False
        if not len(user['last_name']) >= 2:
            flash('Last name must be at least 2 characters!', 'err.last_name')
            is_valid = False
        if not user['pw'] == user['pw1']:
            flash('Passwords must match!', 'err.pw')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', 'err.email')
            is_valid = False
        if User.get_by_email(user):
            flash('This email is already in use!', 'err.email')
            return False
        return is_valid

# these static methods were commented out on refactor to consolidate and display all error messages at once
# all validation checks now occur in the validate_all_present staticmethod

    # # This method will validate name length and that both passwords match
    # @staticmethod
    # def validate_user(user):
    #     if not len(user['first_name']) >= 2:
    #         flash('First name must be at least 2 characters!', 'error_first_name')
    #         return False
    #     if not len(user['last_name']) >= 2:
    #         flash('Last name must be at least 2 characters!','err.last_name')
    #         return False
    #     if not user['pw'] == user['pw1']:
    #         flash('Passwords must match!', 'err.pw')
    #         return False
    #     return True

    # # This method will validate the email is in the correct format
    # @staticmethod
    # def validate_email(user):
    #     is_valid = True
    #     if not EMAIL_REGEX.match(user['email']):
    #         flash('Invalid email address!')
    #         is_valid = False
    #     return is_valid

    # This method will check to see if the email exists in the database
    # If this email exists it will not allow the user to create a new account
    # @staticmethod
    # def email_exist(user):
    #     if User.get_by_email(user):
    #         flash('This email is already in use!')
    #         return False
    #     return True
