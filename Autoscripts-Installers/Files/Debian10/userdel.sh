#!/bin/bash
# .++=====[Author: Acai Kacak]=====++.

read -p "SSH Username to delete : " Pengguna

if getent passwd $Pengguna > /dev/null 2>&1; then
        userdel $Pengguna
        echo -e "User $Pengguna Deleted."
else
        echo -e "Failed: User $Pengguna Not Found."
fi