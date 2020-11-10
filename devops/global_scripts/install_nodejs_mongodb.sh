#! /usr/bin/env bash

# Installer nodejs version 8.x

sudo curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

# Opdatering af npm

sudo npm install npm -g

# Installation af node modulet, der oprettet express applikationer

sudo npm install express-generator -g

# Installation af globale node-moduler

sudo npm install grunt--global
sudo npm install less --global
sudo npm install karma-cli --global


# Installation af database moduler - foretages loklat i de enkelte projekter

# npm install mysql --save
# npm install sqlite3 --save

# Installation af yarn - erstatter bower

sudo curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt-get update && sudo apt-get install yarn

# Installation af mongodb 4.x august 2018

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

sudo echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list

sudo apt-get update
sudo apt-get install -y mongodb-org

sudo cp -f mongod.conf /etc/mongod.conf
