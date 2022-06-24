from flask_app.config.mysqlconnection import connectToMySQL


from flask import flash

from flask_app.models.user_model import User
from flask_app import DATABASE


class Sight:
    def __init__(self, data):
        self.id = data["id"]
        self.location = data["location"]
        self.what_happened = data["what_happened"]
        self.date_sight = data["date_sight"]
        self.num_sasq = data["num_sasq"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def new_sight(cls, data):
        query = "INSERT INTO sight (location, what_happened, date_sight, num_sasq, created_at, updated_at, user_id) VALUES(%(location)s,%(what_happened)s, %(date_sight)s, %(num_sasq)s, NOW(), NOW(), %(user_id)s);"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def edit_sight(cls, data):

        query = 'UPDATE sight SET location = %(location)s, what_happened = %(what_happened)s, date_sight = %(date_sight)s,'
        query += 'num_sasq = %(num_sasq)s, updated_at = NOW() WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM sight WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sight WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_name(cls):
        query = "SELECT * FROM sight join users on sight.user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        sight = []
        for row in result:
            sighting = cls(row)
            user_sighted = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "pw_hash": row["pw_hash"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]

            }
            sighting.user = User(user_sighted)
            sight.append(sighting)
        return sight
    # joined classmethod to retrieve name ("sighted by (name)")
    # joined classmethod to retrieve name ("sighted by (name)")
    # joined classmethod to retrieve name ("sighted by (name)")

    @staticmethod
    def validate_sight_present(user):
        is_valid = True
        if not len(user['location']) > 0:
            flash('You must enter a location!', 'err.location')
            is_valid = False
        if not len(user['what_happened']) > 0:
            flash('You must enter a description on what happened!', 'err.what')
            is_valid = False
        if not len(user['date_sight']) > 0:
            flash('You must enter the date  the beast was sighted!', 'err.date')
            is_valid = False
        if not user['num_sasq']:
            flash('You must enter how many there were!', 'err.num')
            is_valid = False
        if not len(user['location']) > 2:
            flash('Location must be at least 3 charaters!', 'err.location')
            is_valid = False
        if not len(user['what_happened']) > 2:
            flash('What happened must be at least 3 charaters!', 'err.what')
            is_valid = False
        if not len(user['date_sight']) > 2:
            flash('Number sighted must be at least 3 charaters!', 'err.date')
            is_valid = False
        return is_valid
