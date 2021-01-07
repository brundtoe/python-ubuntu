#!/usr/bin/env bash 

export DEBIAN_FRONTEND=noninteractive

set -e

apt-get update
apt-get upgrade -y

apt-get install -y \
        build-essential \
        linux-headers-generic \
        dkms \
        ssh \
        lsb-core \
        software-properties-common \
        apt-transport-https \
        ca-certificates \
        vim \
        git \
        python3-pip \
        python3-setuptools \
        python3-virtualenv

       
sed -Ei 's/^(#?)(PasswordAuthentication)(\s*no)/\2 yes/' /etc/ssh/sshd_config        
systemctl enable ssh
systemctl start ssh



#curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -        

apt-get update

echo "Installerede basis programmer"        
