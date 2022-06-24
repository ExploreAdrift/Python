from flask_app.config.mysqlconnection import connectToMySQL


from flask import flash

from flask_app.models.user_model import User
from flask_app import DATABASE


class Pypie:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.filling = data["filling"]
        self.crust = data["crust"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def add_new_pie(cls, data):
        query = "INSERT INTO pypie (name, filling, crust, created_at, updated_at, user_id) VALUES(%(name)s,%(filling)s, %(crust)s, NOW(), NOW(), %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def edit_py(cls, data):
        query = 'UPDATE pypie SET name = %(name)s, filling = %(filling)s, crust = %(crust)s,'
        query += 'created_at = NOW() updated_at = NOW() WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one_pie(cls, data):
        query = "SELECT * FROM pypie WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pypie WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_name(cls):
        query = "SELECT * FROM pypie join users on pypie.user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        pypie = []
        for row in result:
            piepie = cls(row)
            user_pie = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "pw_hash": row["pw_hash"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            piepie.user = User(user_pie)
            pypie.append(piepie)
        return pypie

    @staticmethod
    def validate_pypie_present(user):
        is_valid = True
        if not len(user['name']) > 0:
            flash('You must enter a name!', 'err.name')
            is_valid = False
        if not len(user['filling']) > 0:
            flash('You must enter a filling!', 'err.filling')
            is_valid = False
        if not len(user['crust']) > 0:
            flash('You must enter a crust!', 'err.crust')
            is_valid = False
        if not len(user['name']) > 1:
            flash('name must be at least 2 charaters!', 'err.name')
            is_valid = False
        if not len(user['filling']) > 2:
            flash('Filling must be at least 3 charaters!', 'err.filling')
            is_valid = False
        if not len(user['crust']) > 2:
            flash('Crust must be at least 3 charaters!', 'err.crust')
            is_valid = False
        return is_valid
