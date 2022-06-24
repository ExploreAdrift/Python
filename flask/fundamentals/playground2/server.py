from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def three_box():
    return render_template("index.html", num=3)


@app.route('play/<int:num>')
def seven_(num):
    return render_template("index.html", num=num)


@app.route('play/<int:num>/<color>')
def seven_(num, color):
    return render_template("index.html", num=num)


if __name__ == "__main__":
    app.run(debug=True)
