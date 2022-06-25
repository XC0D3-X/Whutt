#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

clear
echo "====== Acai Kacak ====="
echo "Create New SSH & VPN Account"
echo "============================"
echo
echo -n "Username: "
read account
echo -n "Password [$account]: "
read pass
echo -n "Time: "
read exp
host=$( hostname )
country=$( wget -qO- https://get.geojs.io/v1/ip/country/full )
useradd -e `date -d "$exp days" +"%Y-%m-%d"` -g users -s /bin/false -M $account
expire="$(chage -l $account | grep "Account expires" | awk -F": " '{print $2}')"
echo -e "$pass\n$pass\n"|passwd $account &> /dev/null
clear
echo "Success Create"
echo
echo -e "Hostname: $host"
echo -e "Username: $account "
echo -e "Password: $pass"
echo -e "Country: $country"
echo -e "Time Period: $exp"
echo -e "Expired Date: $expire"
echo -e "SSL/TLS Port: 443, 80"
echo -e "SSH Port: 110, 109, 143"
echo -e
echo "Thankyou, Happy Go Lucky!"
echo -e
echo -e "Telgram: https://telegram.me/ImAcaii"
echo