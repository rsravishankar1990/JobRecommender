<!DOCTYPE HTML>

<!-- 	Job Recommender 
		Document Purpose:		Design and layout of the home page
		Document Author:		RaSh
		Document Update date:	03/04/2015 -->
		
<html>
<head >
	<Title>RaSh Job Recommender</Title>
	<meta name="keywords" content="Jobs, Recommendation, Linkedin, Content-based Recommendation">
	<meta name="description" content="Job Recommendations based on your Linkedin Profile">
	<meta charset = "UTF-8">
	<meta name="author" content="RaSh">
	<script src= "Validate.js"></script>
	<link rel="stylesheet" type="text/css" href="HomeStyle.css"> 
</head>

<body onload="getCookie()">
	<div id="header">
		<h1 id="page-header">What is the Best job for You?</h1>
	</div>
	<div id="nav">
		<ul>
			<li id="nav-menu"><a id="nav" href="HomePage.php">Home</a></li>
			<li id="nav-menu"><a id="nav" href="about.html">About</a></li>
			<li id="nav-menu"><a id="nav" href="http://www.github.com/rsravishankar1990">Git-repo</a></li>
			<li id="nav-menu"><a id="nav" href="register.php">Register</a></li>
		</ul>
	</div>
	<!--<br/><br/>-->
	<div id="container">
	
	<div id="login" style="width:450px;margin-right:50px">
		<div style="padding-top:50px;padding-right:10px;padding-bottom:50px;padding-left:50px;width:200px;float:left">
		<p style="border-radius:20px;background-color:#938989;text-align:center;color:white;padding:4px">Returning User? Sign in</p>
		<form name= "login-form" action="login.cgi" onsubmit="return validate()" method="POST">
			<div>
			<input id="username" required style="font-family:Arial;padding-bottom:3px;padding-top:3px" type="text" autocomplete="off" name="username"  placeholder="Your E-mail">
			
			</div>
			<div>
			<input required style="font-family:Arial;padding-bottom:3px;padding-top:3px" type="password" name="pwd" id="pwd" placeholder="Password"><br/>
			</div><br/>
			<button style="color:white;background-color:#938989;float:right" type="submit">Log in</button>
			<div id="rem-me"><input id="remem-me" style="position:relative;top:2.5px" type="checkbox" name="remember" value="rememberme" ><p style="display:inline;font-size:0.85em;padding-right:10px;padding-left:10px">Remember me</p></div>
			
		</form>
		</div>
		<div style="padding-top:105px"><p style="display:inline" class="error" id="user-err"></p></div>
	</div>
	
		<div id="welcome">
		<h3 style="font-family:Arial;">Welcome to the Job Recommender</h3>
		<p id="wel-mess" style="font-size:0.9em">
			A naive Recommendation engine which uses your linkedin profile
			information to find best matching newly posted jobs on linkedin. The approach and the technologies used to implement 
			this are provided in the git hub repo.
		</p>
	</div>
	</div>
	
	<div id="footer" style="text-align:center;font-size:0.6em;border-style:solid;width:700px;border-color:white;position:fixed;left:600px;bottom:10px">
		Last updated on March 4th 2015
	</div>
</body>
</html>
