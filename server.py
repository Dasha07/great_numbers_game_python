from flask import Flask, render_template,request,session
import random
app=Flask(__name__)
app.secret_key='Secret numbers'

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/', methods=['post'])
def greatnumbers():
	user_guess = request.form['guess']
	user_guess = int(user_guess)
	

	if 'random' not in session:
		session['random'] = random.randint(0,101)	
	
	if user_guess>session['random']:
		session['request']="big"
		print session['random']
		print "Too High"

	elif user_guess<session['random']:
		session['request']="low"
		print session['random']
		print "Too Low"

	else:
		session['request']="equel"
		print session['random']
		print "Awesome!"
		session['random']= random.randint(0,101)
	
	return render_template("index.html", guess=request.form['guess'])


app.run(debug=True)
