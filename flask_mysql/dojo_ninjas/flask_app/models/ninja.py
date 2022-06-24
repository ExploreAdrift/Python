from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all_now(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojo_ninjas").query_db(query)
        ninjas = []
        for u in results:
            ninjas.append(cls(u))
        return ninjas

    @classmethod
    def ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age,dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())"
        result = connectToMySQL("dojo_ninjas").query_db(query, data)
        return result

    @classmethod
    def get_ninja_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        result = connectToMySQL("dojo_ninjas").query_db(query, data)
        ninjas = []
        for row in result:
            ninjas.append(cls(row))
        return ninjas
