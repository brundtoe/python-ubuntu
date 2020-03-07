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
apache
nginx
nodejs-lts-erbium
docker
docker-compose
firefox
#chromium
#chromium
#keepass
#filezilla
#bleachbit
#gimp
#vlc
#code
#virtualbox
#puppet
#ansible
#vagrant
#packer
"

set +e
for package in $PACKAGES
do

    pack=${package:0:1}
    if [ $pack = "#" ]; then
        printf "fundet $package\n"
    else
        pacman -S $package --noconfirm > /dev/null 2>&1
        if [ $? -ne "0" ]; then
            printf "Package ${package:1} findes ikke *******\n"
        else
            printf "$package OK\n"
        fi
    fi
doneset -e

