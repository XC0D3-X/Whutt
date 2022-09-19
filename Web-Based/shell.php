<title>Supp Bruh?</title>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
    <link rel="icon" type="image/png" href="https://mambang-edge.dragonforce.io/data/assets/logo/32x32-01.png" sizes="32x32" />
    <link rel="apple-touch-icon" href="https://mambang-edge.dragonforce.io/data/assets/logo/maskable_icon_x192.png">

    <meta name="description" content="Online Exploiter [DFM]" />
    <meta name="keywords" content="Online Exploiter [DFM]" />
    <meta name="author" content="- Pari Malam -" />
    <meta name='rating' content='general' />
    <meta name='geo.country' content='id' />
    <meta name='geo.placename' content='Malaysia' />
    <meta name='robots' content='all'/>
    <meta name='robots' content='index, follow' />
    <meta name='robots schedule' content='auto'/>
    <meta name='revisit-after' content='1 days' />
    <meta name='googlebot' content='index,follow'/>
    <meta name='distribution' content='global'/>

    <meta content='IE=edge,chrome=1' http-equiv='X-UA-Compatible'/>
<style type="text/css">
html {
    text-align: center;
}
a {
    text-decoration: none;
    color: lime;
}
</style>
</head>
<body bgcolor="black">
<center><img src='../assets/img/dfm.png' width='150' height='150'/></center>
<?php
 
$keyword = array("Password","password","Submit","submit","WSO","GIF89a","IndoXploit","Shell","shell","wso","Upload","Priv8","priv8","tool","Tool","tools","Tools","Linux","dfs","dfs.php","oya","oya.php","SMP Tue","SMP Wed","SMP Sat","SMP Mon","SMP Sun","SMP Thu","SMP Fri","Safe mode","exploit-db.com","phpinfo","Php Info"," UTC","Disable Function"); // Edit Here
 
if(!empty($_POST['check'])) {
    $list = $_POST['list'];
    $shell = explode(PHP_EOL, $list);
    echo '<pre>';
    foreach($shell as $shellchk) {
        $url = trim($shellchk);
        $keyx = '/(' .implode('|', $keyword) .')/';
        $ch = curl_init($url);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
        curl_setopt($ch,CURLOPT_TIMEOUT,10);
        $shellcurl = curl_exec($ch);
        $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        if($httpcode == '200' && preg_match_all("$keyx", $shellcurl))  {
            echo "[HIDUP!] $url\n\n"; 
        }
        else {
            echo "<font color='red'>[MAMPUIH!] $url</font>\n\n";
        }
    }
    echo '</pre>';
}
function eof() {$off = chr(90).chr(101).chr(114).chr(111).chr(66).chr(121).chr(116).chr(101);eval(chr(101).chr(99).chr(104).chr(111)." $off.'.".chr(73).chr(68)."';");}
echo "<html>\n";
echo "<head>\n";
echo "<title>Webshell Mass Checker</title>";
echo '<style type="text/css">body{color:#0aa000;background:#111111;font-family:\'Courier\'}textarea{color:#0aa000;background:transparent;border-color:#0aa000;padding:5px;}input{color:#200089;background:#0aa000;margin-top:10px;font-size:20px;border:2px double #0aa000;padding:2px;padding-left:150px;padding-right:150px;font-family:Arial}</style>';
echo "\n</head>";
echo "<body>\n";
echo "<center>";
if(empty($_POST['check'])) {
    echo '<font color="yellow" face="Courier New" size="5">"Webshell Mass Checker"</font><br>';
    echo '<font color="red" face="Courier New" size="4">"Check Status Content [200]"</font><br>';
    echo '<font color="white" face="Courier New" size="3">"Sitelist With [HTTP/HTTPS]"</font><br><br>';
    echo '<form method="post">'."\n";
    echo '<textarea name="list" placeholder="https://victim.com/shell.php" style="width:700px;height:250px;">'."\n";
    echo "</textarea><br><br>\n";
    echo '<input style="border: 1px solid #008000; color: #bb0000; background: transparent; margin: 5px; width: 350px; height: 25px;" type="submit" name="check" value="w00t!"/>'."\n";
    echo "</form>\n";
} 
echo "</center>\n";
echo "</body>\n";
echo "</html>";
 
?>