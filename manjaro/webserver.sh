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

if ! pacman -Qs '^apache'; then
  pacman -S apache --noconfirm > /dev/null 2>&1
else
  printf "Apache var allerede installeret\n"
fi

sed -i -f $(pwd)/../config/httpd.conf /etc/httpd/conf/httpd.conf
cp $(pwd)/../config/php-fpm.conf /etc/httpd/conf/extra/.
cp $(pwd)/../config/index.html /srv/http/index.html
printf "<?php\n phpinfo();\n" | tee /srv/http/index.php
printf "Apache er konfigureret\n"


if ! pacman -Qs '^nginx'; then
  pacman -S nginx --noconfirm > /dev/null 2>&1
else
  printf "Nginx var allerede installeret\n"
fi
cp $(pwd)/../config/nginx.conf /etc/nginx/.
printf "<?php\n phpinfo();\n" | tee /usr/share/nginx/html/index.php
printf "nginx er konfigureret\n"

