#!/usr/bin/env bash

#mine tilføjelser til bento/ubuntu boxes
# af ekstra software repositories

# Puppetlabs repository
apt-get -y install dpkg
wget https://apt.puppetlabs.com/puppet6-release-bionic.deb -o /tmp/puppet6-release-bionic.deb
dpkg -i puppet6-release-bionic.deb

#Nodejs repository
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

# yarn repository
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
printf "deb https://dl.yarnpkg.com/debian/ stable main\n" | tee /etc/apt/sources.list.d/yarn.list

# mongodb 4.2 repository
#
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

# Indtil videre anvendes nginx fra bionic beaver
# nginx det er for bøvlet at anvende denne fra nginx.org på Ubuntu
# wget http://nginx.org/keys/nginx_signing.key
#apt-key add nginx_signing.key
#printf "deb http://nginx.org/packages/ubuntu/ bionic nginx\n" | tee /etc/apt/sources.list.d/nginx.list
#printf "deb-src http://nginx.org/packages/ubuntu/ bionic nginx\n" tee -a /etc/apt/sources.list.d/nginx.list
# opdater repositoriet med data fra ovennævnte tilføjelser
apt-get update
