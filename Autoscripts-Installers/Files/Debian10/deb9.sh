#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

# initialisasi var
export DEBIAN_FRONTEND=noninteractive
OS=`uname -m`;
MYIP=`curl -s ifconfig.me`;
MYIP2="s/xxxxxxxxx/$MYIP/g";

# detail nama perusahaan
country=MY
state=KL
locality=KL
organization=AcaiKacak
organizationalunit=AcaiKacak
commonname=AcaiKacak
email=acaikacak@acaikacak.my

# go to root
cd

# disable ipv6
echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
sed -i '$ i\echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6' /etc/rc.local

# set time GMT +7 singapore
ln -fs /usr/share/zoneinfo/Asia/Singapore /etc/localtime

# set locale
sed -i 's/AcceptEnv/#AcceptEnv/g' /etc/ssh/sshd_config
/etc/init.d/ssh restart

# Edit file /etc/systemd/system/rc-local.service
cat > /etc/systemd/system/rc-local.service <<-END
[Unit]
Description=/etc/rc.local
ConditionPathExists=/etc/rc.local
[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99
[Install]
WantedBy=multi-user.target
END

# nano /etc/rc.local
cat > /etc/rc.local <<-END
#!/bin/sh -e
# rc.local
# By default this script does nothing.
exit 0
END

# Ubah izin akses
chmod +x /etc/rc.local

# enable rc local
systemctl enable rc-local
systemctl start rc-local.service

echo "=================  Installing Neofetch  ===================="
echo "========================================================="
# install neofetch
apt-get update -y
apt-get -y install gcc
apt-get -y install make
apt-get -y install cmake
apt-get -y install git
apt-get -y install screen
apt-get -y install unzip
apt-get -y install curl
git clone https://github.com/dylanaraps/neofetch
cd neofetch
make install
make PREFIX=/usr/local install
make PREFIX=/boot/home/config/non-packaged install
make -i install
apt-get -y install neofetch
cd

# update
apt-get -y update

# set repo webmin
sh -c 'echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list'
wget -qO - http://www.webmin.com/jcameron-key.asc | apt-key add -

echo "================  Installing Dropbear ======================"
echo "========================================================="

# install dropbear
apt-get -y install dropbear
sed -i 's/NO_START=1/NO_START=0/g' /etc/default/dropbear
sed -i 's/DROPBEAR_PORT=22/DROPBEAR_PORT=143/g' /etc/default/dropbear
sed -i 's/DROPBEAR_EXTRA_ARGS=/DROPBEAR_EXTRA_ARGS="-p 109 -p 110"/g' /etc/default/dropbear
echo "/bin/false" >> /etc/shells
echo "/usr/sbin/nologin" >> /etc/shells
/etc/init.d/ssh restart
/etc/init.d/dropbear restart

echo "=================  Installing Squid 3  ======================"
echo "========================================================="

# setting dan install vnstat debian 9 64bit
apt-get -y install vnstat
systemctl start vnstat
systemctl enable vnstat
chkconfig vnstat on
chown -R vnstat:vnstat /var/lib/vnstat

# install squid3
cd
apt-get -y install squid3
wget -O /etc/squid/squid.conf "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/squid3.conf"
/etc/init.d/squid restart

# install webmin
cd
wget https://nchc.dl.sourceforge.net/project/webadmin/webmin/1.910/webmin_1.910_all.deb
dpkg --install webmin_1.910_all.deb;
apt-get -y -f install;
sed -i 's/ssl=1/ssl=0/g' /etc/webmin/miniserv.conf
rm -f webmin_1.910_all.deb
/etc/init.d/webmin restart

echo "=================  Installing Stunnel  ====================="
echo "========================================================="

# install stunnel
apt-get install stunnel4 -y
cat > /etc/stunnel/stunnel.conf <<-END
cert = /etc/stunnel/stunnel.pem
client = no
socket = a:SO_REUSEADDR=1
socket = l:TCP_NODELAY=1
socket = r:TCP_NODELAY=1
[dropbear]
accept = 443
connect = 127.0.0.1:143
[dropbear]
accept = 80
connect = 127.0.0.1:110
[openvpnssl]
accept = 833
connect = 127.0.0.1:1194

END

echo "=================  Creating Certificate OpenSSL ======================"
echo "========================================================="
#membuat sertifikat
openssl genrsa -out key.pem 2048
openssl req -new -x509 -key key.pem -out cert.pem -days 1095 \
-subj "/C=$country/ST=$state/L=$locality/O=$organization/OU=$organizationalunit/CN=$commonname/emailAddress=$email"
cat key.pem cert.pem >> /etc/stunnel/stunnel.pem

# konfigurasi stunnel
sed -i 's/ENABLED=0/ENABLED=1/g' /etc/default/stunnel4
/etc/init.d/stunnel4 restart

echo "================= Auto Installer BadVPN ======================"
wget https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/badvpn.sh && chmod +x badvpn.sh && bash badvpn.sh

# Custom Banner SSH
cd
wget -O /etc/issue.net "https://gitlab.com/presult77/autoscript/-/raw/master/redssh.net"
chmod +x /etc/issue.net
echo "DROPBEAR_BANNER="/etc/issue.net"" >> /etc/default/dropbear

# install fail2ban
apt-get -y install fail2ban
service fail2ban restart

# common password debian 
wget -O /etc/pam.d/common-password "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/common-password-deb9"
chmod +x /etc/pam.d/common-password

# download script
cd /usr/bin
wget -O menu "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/menu.sh"
wget -O user-add "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/useradd.sh"
wget -O trial "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/trial.sh"
wget -O user-login "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/userlogin.sh"
wget -O user-list "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/userlist.sh"
wget -O fix "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/fix.sh"
wget -O info "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/info.sh"
wget -O user-del "https://gitlab.com/presult77/autoscript/raw/master/userdel.html"
wget -O user-lock "https://gitlab.com/presult77/autoscript/raw/master/user-lock.html"
wget -O user-expire "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/userexpire.sh"
wget -O user-auto-limit "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/userautolimit.sh"

chmod +x menu
chmod +x user-add
chmod +x trial
chmod +x user-login
chmod +x user-list
chmod +x fix
chmod +x info
chmod +x user-del
chmod +x user-lock
chmod +x user-expire
chmod +x user-auto-limit

cd /usr/local/bin
wget -O user-auto-limit-script "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/userautolimitscript.sh"
chmod +x user-auto-limit-script

# finishing
cd
/etc/init.d/ssh restart
/etc/init.d/dropbear restart
/etc/init.d/stunnel4 restart

sudo apt-get install gnupg1 apt-transport-https dirmngr -y
export INSTALL_KEY=379CE192D401AB61
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY
echo "deb https://ookla.bintray.com/debian generic main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
sudo apt-get update -y
sudo apt-get install speedtest -y

rm -rf ~/.bash_history && history -c
echo "unset HISTFILE" >> /etc/profile
sed -i '$ i\59 23 * * * root /usr/bin/user-expire' /etc/crontab
sed -i '$ i\59 23 * * * root /usr/bin/user-lock' /etc/crontab
sed -i '$ i\59 23 * * * root /usr/bin/fix' /etc/crontab
sed -i '$ i\0 */1 * * * root /bin/badvpn start' /etc/crontab

cd

# Delete script
rm -f /root/deb9.sh
