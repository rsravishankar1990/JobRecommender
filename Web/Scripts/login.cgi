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
		print('<html><head><title>Success!</title><meta charset = "utf-8"></head><body>The best Jobs matching your profile are:<br/>')
		jobdb = db.jobBase
		
		resultSet = jobdb.find({'username':username},{'position':1,'jobtitle':1,'company':1,'link':1,'location':1,'profile_similarity':1,'educ_similarity':1})
		i=0
		for doc in resultSet.sort('profile_similarity',pymongo.DESCENDING):
			if i > 10 or doc['profile_similarity'] < 30:
				break
			else:
				print "Job Title: "+doc['jobtitle']+'<br/>'
				print 'Company: '+doc['company']+'<br/>'
				print 'Education Match:' + str(doc['educ_similarity'])+'% <br/>'
				print 'Profile Match:' + str(doc['profile_similarity'])+'% <br/>'
				print 'Link: <a href="' + doc['link']+'">Link to Apply</a> <br/>'
				print '<br/><br/>'
				print '</br>'
				
			i = i + 1
		
		print('<form action="deluser.cgi" method="POST"><input type="text" name="username" value="'+username.encode('utf-8')+'" style="display:none"><br/><button type="submit">Delete User</button></form></body></html>')
	else:
		print(log_err.read())
