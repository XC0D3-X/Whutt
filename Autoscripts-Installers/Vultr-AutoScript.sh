#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

# Initializing Var
export DEBIAN_FRONTEND=noninteractive
OS=`uname -m`;
MYIP=$(wget -qO- ipv4.icanhazip.com);
MYIP2="s/xxxxxxxxx/$MYIP/g";


# Root Directory
cd

# Disable IPV6
echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
sed -i '$ i\echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6' /etc/rc.local

# Install wget and curl
apt-get update;apt-get -y install wget curl;

# Local Time Manila
ln -fs /usr/share/zoneinfo/Asia/Manila /etc/localtime

# Local Configuration
sed -i 's/AcceptEnv/#AcceptEnv/g' /etc/ssh/sshd_config
service ssh restart

# Update
apt-get update

# Install Essential Packages
apt-get -y install nano iptables dnsutils openvpn screen whois ngrep unzip unrar

echo "clear"                                               >> .bashrc
echo 'echo -e "\e[0m                                    "' >> .bashrc
echo 'echo -e "\e[94m     ______    ______   ______     "' >> .bashrc
echo 'echo -e "\e[94m    /      \  /      \ /      |    "' >> .bashrc
echo 'echo -e "\e[94m   /$$$$$$  |/$$$$$$  |$$$$$$/     "' >> .bashrc
echo 'echo -e "\e[94m   $$ |  $$/ $$ |__$$ |  $$ |      "' >> .bashrc
echo 'echo -e "\e[94m   $$ |      $$    $$ |  $$ |      "' >> .bashrc
echo 'echo -e "\e[94m   $$ |   __ $$$$$$$$ |  $$ |      "' >> .bashrc
echo 'echo -e "\e[94m   $$ \__/  |$$ |  $$ | _$$ |_     "' >> .bashrc
echo 'echo -e "\e[94m   $$    $$/ $$ |  $$ |/ $$   |    "' >> .bashrc
echo 'echo -e "\e[94m    $$$$$$/  $$/   $$/ $$$$$$/     "' >> .bashrc
echo 'echo -e "\e[91m        VPS SCRIPT BY ACAI         "' >> .bashrc
echo 'echo -e "\e[0m"'                                     >> .bashrc
echo 'echo -e "\e[92m    [accounts/options/server]      "' >> .bashrc
echo 'echo -e "\e[0m                                    "' >> .bashrc

# Install WebServer
apt-get -y install nginx

# WebServer Configuration
cd
rm /etc/nginx/sites-enabled/default
rm /etc/nginx/sites-available/default
wget -O /etc/nginx/nginx.conf "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/Nginx/nginx.conf"
mkdir -p /home/vps/public_html
echo "<h1><center>AutoScriptVPS BY ACAI</center></h1>" > /home/vps/public_html/index.html
echo "<h3><center>For More Info Visit MY <a href="https://github.com/apidotmy">Github Repository</a></center><h3>" >> /home/vps/public_html/index.html
echo "<h3><center>You Can Also Contact Me On <a href="https://www.facebook.com/nenekkaukeling">Facebook</a> | <a href="https://telegram.me/ImAcaii">Telegram</a></center></h3>" >> /home/vps/public_html/index.html
wget -O /etc/nginx/conf.d/vps.conf "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/Nginx/vps.conf"
service nginx restart

# Install OpenVPN
apt-get -y install openvpn easy-rsa openssl iptables
cp -r /usr/share/easy-rsa/ /etc/openvpn
mkdir /etc/openvpn/easy-rsa/keys
sed -i 's|export KEY_COUNTRY="US"|export KEY_COUNTRY="MY"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_PROVINCE="CA"|export KEY_PROVINCE="MY"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_CITY="SanFrancisco"|export KEY_CITY="MY"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_ORG="Fort-Funston"|export KEY_ORG="ACAI KACAK"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_EMAIL="me@myhost.mydomain"|export KEY_EMAIL="acaikacak@gmail.com"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_OU="MyOrganizationalUnit"|export KEY_OU="ACAI KACAK"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_NAME="EasyRSA"|export KEY_NAME="ACAI KACAK"|' /etc/openvpn/easy-rsa/vars
sed -i 's|export KEY_OU=changeme|export KEY_OU=ACAI KACAK|' /etc/openvpn/easy-rsa/vars

# Create Diffie-Helman Pem
openssl dhparam -out /etc/openvpn/dh2048.pem 2048

# Create PKI
cd /etc/openvpn/easy-rsa
cp openssl-1.0.0.cnf openssl.cnf
. ./vars
./clean-all
export EASY_RSA="${EASY_RSA:-.}"
"$EASY_RSA/pkitool" --initca $*

# Create key server
export EASY_RSA="${EASY_RSA:-.}"
"$EASY_RSA/pkitool" --server server

# Setting KEY CN
export EASY_RSA="${EASY_RSA:-.}"
"$EASY_RSA/pkitool" client


# cp /etc/openvpn/easy-rsa/keys/{server.crt,server.key,ca.crt} /etc/openvpn
cd
cp /etc/openvpn/easy-rsa/keys/server.crt /etc/openvpn/server.crt
cp /etc/openvpn/easy-rsa/keys/server.key /etc/openvpn/server.key
cp /etc/openvpn/easy-rsa/keys/ca.crt /etc/openvpn/ca.crt

# Setting Server
cd /etc/openvpn/
wget "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/OpenVPN/server.conf"

# set time GMT +8
ln -fs /usr/share/zoneinfo/Asia/Manila /etc/localtime

# Create OpenVPN Config
cd
mkdir -p /home/vps/public_html
cd /home/vps/public_html/
wget "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/OpenVPN/client.ovpn"
sed -i $MYIP2 /home/vps/public_html/client.ovpn;
echo '<ca>' >> /home/vps/public_html/client.ovpn
cat /etc/openvpn/ca.crt >> /home/vps/public_html/client.ovpn
echo '</ca>' >> /home/vps/public_html/client.ovpn
wget "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/OpenVPN/clientssl.ovpn"
sed -i $MYIP2 /home/vps/public_html/clientssl.ovpn;
echo '<ca>' >> /home/vps/public_html/clientssl.ovpn
cat /etc/openvpn/ca.crt >> /home/vps/public_html/clientssl.ovpn
echo '</ca>' >> /home/vps/public_html/clientssl.ovpn
wget "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/Stunnel%20Client/stunnel.conf"
sed -i $MYIP2 /home/vps/public_html/stunnel.conf;
cd /home/vps/public_html/
tar -czf /home/vps/public_html/client.tar.gz client.ovpn clientssl.ovpn stunnel.conf
cd

# Restart OpenVPN
/etc/init.d/openvpn restart

# Setting UFW
apt-get install ufw
ufw allow ssh
ufw allow 3306/tcp
sed -i 's|DEFAULT_INPUT_POLICY="DROP"|DEFAULT_INPUT_POLICY="ACCEPT"|' /etc/default/ufw
sed -i 's|DEFAULT_FORWARD_POLICY="DROP"|DEFAULT_FORWARD_POLICY="ACCEPT"|' /etc/default/ufw
cd /etc/ufw/
wget "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/OpenVPN/before.rules"
cd
ufw enable
ufw status
ufw disable

# set ipv4 forward
echo 1 > /proc/sys/net/ipv4/ip_forward
sed -i 's|#net.ipv4.ip_forward=1|net.ipv4.ip_forward=1|' /etc/sysctl.conf

# Install BadVPN
cd
wget -O /usr/bin/badvpn-udpgw "https://github.com/johndesu090/AutoScriptDeb8/raw/master/Files/BadVPN/badvpn-udpgw"
if [ "$OS" == "x86_64" ]; then
  wget -O /usr/bin/badvpn-udpgw "https://github.com/johndesu090/AutoScriptDeb8/raw/master/Files/BadVPN/badvpn-udpgw64"
fi
sed -i '$ i\screen -AmdS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7300' /etc/rc.local
chmod +x /usr/bin/badvpn-udpgw
screen -AmdS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7300

# SSH Configuration
cd
sed -i '/Port 22/a Port 144' /etc/ssh/sshd_config
sed -i '/Port 22/a Port  81' /etc/ssh/sshd_config
sed -i 's/Port 22/Port  22/g' /etc/ssh/sshd_config
service ssh restart

# Install Dropbear
apt-get -y install busybox dropbear*
sed -i 's/NO_START=1/NO_START=0/g' /etc/default/dropbear
sed -i 's/DROPBEAR_PORT=22/DROPBEAR_PORT=442/g' /etc/default/dropbear
sed -i 's/DROPBEAR_EXTRA_ARGS=/DROPBEAR_EXTRA_ARGS="-p 82 -p 142"/g' /etc/default/dropbear
echo "/bin/false" >> /etc/shells
echo "/usr/sbin/nologin" >> /etc/shells
service ssh restart
service dropbear restart

# Install Squid3
cd
apt-get -y install squid3
wget -O /etc/squid3/squid.conf "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/Squid/squid3.conf"
sed -i $MYIP2 /etc/squid3/squid.conf;
service squid3 restart

# Install WebMin
cd
apt-get -y install webmin
sed -i 's/ssl=1/ssl=0/g' /etc/webmin/miniserv.conf
service webmin restart

# Install Stunnel
apt-get -y install stunnel4
cd /etc/stunnel/
openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -sha256 -subj '/CN=127.0.0.1/O=localhost/C=US' -keyout /etc/stunnel/stunnel.pem -out /etc/stunnel/stunnel.pem
sudo touch stunnel.conf
echo "client = no" > /etc/stunnel/stunnel.conf
echo "pid = /var/run/stunnel.pid" >> /etc/stunnel/stunnel.conf
echo "[openvpn]" >> /etc/stunnel/stunnel.conf
echo "accept = 444" >> /etc/stunnel/stunnel.conf
echo "connect = 127.0.0.1:3306" >> /etc/stunnel/stunnel.conf
echo "cert = /etc/stunnel/stunnel.pem" >> /etc/stunnel/stunnel.conf
sudo sed -i -e 's/ENABLED=0/ENABLED=1/g' /etc/default/stunnel4
iptables -A INPUT -p tcp --dport 444 -j ACCEPT
sudo cp /etc/stunnel/stunnel.pem ~
echo "client = yes\ndebug = 6\n[openvpn]\naccept = 127.0.0.1:3306\nconnect = $IPADDRESS:444\nTIMEOUTclose = 0\nverify = 0\nsni = m.facebook.com" > /var/www/html/stunnel.conf
service stunnel4 restart

# Install Fail2Ban
apt-get -y install fail2ban;
service fail2ban restart

# Install DDOS Deflate
cd
apt-get -y install dnsutils dsniff
wget "https://raw.githubusercontent.com/apidotmy/Autoscript/raw/master/Files/Others/ddos-deflate-master.zip"
unzip ddos-deflate-master.zip
cd ddos-deflate-master
./install.sh
cd
rm -rf ddos-deflate-master.zip

# Banner
rm /etc/issue.net
wget -O /etc/issue.net "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/Others/issue.net"
sed -i 's@#Banner@Banner@g' /etc/ssh/sshd_config
sed -i 's@DROPBEAR_BANNER=""@DROPBEAR_BANNER="/etc/issue.net"@g' /etc/default/dropbear
service ssh restart
service dropbear restart

# XML Parser
cd
apt-get -y --force-yes -f install libxml-parser-perl

# Setting Iptables
cat > /etc/iptables.up.rules <<-END
*nat
:PREROUTING ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -j SNAT --to-source xxxxxxxxx
-A POSTROUTING -o eth0 -j MASQUERADE
-A POSTROUTING -s 192.168.100.0/24 -o eth0 -j MASQUERADE
-A POSTROUTING -s 10.1.0.0/24 -o eth0 -j MASQUERADE
COMMIT

*filter
:INPUT ACCEPT [19406:27313311]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [9393:434129]
:fail2ban-ssh - [0:0]
-A FORWARD -i eth0 -o ppp0 -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i ppp0 -o eth0 -j ACCEPT
-A INPUT -p tcp -m multiport --dports 22 -j fail2ban-ssh
-A INPUT -p ICMP --icmp-type 8 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 53 -j ACCEPT
-A INPUT -p tcp --dport 22  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 80  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 80  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 142  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 144  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 143  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 109  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 110  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 444  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 443  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 3306  -m state --state NEW -j ACCEPT
-A INPUT -p udp --dport 3306  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 1732  -m state --state NEW -j ACCEPT
-A INPUT -p udp --dport 1732  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 1194  -m state --state NEW -j ACCEPT
-A INPUT -p udp --dport 1194  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 3128  -m state --state NEW -j ACCEPT
-A INPUT -p udp --dport 3128  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 7300  -m state --state NEW -j ACCEPT
-A INPUT -p udp --dport 7300  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 3355  -m state --state NEW -j ACCEPT
-A INPUT -p udp --dport 3355  -m state --state NEW -j ACCEPT
-A INPUT -p tcp --dport 10000  -m state --state NEW -j ACCEPT
-A fail2ban-ssh -j RETURN
COMMIT

*raw
:PREROUTING ACCEPT [158575:227800758]
:OUTPUT ACCEPT [46145:2312668]
COMMIT

*mangle
:PREROUTING ACCEPT [158575:227800758]
:INPUT ACCEPT [158575:227800758]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [46145:2312668]
:POSTROUTING ACCEPT [46145:2312668]
COMMIT
END
sed -i $MYIP2 /etc/iptables.up.rules;
iptables-restore < /etc/iptables.up.rules
cat > /etc/rc.local <<-END
#!/bin/sh -e

exit 0
END
chmod +x /etc/rc.local
sed -i '$ i\echo "nameserver 8.8.8.8" > /etc/resolv.conf' /etc/rc.local
sed -i '$ i\echo "nameserver 8.8.4.4" >> /etc/resolv.conf' /etc/rc.local
sed -i '$ i\iptables-restore < /etc/iptables.up.rules' /etc/rc.local

# Install Screenfetch
apt-get -y install lsb-release scrot
wget -O screenfetch "https://raw.githubusercontent.com/apidotmy/Autoscript/master/Files/Others/screenfetch"
chmod +x screenfetch

# Download Commands
cd /usr/bin
wget https://raw.githubusercontent.com/apidotmy/Autoscript/raw/master/Files/Menu/Menu.tar.gz
tar -xzvf Menu.tar.gz
rm Menu.tar.gz
sed -i -e 's/\r$//' accounts
sed -i -e 's/\r$//' bench-network
sed -i -e 's/\r$//' clearcache
sed -i -e 's/\r$//' connections
sed -i -e 's/\r$//' create
sed -i -e 's/\r$//' create_random
sed -i -e 's/\r$//' create_trial
sed -i -e 's/\r$//' delete_expired
sed -i -e 's/\r$//' diagnose
sed -i -e 's/\r$//' edit_dropbear
sed -i -e 's/\r$//' edit_openssh
sed -i -e 's/\r$//' edit_openvpn
sed -i -e 's/\r$//' edit_ports
sed -i -e 's/\r$//' edit_squid3
sed -i -e 's/\r$//' edit_stunnel4
sed -i -e 's/\r$//' locked_list
sed -i -e 's/\r$//' menu
sed -i -e 's/\r$//' options
sed -i -e 's/\r$//' ram
sed -i -e 's/\r$//' reboot_sys
sed -i -e 's/\r$//' reboot_sys_auto
sed -i -e 's/\r$//' restart_services
sed -i -e 's/\r$//' server
sed -i -e 's/\r$//' set_multilogin_autokill
sed -i -e 's/\r$//' set_multilogin_autokill_lib
sed -i -e 's/\r$//' show_ports
sed -i -e 's/\r$//' speedtest
sed -i -e 's/\r$//' user_delete
sed -i -e 's/\r$//' user_details
sed -i -e 's/\r$//' user_details_lib
sed -i -e 's/\r$//' user_extend
sed -i -e 's/\r$//' user_list
sed -i -e 's/\r$//' user_lock
sed -i -e 's/\r$//' user_unlock

# AutoReboot Tools
echo "10 0 * * * root /usr/local/bin/reboot_sys" > /etc/cron.d/reboot_sys
echo "0 1 * * * root delete_expired" > /etc/cron.d/delete_expired
echo "*0 */2 * * * root clearcache" > /etc/cron.d/clearcache

# Set Permissions
cd /usr/bin
chmod +x create
chmod +x accounts
chmod +x create
chmod +x create_random
chmod +x create_trial
chmod +x user_list
chmod +x user_details
chmod +x user_details_lib
chmod +x user_extend
chmod +x user_delete
chmod +x user_lock
chmod +x user_unlock
chmod +x connections
chmod +x delete_expired
chmod +x locked_list
chmod +x options
chmod +x set_multilogin_autokill
chmod +x set_multilogin_autokill_lib
chmod +x restart_services
chmod +x edit_ports
chmod +x show_ports
chmod +x edit_openssh
chmod +x edit_dropbear
chmod +x edit_stunnel4
chmod +x edit_openvpn
chmod +x edit_squid3
chmod +x reboot_sys
chmod +x reboot_sys_auto
chmod +x clearcache
chmod +x server
chmod +x ram
chmod +x diagnose
chmod +x bench-network
chmod +x speedtest

# Finishing
cd
chown -R www-data:www-data /home/vps/public_html
service nginx start
service openvpn restart
service cron restart
service ssh restart
service dropbear restart
service squid3 restart
service webmin restart
rm -rf ~/.bash_history && history -c
rm -f /root/AutoScriptDebian
echo "unset HISTFILE" >> /etc/profile

# grep ports 
opensshport="$(netstat -ntlp | grep -i ssh | grep -i 0.0.0.0 | awk '{print $4}' | cut -d: -f2)"
dropbearport="$(netstat -nlpt | grep -i dropbear | grep -i 0.0.0.0 | awk '{print $4}' | cut -d: -f2)"
stunnel4port="$(netstat -nlpt | grep -i stunnel | grep -i 0.0.0.0 | awk '{print $4}' | cut -d: -f2)"
openvpnport="$(netstat -nlpt | grep -i openvpn | grep -i 0.0.0.0 | awk '{print $4}' | cut -d: -f2)"
squidport="$(cat /etc/squid3/squid.conf | grep -i http_port | awk '{print $2}')"
nginxport="$(netstat -nlpt | grep -i nginx| grep -i 0.0.0.0 | awk '{print $4}' | cut -d: -f2)"

# Info
clear
echo -e ""
echo -e "\e[94m[][][]======================================[][][]"
echo -e "\e[0m                                                   "
echo -e "\e[94m           AutoScriptVPS BY ACAI KACAK            "
echo -e "\e[94m        https://facebook.com/nenekkaukeling       "
echo -e "\e[94m                    Services                      "
echo -e "\e[94m                                                  "
echo -e "\e[94m    OpenSSH        :   "$opensshport
echo -e "\e[94m    Dropbear       :   "$dropbearport
echo -e "\e[94m    SSL            :   "$stunnel4port
echo -e "\e[94m    OpenVPN        :   "3306
echo -e "\e[94m    Port Squid     :   "3355
echo -e "\e[94m    Nginx          :   "$nginxport
echo -e "\e[94m                                                  "
echo -e "\e[94m              Other Features Included             "
echo -e "\e[94m                                                  "
echo -e "\e[94m    Timezone       :   Asia/Manila (GMT +7)       "
echo -e "\e[94m    Webmin         :   http://$MYIP:10000/        "
echo -e "\e[94m    IPV6           :   [OFF]                      "
echo -e "\e[94m    Cron Scheduler :   [ON]                       "
echo -e "\e[94m    Fail2Ban       :   [ON]                       "
echo -e "\e[94m    DDOS Deflate   :   [ON]                       "
echo -e "\e[94m    LibXML Parser  :   {ON]                       "
echo -e "\e[0m                                                   "
echo -e "\e[94m[][][]======================================[][][]\e[0m"
echo -e "\e[0m                                                   "
read -n1 -r -p "          Press Any Key To Show Commands          "
menu
cd