#! /usr/bin/env bash -eux

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

export DEBIAN_FRONTEND=noninteractive

# MongoDB 4.4 
# ref. https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
# skal opdateres ved hvert skifte af MongoDB version

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

apt-get update

# mongodb-org indeholder alle moduler

apt-get install -y mongodb-org

cp -f mongod.conf /etc/mongod.conf
