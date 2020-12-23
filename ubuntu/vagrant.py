# -*- coding: utf-8 -*-import sys
#
# Installation af Vagrant
#
from moduler.fileOperations import fetch_config, install_dpkg
from moduler.vagrant_plugin import vagrant_plugins


def install_vagrant(configs):

    # https://www.vagrantup.com/downloads.html
    version = configs['Common']['vagrant']
    url = f"https://releases.hashicorp.com/vagrant/{version}/vagrant_{version}_x86_64.deb"
    print(url, version)
    install_dpkg(url, version)

    vagrant_plugins(configs)

