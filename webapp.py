from flask import Flask, request, render_template, flash
from markupsafe import Markup
from flask import redirect
from flask import session
import os
import time

app = Flask(__name__)
app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  

@app.route("/")
def render_main():
    return render_template('index.html')
@app.route("/page2")
def render_pageTwo():
    session["start_time"] = time.time()
    return render_template('page2.html')
@app.route("/question2",methods=['GET','POST'])
def render_pageThree():
    if "answer1" not in session:
        session["answer1"]=request.form['questionONE']
    return render_template('page3.html')
@app.route("/question3",methods=['GET','POST'])
def render_pageFour():
    if "answer2" not in session:
        session["answer2"]=request.form['questionTWO']
    return render_template('page4.html')
@app.route("/question4",methods=['GET','POST'])
def render_results():
    
    if "answer3" not in session:
        session["answer3"]=request.form['questionTHREE']
    value=return_score()
    session["end_time"] = time.time()
    time_taken = session["end_time"] - session["start_time"]
    return render_template('page5.html', value=value, time_taken=time_taken)
def return_score():
    value=0
    if session["answer1"]=="Aicama Zorba of La-Susa":
        value+=1
    if session["answer2"]=="Sultan Kösen":
        value+=1
    if session["answer3"]=="Joseph Dituri":
        value+=1
    return value
@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect('/') # url_for('renderMain') could be replaced with '/'

    
if __name__ == '__main__':
    app.run(debug=False)
