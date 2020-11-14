#! /usr/bin/env bash

set -eux
export DEBIAN_FRONTEND=noninteractive

# Nodejs version 14.x

sudo curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

# MongoDB 4.4 
# ref. https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
# skal opdateres ved hvert skifte af MongoDB version

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

sudo apt-get update