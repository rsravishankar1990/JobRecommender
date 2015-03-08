"use strict"
/*
 *Script 		:		Validate.js
 * Author		:		RaSh
 * Purpose		:		Validate credentials on homepage 
 * Last update	:		March 7, 2015
 */

//Check to set cookie
function setCookie(user,pwd) {
	console.log("Entered the setCookie part");
	console.log(document.cookie);
	console.log(pwd);
	console.log("Entered Set Cookie");
	
	var cookieText = "username= "+user+";expires=";
	var cookieText2 = "pwd=" +pwd+";expires=";
	console.log(cookieText);
	var d = new Date();
	 d.setTime(d.getTime() + 24*60*60*1000);
	 console.log(d);
	 
	 cookieText = cookieText + d.toGMTString();
	 cookieText2 = cookieText2 + d.toGMTString();
	 console.log(cookieText);
	 console.log(cookieText2);
	 document.cookie = cookieText;
	 document.cookie= cookieText2;
	 console.log("the document cookie is");
	 console.log(document.cookie);
	 console.log("Cookie Set");
	}


//Get the cookie information if available:
function getCookie() {
	console.log("Entered the getCookie");
	console.log(document.cookie);
	var cookie = document.cookie.split(";");
	for (var i = 0; i<cookie.length; i ++) {
		var c = cookie[i];
		while(c.charAt(0)==" ") {c= c.substring(1);}
		if (c.indexOf("username=") == 0) {
			console.log("entered the username section");
			document.getElementById("username").value = c.substring("username=".length, c.length);
			
		}
		if(c.indexOf("pwd=")==0) {
			console.log("entered the password section");
			document.getElementById("pwd").value=c.substring("pwd=".length,c.length);
		}
	}
}
 
 //Check the username-email pattern
 		function validate() {
			var user = document.forms["login-form"]["username"].value;
			var pwd = document.getElementById("pwd").value;
			console.log(user);
			console.log(pwd);
			var pattern = /[A-Za-z]*[0-9]*@[A-Za-z.]*.(com|in|us|gov|edu)/;
			console.log(pattern.test(user));
			if(!pattern.test(user)) {
				document.getElementById("user-err").innerHTML = "&nbsp&nbsp&nbsp*Enter valid e-mail&nbsp&nbsp&nbsp";
			}
			if(pattern.test(user) && document.getElementById("remem-me").checked) {
				setCookie(user,pwd);
			}
			
			return pattern.test(user);
			
		} 
