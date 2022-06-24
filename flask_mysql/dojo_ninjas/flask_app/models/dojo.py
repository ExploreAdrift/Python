from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at ,updated_at) VALUES (%(name)s, NOW(),NOW());"
        result = connectToMySQL("dojo_ninjas").query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojo_ninjas").query_db(query)
        result = []
        for dojo in results:
            result.append(cls(dojo))
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL("dojo_ninjas").query_db(query, data)
        return cls(result[0])
