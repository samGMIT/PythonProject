# Author: Abuchie Kamara
# Date: October 24th, 2016

# Originally adapted from:
#   http://flask.pocoo.org/

from flask import Flask, request
# MySQLdb.exe needed to run app
# https://sourceforge.net/projects/mysql-python/files/latest/download?source=files
import pymysql

app = Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/submit", methods=['POST'])
def order():
	# Get the form values out of the post request
	name = request.form.get('name')
	text = request.form.get('text')
	
	# Connection variable used to put stuff into DB
	# adapted from http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
	conn = pymysql.connect(host="localhost",
							user="root",
							passwd="",
							db="datarep",
							autocommit=True)
	# Cursor object used to execute queries					
	cur = conn.cursor()
	
	# Try to add order to DB and catch exceptions
	cur.execute("INSERT INTO blogposts VALUES(NULL, '" + name + "', '" + text + "')")
	
	# Close the cursor and collection to stop any memory leaks
	cur.close()
	conn.close()
	
	# Default return for method
	return "Success"
	
@app.route("/getPosts", methods=['GET'])
def booking():
	# Get the form values out of the post request
	
	# Connection variable used to put stuff into DB
	# adapted from http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
	conn = pymysql.connect(host="localhost",
							user="root",
							passwd="",
							db="datarep",
							autocommit=True)
	# Cursor object used to execute queries					
	cur = conn.cursor()
	
	# Try to add order to DB and catch exceptions
	cur.execute("Select * from blogposts")
	
	# Close the cursor and collection to stop any memory leaks
	cur.close()
	conn.close()
	
	# Default return for method
	return "success"

@app.route("/about", methods=['GET'])
def about():
	return app.send_static_file('about.html')

@app.route("/favorites", methods=['GET'])
def favorites():
	return app.send_static_file('favorites.html')

@app.route("/contact", methods=['GET'])
def contact():
	return app.send_static_file('contact.html')

if __name__ == "__main__":
    app.run(port=8080) # Run project on localhost:8080