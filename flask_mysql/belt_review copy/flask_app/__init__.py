from flask import Flask
app = Flask(__name__)

app.secret_key = "recipe"

# setting global Variable for database name
DATABASE = "recipe_db"
