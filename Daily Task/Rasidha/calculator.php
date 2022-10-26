<html>
<head>
<title>calculator program in PHP using the switch case
</title>
</head>
<?php
$FirstNumber = $_POST['FirstNumber'];
$SecondNumber = $_POST['SecondNumber'];
$operator = $_POST['operator'];
$CalculatorResult = '';
if (is_numeric($FirstNumber) && is_numeric($SecondNumber)) {
switch ($operator) {
case "Addition":
$CalculatorResult = $FirstNumber + $SecondNumber;
break;
case "Subtraction":
$CalculatorResult = $FirstNumber - $SecondNumber;
break;
case "Multiplication":
$CalculatorResult = $FirstNumber * $SecondNumber;
break;
case "Division":
$CalculatorResult = $FirstNumber / $SecondNumber;
}
}
?>

<body>
<div id="page-wrap">
<h1>PHP - Simple Calculator Program</h1>
<form action="" method="post" id="quiz-form">
<p>
<input type="number" name="FirstNumber" id="FirstNumber" required="required" value="<?php echo $FirstNumber; ?>" /> <b>First Number</b>
</p>
<p>
<input type="number" name="SecondNumber" id="SecondNumber" required="required" value="<?php echo $SecondNumber; ?>" /> <b>Second Number</b>
</p>
<p>
<input readonly="readonly" name="CalculatorResult" value="<?php echo $CalculatorResult; ?>"> <b>CalculatorResult</b>
</p>
<input type="submit" name="operator" value="Addition" />
<input type="submit" name="operator" value="Subtraction" />
<input type="submit" name="operator" value="Multiplication" />
<input type="submit" name="operator" value="Division" />
</form>
</div>
</body>
</html>