<?php
$authKey = "YOUR_AUTH_KEY";
$phoneNumber = $_POST['phoneno'];
$senderId = "YOUR_SENDER_ID";
$message = urlencode($_POST['smstext']);
$fields = array(
    "sender_id" => $senderId,
    "message" => $message,
    "language" => "english",
    "route" => "p",
    "numbers" => $phoneNumber,
);

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "YOUR_GATEWAY_URL",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_SSL_VERIFYHOST => 0,
  CURLOPT_SSL_VERIFYPEER => 0,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode($fields),
  CURLOPT_HTTPHEADER => array(
    "authorization: ".$authKey,
    "accept: */*",
    "cache-control: no-cache",
    "content-type: application/json"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
?>