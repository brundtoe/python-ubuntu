#!/usr/bin/env bash

set -eux
export DEBIAN_FRONTEND=noninteractive

#mine tilføjelser til bento/ubuntu boxes

sudo apt-get update
sudo apt-get upgrade -y
# dpkg skal være installeret, da den anvendes senere i scriptet
sudo apt-get -y install dpkg

sudo apt-get install -y \
  lsb-release \
  dkms \
  build-essential \
  software-properties-common \
  linux-headers-generic \
  apt-transport-https \
  gnupg \
  vim \
  curl \
  wget \
  git \
  cifs-utils \
  python3-pip \
  python3-setuptools \
  python-apt \
  python3-virtualenv \
  sqlite3 \
  libsqlite3-dev
