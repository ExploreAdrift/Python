from flask_app.config.mysqlconnection import connectToMySQL


from flask import flash

from flask_app.models.user_model import User
from flask_app import DATABASE


class Trip:
    def __init__(self, data):
        self.id = data["id"]
        self.start_trip_date = data["start_trip_date"]
        self.end_trip_date = data["end_trip_date"]
        self.num_people = data["num_people"]
        self.plans = data["plans"]
        self.packing = data["packing"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.park_id = data["park_id"]

    @classmethod
    def new_trip(cls, data):
        query = "INSERT INTO trips (start_trip_date, end_trip_date, num_people, created_at, updated_at, user_id)"
        query += "VALUES(%(start_trip_date)s, %(end_trip_date)s,%(num_people)s, NOW(), NOW(), %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def edit_trip(cls, data):
        query = "UPDATE trips SET park_code = %(park_code)s, start_date = %(start_date)s, end_date = %(end_date)s, num_people = %(num_people)s, plans = %(plans)s, packing = %(packing)s, entrance_fee = %(entrance_fee)s;"
        query += "standard_hours = %(standard_hours)s, state = %(state)s, park_name = %(park_name)s, activity = %(activity)s, created_at = NOW() WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM trips WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def add_park(cls, data):
        query = "UPDATE trips set park_id = %(park_id)s WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
