#!/usr/bin/env python
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
import cgi
import pymongo
from pymongo import MongoClient

log_err = open("login_error.php","r")


#Get the Username and password and check with database:
print("Content-type: text/html \n")
#Create MongoClient:
cli = MongoClient()
db = cli.JobRecommender
userInfo = db.userInfo

#Create the form object
formData = cgi.FieldStorage()

username = formData.getvalue("username")
password = formData.getvalue("pwd")


resultSet = userInfo.find_one({"username":username},{"username":1,"password":1})

#Check if its an empty set and if so redirect to error page
if not(resultSet):
	print(log_err.read())
else:
	if (username == resultSet["username"] and password == resultSet["password"]):
		print("<html><head><title>Success!</title></head><body>Success</body></html>")
	
	else:
		print(log_err.read())
