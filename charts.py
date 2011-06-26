"""A quick demo to show how to dynamically generate a webpage using the Google
Charts API with the Flask web framework.

Run charts.py and then connect to http://localhost:5000/charts/ in your
browser."""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/chart/')
def hello():
	# The data can come from anywhere you can read it; for instance, a SQL
	# query or a file on the filesystem created by another script.
	# This example expects two values per row; for more complicated examples,
	# refer to the Google Charts gallery.
	data = [('Sunday', 48), ('Monday', 27), ('Tuesday', 32), ('Wednesday', 42),
			('Thursday', 38), ('Friday', 45), ('Saturday', 52)]
	return render_template('template.html', data=data)

if __name__ == '__main__':
	# Automatically detect changes to charts.py and reload the server as
	# necessary.
	app.run(debug=True)
