from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Daniel","Yonathan","Dana", "mother", "father"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
	  	user = request.form['username']
	  	pas = request.form['password']
	  	if user == username and pas == password:
	  		return redirect(url_for('home'))
	  	else:
	  			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', facebook_friends = facebook_friends)
@app.route('/friends_exists/<string: name>', methods = ['GET', 'POST'])
def friends_exists(friends_exists):
	return render_template('friends_exists.html', facebook_friends = friends_exists)

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)