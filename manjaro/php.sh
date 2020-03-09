#!/usr/bin/env bash

set -e

if [ $UID != "0" ]
then
    echo "Script kræver root adgang"
    exit 1
fi

## en række php-moduler findes som del af den af Arch Linux teamet kompilerede udgave af php

pacman -Syu --noconfirm

PACKAGES="php 
php-cgi 
php-fpm
php-sqlite
php-intl
php-xsl
xdebug
composer
#php-cli
#php-dom
#php-mbstring
#php-mysql
#php-curl
#php-json
#php-common
#php-mbstring
#php-zip
#php-BCMath
"

# der skal tilføjes en test af med pacman -Si

# kan pacman -q undertrykker output

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
  if pacman -Qs $package --noconfirm > /dev/null 2>&1; then
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
