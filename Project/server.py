from flask_app.controllers import trip_controller, user_controller
import flask_app

from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)
