from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = "penis"

lead = {}

@app.route('/')
def index(): 
    session['num'] = random.randint(0,100)
    session['attempt'] = 0
    print(session['num'])
    return render_template("index.html")


@app.route('/numcheck', methods=['POST'])
def numcheck():
    session['attempt'] += 1
    session['guess']=request.form['guess']
    if session['attempt'] == 6:
        return redirect('/loser')
    if int(session['guess']) == int(session['num']):
        return redirect('/winnerb')
    else:
        return redirect('/nextguess')

@app.route('/nextguess')
def nextguess():

    if int(session['guess']) < int(session['num']):
        answer = "Sorry, too low!\n Guess again!"
        color = "red"
        return render_template("nextguess.html", answer = answer, color= color)
    if int(session['guess']) > int(session['num']):
        answer = "Sorry, too high!\n Guess again!"
        color = "blue"
        return render_template('nextguess.html', answer=answer, color=color)


@app.route('/winnerb')
def winnerb():
    return render_template('winnerb.html')

@app.route('/addwin',methods=['POST'])
def addwin():
    value = session['attempt']
    lead[request.form['win']]= value
    return redirect('/winnernb')

@app.route('/winnernb')
def winnernb():
    l1={}
    l2={}
    l3={}
    l4={}
    l5={}
    for x in lead:
        if lead[x] == 1:
            l1[x] = lead[x]
        elif lead[x] == 2:
            l2[x] = lead[x]
        elif lead[x] == 3:
            l3[x] = lead[x]
        elif lead[x] == 4:
            l4[x]= lead[x]
        else:
            l5[x] = lead[x]
    return render_template('winnernb.html', l1 =l1, l2=l2, l3=l3, l4=l4, l5=l5)

@app.route('/restart')
def restart():
    session.pop('num')
    session.pop('guess')
    return redirect('/')

@app.route('/loser')
def loser():
    return render_template('loser.html')


if __name__=="__main__":
    app.run(debug=True)