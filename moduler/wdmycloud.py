#!../venv/bin/python
# -*- coding: utf-8 -*-import sys
"""
Oprettelse af mount points, credentials og fstab for wdmycloud
"""

import sys
import os
import shutil
from string import Template


from moduler.fileOperations import fetch_config, addLine
from moduler.add_mountpoints import add_mountpoints


# Opdater smbcredentials med password til wdmycloud
def update_credentials(configs):
    try:
        user = configs['Common']['user']
        path = configs['Common']['path']
        filename_env = f'{path}/config/.env_develop'
        password = fetch_config(filename_env)['Common']['password']
        text = f'username={user}\npassword={password}\n'
        filename_credentials = f'/home/{user}/.smbcredentials'
        with open(filename_credentials, 'w') as fout:
            fout.write(text)
        shutil.chown(filename_credentials, user, user)
        os.chmod(filename_credentials, 0o600)
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved opdatering af ~/.smbcredentials')
    else:
        print('~/.smbcredentials er opdateret med mountpoint')


def update_wdmycloud(configs):
    filename = '/etc/fstab'
    try:
        mount_points = configs['mount.points']
        user = configs['Common']['user']
        filename_wdmycloud = configs['Common']['filename_wdmycloud']
        add_mountpoints(user, mount_points)
        update_credentials(configs)

        with open(filename_wdmycloud) as src_file:
            for line in src_file:
                tm = Template(line)
                addLine(filename, tm.substitute(user=user))
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved opdatering af wdmycloud')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Konfiguration af wdmycloud')
    configs = fetch_config('../config/config.ini')
    update_wdmycloud(configs)
