#!/usr/bin/env bash 

set -e

pacman-mirrors --country Germany,France,Denmark,Sweden,Belgium,United_Kingdom
pacman -Syyu --noconfirm

pacman -S --noconfirm \
        gcc \
        dkms \
        make \
        perl \
        vim \
        git \
        openssh \        
        linux-headers \
        python-pip \
        python-setuptools \
        python-virtualenv

pacman -S base-devel --needed --noconfirm

sed -Ei 's/^(#?)(PasswordAuthentication)(\s*no)/\2 yes/' /etc/ssh/sshd_config        
systemctl enable sshd
systemctl start sshd
        
echo "Installerede basis programmer"        
