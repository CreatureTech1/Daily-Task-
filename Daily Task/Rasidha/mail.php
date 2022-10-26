<?php
$to = "somebody@example.com, somebodyelse@example.com";
$subject = "Email";
$message = "
<html>
<head>
<title>Email</title>
</head>
<body>
<table>
<tr>
<th>Firstname</th>
<th>Lastname</th>
</tr>
<tr>
<td>John</td>
<td>Doe</td>
</tr>
</table>
</body>
</html>
";
$headers = "MIME-Version: 10.4.13" . "\r\n";
$headers = "Content-type:text/html;charset=UTF-8" . "\r\n";
$headers = 'From: <webmaster@example.com>' . "\r\n";
$headers = 'Cc: myboss@example.com' . "\r\n";
mail($to,$subject,$message,$headers);
?>