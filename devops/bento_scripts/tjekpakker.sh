#! /usr/bin/env bash
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
for package in $PACKAGES
do
   dpkg -s $package &> /dev/null
   if [ $? -ne 0 ]; then
      printf "Package $package er IKKE installeret!\n"
   else
      printf "Package $package er installeret!\n"
   fi
done
