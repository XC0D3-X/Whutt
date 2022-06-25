#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

Login=trial-`</dev/urandom tr -dc X-Z0-9 | head -c4`
lama="1"
Pass=`</dev/urandom tr -dc a-f0-9 | head -c9`
IP=$(ip route get 1 | awk '{print $NF;exit}')
useradd -e `date -d "$lama days" +"%Y-%m-%d"` -s /bin/false -M $Login
host=$( hostname )
country=$( wget -qO- https://get.geojs.io/v1/ip/country/full )
echo -e "$Pass\n$Pass\n"|passwd $Login &> /dev/null
clear
echo -e "Username: $Login"
echo -e "Password: $Pass"
echo -e "Hostname: $host"
echo -e "Country: $country"
echo -e "SSL/TLS Port: 443, 80"
echo -e "SSH Port: 109, 110, 80, 143"
echo -e "Squid Port: 8000, 8080, 3128"