#!../venv/bin/python
#
# Installation af Vagrant
#
import sys,os
from moduler.fileOperations import fetch_config, install_dpkg

if __name__ == '__main__':
    if os.geteuid() != 0:
       sys.exit('Script skal udføres med root access')
    configs = fetch_config('../config/config.ini')
    # https://www.vagrantup.com/downloads.html
    version = configs['Common']['vagrant']
    url = f"https://releases.hashicorp.com/vagrant/{version}/vagrant_{version}_x86_64.deb"
    print(url, version)
    install_dpkg(url, version)