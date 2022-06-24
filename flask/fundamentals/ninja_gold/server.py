from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)    
app.secret_key = 'bananahammock'


@app.route('/')          
def hello_world():
    if 'gold' in session:
        return render_template("index.html")  
    else:
        session['gold'] = 0
        session['comment'] = []
    return render_template("index.html")  

@app.route('/process_money', methods=["POST"])
def process_money():
    session['gold'] += int(request.form['building'])
    session['name'] = request.form['name']
    session['amount'] = request.form['building']
    comment()
    print(request.form)
    print(session['gold'])
    return redirect('/')

@app.route('/reset_session')
def reset_game():
    session.pop('gold')
    session.pop('comment')
    return redirect('/')


def comment():
    if int(session['amount']) < 0:
        session['comment'].append(f" { session['name'] } took { session['amount'] } gold from you! {datetime.datetime.now()}")
    else:
        session['comment'].append(f" You earned { session['amount'] } gold from { session['name'] }! {datetime.datetime.now()}")
    print(session['comment'])

if __name__=="__main__":  
    app.run(debug=True) 