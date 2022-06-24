from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # notice the 2 new named arguments!
    return render_template("index.html", phrase="hello", times=5)


if __name__ == "__main__":
    app.run(debug=True)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes


@app.route('/success')
def success():
    return "success"


@app.route('/Dojo')
def mojo():
    return "dojo"


@app.route('/say/nick')
def say_name():
    return "nick"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
