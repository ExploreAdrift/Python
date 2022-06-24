from flask_app.config.mysqlconnection import connectToMySQL


from flask import flash

from flask_app.models.user_model import User
from flask_app import DATABASE


class Band:
    def __init__(self, data):
        self.id = data["id"]
        self.band_name = data["band_name"]
        self.genre = data["genre"]
        self.home_city = data["home_city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def new_band(cls, data):
        query = "INSERT INTO band (band_name, genre, home_city, created_at, updated_at, user_id) VALUES(%(band_name)s, %(genre)s, %(home_city)s, NOW(), NOW(), %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def edit_band(cls, data):

        query = 'UPDATE band SET band_name = %(band_name)s, genre = %(genre)s,'
        query += 'home_city = %(home_city)s, updated_at = NOW() WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM band WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM band WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_name(cls):
        query = "SELECT * FROM band join users on band.user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        band = []
        for row in result:
            found = cls(row)
            user_founded = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "pw_hash": row["pw_hash"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]

            }
            found.user = User(user_founded)
            band.append(found)
        return band
    # joined classmethod to retrieve name ( by (name)")
    # joined classmethod to retrieve name ("by (name)")
    # joined classmethod to retrieve name ("by (name)")

    @staticmethod
    def validate_band(band):
        is_valid = True
        if not len(band['band_name']) > 0:
            flash('You must enter a band name!', 'err.name')
            is_valid = False
        if not len(band['genre']) > 0:
            flash('You must enter a genre!', 'err.genre')
            is_valid = False
        if not len(band['home_city']) > 0:
            flash('You must enter home city!', 'err.home')
            is_valid = False
        if not len(band['band_name']) > 2:
            flash('band name must be at least 3 charaters!', 'err.name')
            is_valid = False
        if not len(band['genre']) > 2:
            flash('genre must be at least 3 charaters!', 'err.genre')
            is_valid = False
        if not len(band['home_city']) > 2:
            flash('home city must be at least 3 charaters!', 'err.home')
            is_valid = False
        return is_valid
