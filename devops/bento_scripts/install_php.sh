#!/usr/bin/env bash -eux

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get upgrade -y

apt-get install -y \
   php7.4-cli \
   php7.4-cgi \
   php7.4-fpm \
   php7.4-bcmath \
   php7.4-bz2 \
   php7.4-common \
   php7.4-curl \
   php7.4-dev \
   php7.4-intl \
   php7.4-json \
   php-7.4-mysql \
   php7.4-opcache \
   php7.4-phpdbg \
   php7.4-readline \
   php7.4-sqlite \
   php7.4-tidy \
   php7.4-xml \
   php7.4-xmlrpc \
   php7.4-mbstring \
   php7.4-xsl \
   php7.4-zip \
   php-xdebug

echo "Det var installationen af php"