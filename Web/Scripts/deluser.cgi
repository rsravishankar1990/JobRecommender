#!/usr/bin/env python
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
import cgi
import pymongo
from pymongo import MongoClient


#Get the Username and password and check with database:
print("Content-type: text/html \n")
#Create MongoClient:
cli = MongoClient()
db = cli.JobRecommender
userInfo = db.userInfo
jobdb = db.jobBase
profile = db.profile

formData = cgi.FieldStorage()

username = formData.getvalue('username')

#Delete the documents related to username

userInfo.remove({'username':username})
profile.remove({'username':username})
jobdb.remove({'username':username})

content = open("HomePage.php","r")

print(content.read().encode('utf-8'))

