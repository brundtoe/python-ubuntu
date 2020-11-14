#! /usr/bin/env bash 

set -eu

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

export DEBIAN_FRONTEND=noninteractive

#mine tilføjelser til bento/ubuntu boxes

apt-get update
apt-get upgrade -y
# dpkg skal være installeret, da den anvendes senere i scriptet
apt-get -y install dpkg

apt-get install -y \
  lsb-release \
  dkms \
  build-essential \
  software-properties-common \
  linux-headers-generic \
  debconf-utils \
  apt-transport-https \
  gnupg \
  vim \
  curl \
  wget \
  git \
  expect \
  cifs-utils \
  python3-pip \
  python3-setuptools \
  python-apt \
  python3-virtualenv \
  sqlite3 \
  libsqlite3-dev
