#!/usr/bin/env bash -eu

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

# One last upgrade check
apt-get upgrade -y

# Clean Up
apt -y autoremove
apt -y clean
chown -R vagrant:vagrant /home/vagrant
chown -R vagrant:vagrant /usr/local/bin