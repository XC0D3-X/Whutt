#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

# Details
country=MY
state=KL
locality=KL
organization=AcaiKacak
organizationalunit=AcaiKacak
commonname=AcaiKacak
email=acaikacak@acaikacak.my

# Disable IPV6
echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
sed -i '$ i\echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6' /etc/rc.local

# ROOT
cd
# UPDATE
apt-get install net-tools
apt-get -y update

# SET REPO WEBMIN
sh -c 'echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list'
wget -qO - http://www.webmin.com/jcameron-key.asc | apt-key add -

# SETTING & INSTALL VNSTAT DEBIAN 9 64 BIT
apt-get -y install vnstat
systemctl start vnstat
systemctl enable vnstat
chkconfig vnstat on

# SQUID 3
cd
apt-get -y install squid3
wget -O /etc/squid/squid.conf "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/squid3.conf"
/etc/init.d/squid restart

# WEBMIN
cd
wget https://nchc.dl.sourceforge.net/project/webadmin/webmin/1.910/webmin_1.910_all.deb
dpkg --install webmin_1.910_all.deb;
apt-get -y -f install;
sed -i 's/ssl=1/ssl=0/g' /etc/webmin/miniserv.conf
rm -f webmin_1.910_all.deb
/etc/init.d/webmin restart

echo "=================  Stunnel Install  ====================="
echo "========================================================="

# STUNNEL
apt-get install stunnel4 -y
cat > /etc/stunnel/stunnel.conf <<-END
cert = /etc/stunnel/stunnel.pem
client = no
socket = a:SO_REUSEADDR=1
socket = l:TCP_NODELAY=1
socket = r:TCP_NODELAY=1
[openvpnssl]
accept = 833
connect = 127.0.0.1:1194

END

echo "=================  Creating Certificate OpenSSL ======================"
echo "========================================================="

#Creating Certificate
openssl genrsa -out key.pem 2048
openssl req -new -x509 -key key.pem -out cert.pem -days 1095 \
-subj "/C=$country/ST=$state/L=$locality/O=$organization/OU=$organizationalunit/CN=$commonname/emailAddress=$email"
cat key.pem cert.pem >> /etc/stunnel/stunnel.pem

# Configuration Stunnel
sed -i 's/ENABLED=0/ENABLED=1/g' /etc/default/stunnel4
/etc/init.d/stunnel4 restart
chown -R vnstat:vnstat /var/lib/vnstat

cd
sed -i '$ i\0 */12 * * * root /usr/bin/fix' /etc/crontab

cd /usr/bin
wget -O fix "https://raw.githubusercontent.com/apidotmy/Autoscript/main/Files/Debian10/fix.sh"
chmod +x fix

sudo apt-get install gnupg1 apt-transport-https dirmngr -y
export INSTALL_KEY=379CE192D401AB61
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY
echo "deb https://ookla.bintray.com/debian generic main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
sudo apt-get update -y
sudo apt-get install speedtest -y
