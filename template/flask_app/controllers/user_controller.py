from flask_app import app

from flask import render_template, request, redirect, session, flash

from flask_app.models.sight_model import Sight
from flask_app.models.user_model import User

# import bcrypt to hash password info
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
