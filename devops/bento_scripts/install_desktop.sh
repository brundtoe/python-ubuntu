#!/usr/bin/env bash -eux

#Installation af programmer med GUI Ubuntu Desktop

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

export DEBIAN_FRONTEND=noninteractive

apt-get update && apt-get upgrade -y

apt-get install -y \
   gparted \
   synaptic \
   samba \
   system-config-samba \
   gnome-system-tools

