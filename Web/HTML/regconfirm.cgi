#!/usr/bin/env python
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
import cgi
import pymongo
from pymongo import MongoClient

#Get the template of the output files: Registered and error
errorFile = open("register_error.php","r")
successFile = open("register_conf.php","r")
errorStr = errorFile.read()
successStr = successFile.read()



client = MongoClient('localhost',27017)

#Get the user Database connection for the same:
db = client.JobRecommender
userInfo = db.userInfo

#Get the Form data to be registered 
formData = cgi.FieldStorage()
username = formData.getvalue('user')
password = formData.getvalue('pwd-enter')
firstName = formData.getvalue('fname')
lastName = formData.getvalue('lname')
posnum = int(formData.getvalue('position-num'))
positions = list()
for i in range(1,posnum+1):
	temp = "position" + str(i)
	positions.append(formData.getvalue(temp))
resume = formData.getvalue('resume')

#Validate if the obtained username already exists in the system
result = userInfo.find_one({'username':username})
if not(result):
	#Update the database with the values
	userInfo.insert({	'username':username,
							'password':password,
							'firstName':firstName,
							'lastName':lastName,
							'resume':resume,
							'positions':positions	})
	print(successStr)
#If the username is already present, then dont update the values in the db
else:
	print(errorStr)





