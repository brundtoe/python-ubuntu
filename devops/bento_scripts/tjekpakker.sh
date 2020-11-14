#! /usr/bin/env bash
PACKAGES="lsb-release
dkms build-essential
software-properties-common
linux-headers-generic
apt-transport-https
vim curl wget git
cifs-utils
python3-pip
python3-setuptools
python-apt
python3-virtualenv
sqlite3 libsqlite3-dev
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
