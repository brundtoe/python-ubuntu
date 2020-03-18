#!/usr/bin/env bash

set -e

if [ $UID != "0" ]
then
    echo "Script kræver root adgang"
    exit 1
fi

## opdeles i to filer en for pgm uden gui og en med gui

## hvad sker der hvis en linje ændres til en kommentar
## gtk2 er krævet af smartgit
pacman -Syu --noconfirm

PACKAGES="gcc
make
perl
dkms
patch
curl
wget
git
gtk2
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
gnome-keyring
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
  # pakker der ikke skal installeres
  if [ $pack = "#" ]; then
      printf "fundet $package\n"
      continue
  fi
  # er pakken installeret
  if pacman -Qs "^$package$" --noconfirm > /dev/null 2>&1; then
    printf "Package $package er OK\n"
    continue
  fi
  # installer pakken
  if ! pacman -S $package --noconfirm > /dev/null 2>&1; then
     printf "Package $package kan ikke installeres\n"
  else
    printf  "Package $package er installeret\n"
  fi
done
set -e
printf "Det var så det!\n"
