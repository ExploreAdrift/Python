# server won't start without flask
from flask import Flask
app=Flask(__name__)

# Secret key for cookie access, allows use of session
app.secret_key="recipe"

#setting global variable for database name
DATABASE = 'recipe_db'