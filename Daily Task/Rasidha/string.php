<?php
$string = 'Hello Everyone';
echo "Entered String: " . $string . "<br />"; 
$str_len = strlen($string);
echo "Reversed String: "; 
for ( $x = $str_len - 1; $x >=0; $x-- )
{
  echo $string[$x];
}
?>