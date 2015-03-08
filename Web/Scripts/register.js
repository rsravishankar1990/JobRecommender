"use strict"
/*
 *Script 		:		register.js
 * Author		:		RaSh
 * Purpose		:		Validate credentials on registration 
 * Last update	:		March 8, 2015
 */


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
				document.getElementById("pwd-error").innerHTML="&nbsp&nbsp&nbsp*Passwords dont match&nbsp&nbsp&nbsp";
				return false;
			}	
			return true;
			
		} 
		


//When the Add Another button is clicked it should create another text box for adding a position
//
function addPosition() {
	console.log("Entered the add position function");
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

	td.appendChild(input);
	
	return false;
}
