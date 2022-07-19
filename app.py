# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import *
import os
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods = ["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def welcome():
	return render_template('welcome.html')

@app.route('/Level_1', methods = ["GET", "POST"])
def Level_1():
	if request.method == 'POST':
		flag_value1= request.form.get("flag")
		if flag_value1 == 'OSINT.ctf{hawaii}':
			flash("Boom !! You got the flag . Solve next level")
			return redirect(url_for('Level_2'))
		if flag_value1 and flag_value1 != 'OSINT.ctf{hawaii}':
			error = "Wrong flag"
			flash(error)

	return render_template('Level_1.html')

@app.route('/Level_2', methods = ["GET", "POST"])
def Level_2():
	if request.method == 'POST':
		flag_value2 = request.form.get("flag2")
		if flag_value2 == 'OSINT.ctf{14.4.31.3}':
			flash("Boom !! You got the flag . Solve next level")
			return redirect(url_for('Level_3'))
		if flag_value2 and flag_value2 != 'OSINT.ctf{14.4.31.3}':
			error = "Wrong flag"
			flash(error)
	return render_template('Level_2.html')


@app.route('/Level_3', methods = ["GET", "POST"])
def Level_3():
	if request.method == 'POST':
		flag_value3 = request.form.get("flag3")
		if flag_value3 == 'OSINT.ctf{Ryuk}':
			flash("Boom !! You got the flag . Solve next level")
			return redirect(url_for('final'))
		if flag_value3 and flag_value3 != 'OSINT.ctf{Ryu}':
			error = "Wrong flag"
			flash(error)
	return render_template('Level_3.html')


@app.route('/final', methods = ["GET", "POST"])
def final():
	if request.method == 'POST':
		flag_value4 = request.form.get("flag4")
		if flag_value4 == 'OSINT.ctf{national.museum.ireland}':
			flash("Boom !! You got the flag . Solve next level")
			return redirect(url_for('success'))
		if flag_value4 and flag_value4 != 'OSINT.ctf{national.museum.ireland}':
			error = "Wrong flag"
			flash(error)
	return render_template('final.html')

@app.route('/success', methods = ["GET", "POST"])
def success():
	if request.method == 'POST':
		pass
	return render_template('success.html')

# main driver function
if __name__ == '__main__':
	app.config['SECRET_KEY']='osintctf'
	port = int(os.environ.get('PORT', 8080))
	waitress.serve(app, port=port)
	app.run(debug=True)
