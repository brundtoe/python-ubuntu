#!/usr/bin/env bash 

set -e

# kan kun anvendes på Manjaro
#pacman-mirrors --country Germany,France,Denmark,Sweden,Belgium,United_Kingdom
#pacman -Syyu --noconfirm

pacman -Syu --noconfirm \
        gcc \
        dkms \
        make \
        perl \
        vim \
        nfs-utils \
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
