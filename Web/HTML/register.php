<!DOCTYPE HTML>

<!-- 	Job Recommender 
		Document Purpose:		Registration Page
		Document Author:		RaSh
		Document Update date:	03/08/2015 -->
		
<html>
<head >
	<Title>RaSh Job Recommender</Title>
	<meta name="keywords" content="Jobs, Recommendation, Linkedin, Content-based Recommendation">
	<meta name="description" content="Job Recommendations based on your Linkedin Profile">
	<meta charset = "UTF-8">
	<meta name="author" content="RaSh">
	<script src= "register.js"></script>
	<link rel="stylesheet" type="text/css" href="HomeStyle.css"> 
	<link rel="stylesheet" type="text/css" href="register.css">
</head>

<body>
	<div id="header">
		<h1 id="page-header">What is the Best job for You?</h1>
	</div>
	<div id="nav">
		<ul>
			<li id="nav-menu"><a href="HomePage.php">Home</a></li>
			<li id="nav-menu"><a href="about.html">About</a></li>
			<li id="nav-menu"><a href="http://www.github.com/rsravishankar1990">Git-repo</a></li>
			<li id="nav-menu"><a href="register.php">Register</a></li>
		</ul>
	</div>
	<!--<br/><br/>-->
	<div id="register-container">
		<div id="register-form">
			<p class="sub-header">Enter your info manually or use Linkedin to share your info</p>
		<form name="register-form" action="regconfirm.php" onsubmit="return registerValidate()" method="POST">
			<table id="register-table">
				<tr>
					<td class="form-data-title">Username</td>
					<td class="form-data">
						<input autocomplete="off" name="user" required type= "text" placeholder="Enter your e-mail">
						<span class="regerror" id="user-error"></span>
					</td>
					
			<!--<br/><br/>-->
				</tr>
				<tr>
					<td class="form-data-title">Enter a password</td>
					<td class="form-data">
						<input required name="pwd-enter" type= "password" placeholder="Password">
						<span class="regerror" id="pwd-error">
					</td>
			<!--<br/><br/>-->
				</tr>
								<tr>
					<td class="form-data-title">Confirm Password</td>
					<td class="form-data">
						<input required name="pwd-confirm" type= "password" placeholder="Type again">
					</td>
			<!--<br/><br/>-->
				</tr>
				
				<tr>
					<td class="form-data-title" >Upload resume</td>
					<td class="form-data" >
						<input autocomplete="off" name="resume-file" type="file" value="Browse"><br/>
						<span class="important">*valid types are .docx,.txt,.pdf</span>
						</textarea>
					</td>
				</tr>
				<tr>
					<td style="text-align:center;font-family:Arial">or</td>
					<td></td>
				</tr>
				<tr>
					<td class="form-data-title" >Paste resume</td>
					<td class="form-data" >
						<textarea autocomplete="off" name="resume" placeholder="Paste your resume here" rows="10" cols="50">
						</textarea>
					</td>
					<tr>
					<td class="form-data-title" >Positions you like?</td>
					<td id="position-adder" class="form-data" >
						<input autocomplete="off" required class="job-position" type="text" name="position1" placeholder="Position name">
					</td>	
				</tr>
				<tr>
					<td class="form-data-title"></td>
					<td class="form-data"><button onclick="return addPosition()">Add another</button></td>
				</tr>
				<tr>
					<td class="form-data-title">
					</td>
					<td class="form-data">
						<input type="submit" value="Register">
					</td>
				</tr>
			</table>
		</div>
		</form>
	
	
	
	</div>
	
</body>
</html>
