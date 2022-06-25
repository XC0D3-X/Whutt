#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

installation_dir="/opt/"
badvpn_dir_name="badvpn-1.999.130"
touch /etc/rc.local
sudo apt-get install cmake build-essential -y
sudo apt-get install screen wget gcc build-essential g++ make -y
sudo apt-get install unzip
wget https://codeload.github.com/ambrop72/badvpn/zip/1.999.130
unzip -o 1.999.130 -d "$installation_dir/"
cd "$installation_dir/"
cmake "$installation_dir/$badvpn_dir_name" -DBUILD_NOTHING_BY_DEFAULT=1 -DBUILD_UDPGW=1
make install
echo
echo
echo "***** BadVPN Runs on Port 7300 *****"
badvpn-udpgw --listen-addr 127.0.0.1:7300 > /dev/null &
netstat -nlpt | grep 7300
sed -i '$ i\screen -AmdS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7300' /etc/rc.local
chmod +x /usr/local/bin/badvpn-udpgw
screen -AmdS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7300
echo
echo
echo "Removing unnecessary file(s)..."
rm -rf "$installation_dir/1.999.130"
echo
echo "Removed!"
echo
echo "Enjoy!"
echo
