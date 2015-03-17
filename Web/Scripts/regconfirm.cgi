#!/usr/bin/env python
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
import cgi
import pymongo
import jobpull
from pymongo import MongoClient
import numpy as np

#Get the template of the output files: Registered and error
errorFile = open("register_error.php","r")
successFile = open("register_conf.php","r")
errorStr = errorFile.read()
successStr = successFile.read()
print("Content-type:text/html")


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

profile_blob = formData.getvalue('profile')
blob = formData.getvalue('blob')

#Get the fields from the profile - blob
profile_split = profile_blob.split(';')
profile_dict = {'username':username,'blob':blob}
for text in profile_split:
	split=text.split('::')
	if(len(split)==2):
		profile_dict.setdefault(split[0],split[1])





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
	profile = db.profile
	profile.insert(profile_dict)
	print(successStr)
	jobdb = db.jobBase
	
	#Job Recommendation Phase
	#Prepare the user profile and get jobs
	#Prepare the education field
	edu = profile_dict["degree"].split("|")
	qualification = {'PhD':0,'Master':0,'Bachelor':0}
	for degree in edu:
		if (degree.count("Master") >= 1 or degree.count("MS") >= 1 or degree.count("ME") >= 1 or degree.count("M.E") >= 1 or degree.count("M.S") >=1 ):
			qualification['Master'] = 1
		if (degree.count("Bachelor") >= 1 or degree.count("BS") >= 1 or degree.count("B.S") >=1 ) or degree.count("B.E") >= 1 or degree.count("B.A") >= 1 or degree.count("BA") >=1:
			qualification['Bachelor'] = 1
		if (degree.count("Doctor") >=1 or degree.count("PhD") >= 1 or degree.count("Ph.D") >= 1):
			qualification['PhD'] = 1
	
	#Count the number of words in the blob:
	skills = profile_dict["skills"].split("|")
	userProfile = jobpull.wordCountList(blob,skills)
	userEduc = [qualification['PhD'],qualification['Master'],qualification['Bachelor']]
	userWords = userProfile.keys()

	#Get the positions for which user wants jobs and update jobs database
	for position in positions:
		#Extract job info as a dictionary
		jobDict = jobpull.extractJobs(position)
		#For each job in jobdict extract the description
		jobIter = 0
		for job in jobDict:
			content = jobpull.extractJobDesc(job['url'])
			jqualification = {'PhD':0,'Master':0,'Bachelor':0}
			job.setdefault("desc",content)
			if (content.count("Master") >= 1 or content.count("MS") >= 1 or content.count("ME") >= 1 or content.count("M.E") >= 1 or content.count("M.S") >=1 ):
				jqualification['Master'] = 1
			if (content.count("Bachelor") >= 1 or content.count("BS") >= 1 or content.count("B.S") >=1 ) or content.count("B.E") >= 1 or content.count("B.A") >= 1 or content.count("BA") >=1:
				jqualification['Bachelor'] = 1
			if (content.count("Doctor") >=1 or content.count("PhD") >= 1 or content.count("Ph.D") >= 1):
				jqualification['PhD'] = 1
			jobEduc = [jqualification['PhD'],jqualification['Master'],jqualification['Bachelor']]
			
			#Calculate the pearson correlation in education
			corr = jobpull.jacSimilarity(userEduc,jobEduc)
			corr = corr*100
			job.setdefault("educ_similarity",corr)
			
			#Get the weightage of words in the job description
			jobProfile = jobpull.wordCountList(content,skills)
			userWeight=[]
			jobWeight = []
			for word in userWords:
				temp = userProfile[word]
				userWeight.append(temp)
				temp = jobProfile[word]
				jobWeight.append(temp)
				
			corr = jobpull.cosSimilarity(userWeight,jobWeight)
			corr=corr*100
			corr2 = jobpull.jacNorm(userWeight,jobWeight)
			corr2 = corr2*100
			job.setdefault("profile_similarity",corr)
			job.setdefault("profile_jac",corr2)
			job.setdefault("username",username)
			jobentry = {'username':username,
						'position':position,
						'jobtitle':job['jobtitle'],
						'profile_similarity':job['profile_similarity'],
						'educ_similarity':job['educ_similarity'],
						'company':job['company'],
						'location':job['formattedLocation'],
						'link':job['url'],
						'profile_jac':job['profile_jac']					
								}
			jobdb.insert(jobentry)
			
	
	
	
#If the username is already present, then dont update the values in the db
else:
	print(errorStr)





