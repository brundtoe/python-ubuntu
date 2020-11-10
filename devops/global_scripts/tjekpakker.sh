#! /usr/bin/env bash
set -e
if [ $UID != "0" ]; then
   echo "scriptet skal afvikes med root acces"
fi

PACKAGES="gcc make linux-generic
linux-headers-$(uname -r) build-essential dkms
vim curl wget git lynx
cifs-utils samba
sqlite3 libsqlite3-dev
python2.7 python-dev python2.7-dev
unixodbc unixodbc-dev
libssl-dev libmysqlclient-dev
patch ruby-dev
zlib1g-dev liblzma-dev libkrb5-dev libkrb5-dbg
"
# set + e
for package in $PACKAGES
do
   dpkg -s $package  > /dev/null   2>&1 || true
   if [ $? -ne 0 ]; then
      printf "Package $package er IKKE installeret!\n"
   else
      printf "Package $package er installeret!\n"
   fi
done
