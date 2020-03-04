#!/usr/bin/env bash

set -e

if [ $UID != "0" ]
then
    echo "Script kræver root adgang"
    exit 1
fi

## opdeles i to filer en for pgm uden gui og en med gui

## hvad sker der hvis en linje ændres til en kommentar

pacman -Syu --noconfirm

PACKAGES="gcc
make
perl
dkms
patch
curl
wget
git
vim
tmux
cifs-utils
sqlite
python
python-pip
acl
ca-certificates
hplip-minimal
mariadb
mysql-workbench
keepass
filezilla
bleachbit
nodejs-lts-erbium
chromium
firefox
gimp
vlc
code
docker
docker-compose
chromium
virtualbox
puppet
apache
nginx
ansible
vagrant
packer
"

set +e
for package in $PACKAGES
do
    # pacman -Qi $package  > /dev/null 2>&1
    pacman -S $package --noconfirm  > /dev/null 2>&1
    if [ $? -ne "0" ]; then
        printf "Package $package kan ikke installeres *****\n"
    else
        printf "$package OK\n"
    fi
done
set -e

