#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

red='\e[1;31m'
green='\e[0;32m'
NC='\e[0m'
echo "Connecting to Server..."
sleep 0.4
echo "Checking Permision..."
sleep 0.4
CEK=0123456
if [ "$CEK" != "0123456" ]; then
		echo -e "${red}Permission Denied!${NC}";
        echo $CEK;
        exit 0;
else
echo -e "${green}Permission Accepted...${NC}"
sleep 1
clear
fi

if [ ! -e /usr/local/bin/user-auto-limit-script ]; then
echo 'FATAL ERROR'
echo 'Error Code: 404'
echo 'Please update your premium script!'
fi

echo "-------------------------------------------"
echo "         Auto Kill Multi Login Menu        "
echo "-------------------------------------------"
echo "1.  Set Auto Kill Multi Login 3  minutes"
echo "2.  Set Auto Kill Multi Login 5  minutes"
echo "3.  Set Auto Kill Multi Login 7  minutes"
echo "4.  Set Auto Kill Multi Login 10 minutes"
echo "5.  Set Auto Kill Multi Login 15 minutes"
echo "6.  Set Auto Kill Multi Login 30 minutes"
echo "7.  Turn off Auto-Limit"
echo "8.  View Multilogin Users Log"
echo "9.  Remove Log Limit"
echo "-------------------------------------------"
read -p "Select options from [1-9]: " x

if (($x<7)); then
echo " "
echo "-------------------------------------------"
read -p "Multilogin Maximum Number Of Allowed: " max

fi
if test $x -eq 1; then
echo "*/3 * * * *  root /usr/local/bin/user-auto-limit-script $max" > /etc/cron.d/user_auto_limit 
echo "User-Auto-Limit successfully set in 3 minutes."
elif test $x -eq 2; then
echo "*/5 * * * *  root /usr/local/bin/user-auto-limit-script $max" > /etc/cron.d/user_auto_limit
echo "User-Auto-Limit successfully set in 5 minutes."
elif test $x -eq 3; then
echo "*/7 * * * *  root /usr/local/bin/user-auto-limit-script $max" > /etc/cron.d/user_auto_limit
echo "User-Auto-Limit successfully set in 7 minutes."
elif test $x -eq 4; then
echo "*/10 * * * *  root /usr/local/bin/user-auto-limit-script $max" > /etc/cron.d/user_auto_limit
echo "User-Auto-Limit successfully set in 10 minutes."
elif test $x -eq 5; then
echo "*/15 * * * *  root /usr/local/bin/user-auto-limit-script $max" > /etc/cron.d/user_auto_limit
echo "User-Auto-Limit successfully set in 15 minutes."
elif test $x -eq 6; then
echo "*/30 * * * *  root /usr/local/bin/user-auto-limit-script $max" > /etc/cron.d/user_auto_limit
echo "User-Auto-Limit successfully set in 30 minutes."
elif test $x -eq 7; then
rm -f /etc/cron.d/user_auto_limit
echo "User-Auto-Limit has been successfully shut down."
elif test $x -eq 8; then
if [ ! -e /root/log-limit.txt ]; then
	echo "No user detected has multilogin activity"
	else 
	echo 'User log performed multilogin activity'
	echo "-------"
	cat /root/log-limit.txt
fi
elif test $x -eq 9; then
echo "" > /root/log-limit.txt
echo "Logs deleted successfully!"
else
echo "Options Not Available In Menu."
exit
fi
