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

@app.route("/order", methods=['POST'])
def order():
	# Get the form values out of the post request
	price = request.form.get('price')
	items = request.form.get('items')
	delivery = request.form.get('delivery')
	time = request.form.get('time')
	address = request.form.get('address')
	phoneNr = request.form.get('phoneNr')
	
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
	cur.execute("INSERT INTO orders VALUES(NULL, '" + items + "', '" + price + "', '" + delivery + "', '" + time + "', '" + address + "', '" + phoneNr + "')")
	
	# Close the cursor and collection to stop any memory leaks
	cur.close()
	conn.close()
	
	# Default return for method
	return "success"
	
@app.route("/booking", methods=['POST'])
def booking():
	# Get the form values out of the post request
	numOfPeople = request.form.get('numOfPeople')
	orderDate = request.form.get('orderDate')
	bookedDate = request.form.get('bookedDate')
	phoneNr = request.form.get('phoneNr')
	name = request.form.get('name')
	
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
	cur.execute("INSERT INTO bookings VALUES(NULL, '" + numPeople + "', '" + orderDate + "', '" + bookingDate + "', '" + phoneNr + "', '" + name + "')")
	
	# Close the cursor and collection to stop any memory leaks
	cur.close()
	conn.close()
	
	# Default return for method
	return "success"

if __name__ == "__main__":
    app.run(port=8080) # Run project on localhost:8080