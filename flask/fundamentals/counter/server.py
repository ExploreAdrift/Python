from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app. secret_key = "Kablam"


@app.route('/')
def original():
    if 'visit' in session:
        session['visit'] += 1

    else:
        session['visit'] = 1
    return render_template('index.html')


@app.route('/destroy_session')
def refresh():
    session.pop('visit')
    return redirect('/')


@app.route('/counter_session')
def counter():
    session['visit'] += 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
