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

PACKAGES="apache nginx"

for package in $PACKAGES
do
    if ! pacman -Qe $package; then
      pacman -S $package --noconfirm > /dev/null 2>&1
      sed -i -f $(pwd)/../config/httpd.conf /etc/httpd/conf/httpd.conf
      cp $(pwd)/../config/php-fpm.conf /etc/httpd/conf/extra/.
      cp $(pwd)/../config/nginx.conf /etc/nginx/.
    else
      printf "$package OK\n"
    fi
done
