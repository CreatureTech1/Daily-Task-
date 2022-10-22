<html>
<head><title> Check the number is Prime or not></title>
<form method="post">  
Enter a Number: <input type="text" name="check"><br><br>  
<input type="submit" name="submit" value="Submit">  
</form>  
<?php  
if($_POST)  
{  
    $check=$_POST['check'];  
    for ($i = 2; $i <= $check-1; $i++) {  
      if ($check % $i == 0) {  
      $value= True;  
      }  
}  
if (isset($value) && $value) {  
     echo 'The Number '. $check . ' is not prime';  
}  else {  
   echo 'The Number '. $check . ' is prime';  
   }   
}  
?>  
</head>
</html>