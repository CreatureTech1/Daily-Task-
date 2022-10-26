
<?php
require_once 'Request.php';
$requestModel = new Request();
$ip = $requestModel->getIpAddress();
$isValidIpAddress = $requestModel->isValidIpAddress($ip);
?>
<html>
<head>
<title>Get Geo Location by the IP address</title>

</head>
<body>
<div class="txt-heading">Get Geo Location by the IP address</div>
<?php
if ($isValidIpAddress == "") {
    echo "<div class='error'>Invalid IP address $ip</div>";
} else {
    $geoLocationData = $requestModel->getLocation($ip);
    print "<PRE>";
    print_r($geoLocationData);
    ?>
<div id="location">
<div class="geo-location-detail">

<div class="row">
<div class="form-label">
Country Name: <?php  echo $geoLocationData['country'];?>
</div>
</div>
<div class="row">
<div class="form-label">
Country Code: <?php   echo $geoLocationData['country_code'];?>
</div>
</div>
<div class="row">
<div class="form-label">
Ip Address: <?php  echo $geoLocationData['ip'];?>
</div>
</div>
</div>
</div>
<?php
 }
?>
</body>
</html>