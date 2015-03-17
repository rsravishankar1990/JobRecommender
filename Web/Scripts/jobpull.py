import urllib2
import json
import pandas
from bs4 import BeautifulSoup
import numpy as np

def extractJobs(title):
	#Split the title into its component words to search for the jobs
	titleList = title.split(" ")
	
	#build the query string based on the title
	i=1
	queryString = '"'
	while(i<=len(titleList)):
		queryString = queryString + str(titleList[i-1])
		if(i==len(titleList)):
			queryString=queryString + '"'
		else:
			queryString = queryString + '+'
		i=i+1
	
	
	#Use the query string to get all jobs posted for this title
	pub_key = str(7205198081853451)
	fmt = "json"
	sort="date"
	jt="fulltime"
	limit=str(25)
	fromage=str(1)
	api_base = "http://api.indeed.com/ads/apisearch?publisher="
	version = str(2)
	highlight=str(0)
	api_url = api_base+pub_key+"&q="+queryString+"&jt="+jt+"&sort="+sort+"&limit="+limit+"&highlight="+highlight+"&fromage="+fromage+"&v="+version+"&format="+fmt
	
	#Get the number of jobs in the title
	api_request = urllib2.urlopen(api_url)
	api_result = json.loads(api_request.read())
	jobs = api_result['results']
	totalResults = int(api_result['totalResults'])
	#
	
	iterations = min(int(totalResults/25),2)
	loopIter = 1
	while(loopIter <= iterations):
		url=api_base+pub_key+"&q="+queryString+"&jt="+jt+"&sort="+sort+"&start="+str((loopIter)*25)+"&limit="+limit+"&highlight="+highlight+"&fromage="+fromage+"&v="+version+"&format="+fmt
		api_request = urllib2.urlopen(url)
		api_result = json.loads(api_request.read())
		result = api_result['results']
		jobs.extend(result)
		loopIter = loopIter + 1
	#
	
	
	return jobs
	
def extractJobDesc(url):
	soup = None
	while not soup:
		try:
			request = urllib2.urlopen(url)
			soup=BeautifulSoup(request.read())
		except:
			pass
	content = soup.find("span",class_="summary").text.encode("utf-8") 
	return content
		
		
def wordCount(blob):
	blob = blob.upper()
	charRemove = ['\n','\t',',','.',';',':','/','?','-']
	wordRemove = ['THE','MUST','FROM','FOR','SHOULD','NOT','YOUR','ANOTHER','ONE','THAN','USE','BY','OF','AT','AS','YOU','IS','ON','IN','WAS','WHERE','THERE','THAT','WITH','OR','WHAT','WHICH','IT','A','AND','WILL','WOULD','CAN','COULD','WHILE','THEIR','NOT']
	for char in charRemove:
		blob=blob.replace(char," ")
	words = blob.split(" ")
	words = list(set(words))
	wdCount = {}
	for word in words:
		wdCount.setdefault(word,blob.count(word))
	for word in wordRemove:
		if(wdCount.has_key(word)):
			wdCount.pop(word)
	return wdCount

def wordCountList(blob,words):
	blob = blob.upper()
	charRemove = ['\n','\t',',','.',';',':','/','?','-','|']
	wordRemove = ['THE','MUST','FROM','FOR','SHOULD','NOT','YOUR','ANOTHER','ONE','THAN','USE','BY','OF','AT','AS','YOU','IS','ON','IN','WAS','WHERE','THERE','THAT','WITH','OR','WHAT','WHICH','IT','A','AND','WILL','WOULD','CAN','COULD','WHILE','THEIR','NOT']
	for char in charRemove:
		blob=blob.replace(char," ")
	totalWords = len(blob.split(" "))
	wdCount = {}
	for word in words:
		if word == "":
			continue
		else:
			temp = " " +word.upper() +" "
			count = blob.count(temp)
			perc = float(count)/float(totalWords)
			perc = perc*100
			wdCount.setdefault(word.upper(),perc)
	
	return wdCount
	
def cosSimilarity(lista,listb):
	c=[]
	d=[]
	for num in lista:
		num = float(num)-float(np.mean(lista))
		c.append(num)
	for num in listb:
		num=float(num)-float(np.mean(listb))
		d.append(num)
	corr = np.dot(c,d)/(np.linalg.norm(np.array(c))*np.linalg.norm(np.array(d)))
	return corr
	
def jacSimilarity(lista,listb):
	c=[]
	d=[]
	for num in lista:
		if num>0:
			c.append(1)
		else:
			c.append(0)
	for num in listb:
		if num>0:
			d.append(1)
		else:
			d.append(0)
	
	total = sum(listb)
	equal = 0
	i = 0
	while i< len(lista):
		if (c[i] == d[i] and d[i]==1):
			equal = equal + 1
		i=i+1
		
	if total > 0:
		corr = float(equal)/float(total)
	else:
		corr = 1
	return corr


def jacNorm(lista,listb):
	c=[]
	d=[]
	for num in lista:
		if num>0:
			c.append(1)
		else:
			c.append(0)
	for num in listb:
		if num>0:
			d.append(1)
		else:
			d.append(0)
	
	total = 0
	j=0
	while(j<len(lista)):
		if(c[j] == 1 or d[j]==1):
			total = total+1
		j=j+1
		
		
	equal = 0
	i = 0
	while i< len(lista):
		if (c[i] == d[i] and d[i]==1):
			equal = equal + 1
		i=i+1
		
	if total > 0:
		corr = float(equal)/float(total)
	else:
		corr = 1
	return corr
