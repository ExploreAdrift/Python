from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    print("Index route")
    return render_template("index.html", num=5, row=5)


@app.route('/<int:x>')
def second_one(x):
    return render_template("index.html", num=8, row=x)


@app.route('/<int:x>/<int:y>')
def third_one(x, y):
    return render_template("index.html", num=x, row=y)


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def fourth_one(x, y, color1, color2):
    return render_template("index.html", num=x, row=y)


if __name__ == "__main__":
    app.run(debug=True)
