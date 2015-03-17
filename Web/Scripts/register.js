"use strict"
/*
 *Script 		:		register.js
 * Author		:		RaSh
 * Purpose		:		Validate credentials on registration 
 * Last update	:		March 8, 2015
 */


//Handling Linkedin API
function printEnter() {
	console.log("Entered the linkedin load");
	IN.Event.on(IN, "auth", printAuth);
}

function printAuth() {
	console.log("My name is Ravishankar");
	IN.API.Raw("/people/~:(id,recommendations-received,first-name,location,last-name,interests,honors-awards,headline,publications,patents,skills,certifications,educations,courses,job-bookmarks,public-profile-url,specialties,industry,email-address,summary,picture-url,positions)").result(onSuccess).error(onError);
}
function onSuccess(data) {
	
	//Build Resume from Linkedin Profile
	
	var profile_text = "";
	
	if(data.summary) {
	var resume_text = "";
	resume_text = resume_text+ "Summary:\n"+data.summary+"\nEducation:\n";
}
	if(data.educations) {
	var edu = data.educations.values;
	for (var i = 0;i<data.educations.values.length;i++) {
		var edobj = edu[i];
		resume_text = resume_text + edobj.degree + "\t" +edobj.fieldOfStudy+"\n"+edobj.schoolName+"\n" +edobj.notes+"\n" ;
	}
}
	if(data.positions) {
	resume_text = resume_text + "\n\nPositions:\n";
	var pos = data.positions.values;
	for (i=0;i<data.positions.values.length;i++) {
		var posobj = pos[i];
		resume_text = resume_text + posobj.title + "\n" + posobj.company.name + "\n" + posobj.summary + "\nExperience: \t" + posobj.startDate.month+"-"+posobj.startDate.year+" to "+posobj.endDate.month+"-"+posobj.endDate.year+"\n"; 
	}
}

	if(data.skills) {
	resume_text = resume_text + "\n\nSkills:\n";
	var ski = data.skills.values;
	for(i=0;i<data.skills.values.length;i++) {
		var skiobj = ski[i];
		resume_text = resume_text + skiobj.skill.name + "\n";
	}
}

	if(data.certifications) {
	resume_text = resume_text + "\n\nCertifications:\n";
	var cert = data.certifications.values;
	for(i=0;i<data.certifications.values.length;i++) {
		var certobj = cert[i];
		resume_text = resume_text + certobj.name + "\n";
	}
}
	
	
	//Fill the registration field values
	
	document.forms["register-form"]["user"].value = data.emailAddress;
	document.forms["register-form"]["fname"].value = data.firstName;
	document.forms["register-form"]["lname"].value = data.lastName;
	document.forms["register-form"]["resume-paste"].value = resume_text;



	//Create User profile and paste in the profile text area
	if(data.location) {
	profile_text = profile_text + "location::" + data.location.name + ";";
}
	if(data.pictureUrl) {
	profile_text = profile_text + "profilepic::"+data.pictureUrl+";" ;
}


	//Calculate the experience
	if(data.positions) {
	var experience = 0;
	for (i=0;i<data.positions.values.length;i++) {
		var pos = data.positions.values[i];
		var diff = (pos.endDate.year - pos.startDate.year)*12 + (pos.endDate.month - pos.startDate.month);
		experience = experience + diff;
	}
	
	experience = parseInt(experience/12);
	profile_text = profile_text + "experience::"+experience+";";
}
	if(data.interests) {
	profile_text = profile_text + "interests::" + data.interests+";";
}

	//Skills for the profile
	if(data.skills) {
	profile_text = profile_text + "skills::";
	for(i=0;i<data.skills.values.length;i++) {
		var skiobj = data.skills.values[i];
		profile_text = profile_text + skiobj.skill.name + "|";
	}
	profile_text = profile_text + ";";
}
	
	//Certifications
	if(data.certifications) {
		profile_text = profile_text + "certifications::";
		for(i=0;i<data.certifications.values.length;i++) {
		var certobj = data.certifications.values[i];
		profile_text = profile_text + certobj.name + "|";
	}
		profile_text = profile_text + ";";
}
	
	
	//Education
	if(data.educations) {
		profile_text = profile_text + "degree::";
		for (var i = 0;i<data.educations.values.length;i++) {
		var edobj = data.educations.values[i];
		profile_text = profile_text + edobj.degree + "|" ;
	}
	
		profile_text = profile_text + ";major::";
	//Major
		for (var i = 0;i<data.educations.values.length;i++) {
		var edobj = data.educations.values[i];
		profile_text = profile_text + edobj.fieldOfStudy + "|" ;
	}
		profile_text = profile_text + ";";
}
		
	
	
	//Create the blob for processing
	var blob = "";
	
	//Profile Summary
	if(data.summary) {
	blob = blob + data.summary;
}
	//interests summary
	if(data.interests) {
	blob = blob + " " + data.interests;
}
	//Positions summary
	if(data.positions) {
		for (i=0;i<data.positions.values.length;i++) {
		var pos = data.positions.values[i];
		blob = blob + " " + pos.summary;
	}
}
	//Publications text
	if(data.publications) {
	for(i=0;i<data.publications.values.length;i++) {
		
		var pub = data.publications.values[i];
		blob = blob + " " + pub.summary;
	}
}
	
	
	//Recommendation text
	if(data.recommendations) {
		for(i=0;i<data.recommendationsReceived.values.length;i++) {
			var rec = data.recommendationsReceived.values[i];
			blob = blob + " " + rec.recommendationText;
		}
			
	}
		//Certifications
	if(data.certifications) {
		blob = blob + "certifications::";
		for(i=0;i<data.certifications.values.length;i++) {
		var certobj = data.certifications.values[i];
		blob = blob + certobj.name + "|";
	}
}
	//Skills for the profile
	if(data.skills) {
	blob = blob + "skills::";
	for(i=0;i<data.skills.values.length;i++) {
		var skiobj = data.skills.values[i];
		blob = blob + skiobj.skill.name + "|";
	}
	
}
	
	console.log(profile_text);
	
	document.getElementById("profile-paste").innerHTML = profile_text;
	document.getElementById("profile-blob").innerHTML = blob;
	
}






function onError(error) {
	console.log(error);
}








//Get the credentials and check if they are proper
//Passwords should match in both rows
//username should be a valid e-mail
function registerValidate() {
			var user = document.forms["register-form"]["user"].value;
			var pwd = document.forms["register-form"]["pwd-enter"].value;
			var pwdconf = document.forms["register-form"]["pwd-confirm"].value;
			console.log(user);
			console.log(pwd);
			console.log(pwdconf);
			var pattern = /[A-Za-z]*[0-9]*@[A-Za-z.]*.(com|in|us|gov|edu)/;
			console.log(pattern.test(user));
			if(!pattern.test(user)) {
				console.log("Does not match the given pattern");
				document.getElementById("user-error").innerHTML = "&nbsp&nbsp&nbsp*Enter valid e-mail&nbsp&nbsp&nbsp";
				return false;
			}
			if(pwd==pwdconf) {
				console.log("Passwords match");
			}else {
				console.log("Passwords dont match at all");
				document.forms["register-form"]["pwd-confirm"].value="";
				document.forms["register-form"]["pwd-enter"].value="";
				document.getElementById("pwd-error").innerHTML="&nbsp&nbsp&nbsp*Passwords dont match&nbsp&nbsp&nbsp";
				return false;
			}	
			return true;
			
		} 
		


//When the Add Another button is clicked it should create another text box for adding a position
//
function addPosition() {
	console.log("Entered the add position function");
	var posnum = document.getElementById("numPosition").value;
	posnum = parseInt(posnum);
	posnum = posnum + 1;
	console.log(posnum);
	document.getElementById("numPosition").value = posnum ;
	var position = document.getElementsByClassName("job-position");
	for(var i= 0;i<position.length;i++) {
		console.log(position[i].value);
	}
	var td = document.getElementById("position-adder");
	var br = document.createElement("br");
	td.appendChild(br);
	
	
	var input = document.createElement("input");
	var name = 	"position"+position.length;
	input.setAttribute("name",name);
	input.setAttribute("type","text");
	input.setAttribute("placeholder","Position Name");
	input.setAttribute("class","job-position");
	input.setAttribute("autocomplete","off");
	
	td.appendChild(input);
	
	return false;
}

function loadFile(event) {
	console.log(event.target.files[0].name);
	console.log(event.target.files[0].lastModifiedDate);
	
	var file = event.target.files[0];
	if(file) {
		console.log("Entered the variable file");
	
	}

}

function getAsText(readFile) {
	  var reader = new FileReader();
  
  // Read file into memory as UTF-16      
  reader.readAsText(readFile, "UTF-16");
  
  // Handle progress, success, and errors
  
  console.log(reader.result);
}



function startRead() {  
  // obtain input element through DOM 
  
  var file = document.getElementById('file').files[0];
  if(file){
    getAsText(file);
  }
}

function getAsText(readFile) {
        
  var reader = new FileReader();
  
  // Read file into memory as UTF-16      
  reader.readAsText(readFile, "utf-16");
  console.log(reader.readyState);
  console.log(reader.result);
  // Handle progress, success, and errors
  reader.onprogress = updateProgress;
  reader.onload = loaded;
  reader.onerror = errorHandler;
}

function updateProgress(evt) {
  if (evt.lengthComputable) {
    // evt.loaded and evt.total are ProgressEvent properties
    var loaded = (evt.loaded / evt.total);
    if (loaded < 1) {
		console.log("Loading not complete");
		console.log(loaded);
      // Increase the prog bar length
      // style.width = (loaded * 200) + "px";
    }
  }
}

function loaded(evt) {  
  // Obtain the read file data    
  var fileString = evt.target.result;
  // Handle UTF-16 file dump
  console.log("Entered loaded");
  console.log(fileString);
  document.getElementById("resume-paste").innerHTML="";
  document.getElementById("resume-paste").innerHTML=fileString;
}

function errorHandler(evt) {
  if(evt.target.error.name == "NotReadableError") {
    console.log("The file could not be read");
  }
}














