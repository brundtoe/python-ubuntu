#! /usr/bin/env bash

set -eux
export DEBIAN_FRONTEND=noninteractive

# Nodejs version 14.x

sudo curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt-get update

sudo apt-get install -y nodejs

# Opdatering af npm

sudo npm install npm -g

# Installation af node modulet, der oprettet express applikationer

sudo npm install - g \
    express-generator \
    json-server
