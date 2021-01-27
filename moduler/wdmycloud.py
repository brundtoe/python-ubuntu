# -*- coding: utf-8 -*-
#
#
"""
Oprettelse af mount points, credentials og fstab for wdmycloud
"""

import sys
import os
import pwd
import shutil
from string import Template
from moduler.configuration import fetch_config
from moduler.fileOperations import add_line
from moduler.add_mountpoints import add_mountpoints
from moduler.install_programs import install_program


def update_credentials(configs):
    try:
        user = pwd.getpwuid(1000).pw_name
        project_path = configs['Common']['project_path']
        filename_env = f'{project_path}/config/.env_develop'
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
        user = pwd.getpwuid(1000).pw_name
        filename_wdmycloud = configs['Common']['filename_wdmycloud']
        add_mountpoints(user, mount_points)
        update_credentials(configs)
        with open(filename_wdmycloud) as src_file:
            for line in src_file:
                tm = Template(line)
                add_line(filename, tm.substitute(user=user))
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved opdatering af wdmycloud')
