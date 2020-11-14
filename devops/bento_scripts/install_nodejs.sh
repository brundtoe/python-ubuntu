#! /usr/bin/env bash 

set -eu

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

export DEBIAN_FRONTEND=noninteractive

# Nodejs version 14.x

curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

apt-get update

apt-get install -y nodejs

# Opdatering af npm

npm install npm -g

# Installation af node modulet, der oprettet express applikationer

sudo npm install -g \
    express-generator \
    json-server \
    nodemon \
    pm2


