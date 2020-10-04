#!../venv/bin/python
# Installation og konfiguration af Apache

import sys, os, shlex
import subprocess

from moduler.fileOperations import fetch_config, isFound, addLine
from moduler.smbcredentials import smbcredentials
from moduler.add_mountpoints import add_mountpoints

# Opdater smbcredentials med password til wdmycloud
def update_credentials(configs):
    try:
        user = configs['Common']['user']
        filename = '../config/.env_develop'
        password = fetch_config(filename)['Common']['password']
        smbcredentials(user, password)
    except Exception as err:
        sys.exit('Der opstod fejl ved opdatering af ~/.smbcredentials')
    else:
        print('~/.smbcredentials er opdateret med mountpoint')

def update_fstab(configs, filename):
    try:
        mount_points = configs['mount.points']
        user = configs['Common']['user']
        filename_wdmycloud = configs['Common']['filename_wdmycloud']
        add_mountpoints(user, mount_points)
        update_credentials(configs)

        with open(filename_wdmycloud) as src_file:
            for line in src_file:
                addLine(filename, line)
    except Exception as err:
        sys.exit('Der opstod fejl ved opdatering af wdmycloud')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Konfiguration af wdmycloud')
    configs = fetch_config('../config/config.ini')
    filename = '/etc/fstab'
    update_fstab(configs, filename)
