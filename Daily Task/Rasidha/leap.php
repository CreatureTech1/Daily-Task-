<?php
function isLeap($year)
{
return (date('L',mktime(0,0,0,1,1,$year))==1);
}
for($year=1991;$year<2016;$year++)
{
if(isleap($year))
{
echo"$year: Leap Year <br/>\n";
}
else
{
echo"$year: Not leap year <br/>\n";
}
}
?>
