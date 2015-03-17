<!DOCTYPE HTML>
<html>
<head >
	<Title>Account Registration</Title>
	<meta name="keywords" content="Jobs, Recommendation, Linkedin, Content-based Recommendation">
	<meta name="description" content="Job Recommendations based on your Linkedin Profile">
	<meta charset = "UTF-8">
	<meta name="author" content="RaSh">
</head>
<body>
<?php 
		$cli = new MongoClient();
		$db = $cli->selectDB("JobRecommender");
		$userInfo = $db->selectCollection("userInfo");
		$user = array(
						'username' => 'test@email.com',
						'password' => 'testpass'
						);
		$userInfo->insert($user);
		$result = $userInfo->findOne();
		var_dump ($result);
?>
</body>

</html>
