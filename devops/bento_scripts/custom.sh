#!/usr/bin/env bash

#mine tilføjelser til bento/ubuntu boxes

# Installer pakkerne
PACKAGES="gcc make
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
# PHP7.2 må ikke installeres, da den også installerer Apache2
# Det er ikke nødvendigt at installere php7.2-cli og php7.2-cgi

for package in $PACKAGES
do
  apt-get install -y $package
done

bindir=/home/vagrant/bin
if ! [ -d $bindir ]
then
   printf "Opretter /home/vagrant/bin"
   sudo mkdir $bindir && sudo chown vagrant:vagrant $bindir
fi
