from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app import DATABASE

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
