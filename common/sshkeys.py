# -*- coding: utf-8 -*-
# script som opretter en default ssh key for user,
# hvis den ikke allerede eksisterer
# 

import sys
import os
import shutil
import pwd
from subprocess import run
from moduler.utilities import change_owner


def create_sshkeys(configs):
    user = pwd.getpwuid(1000).pw_name
    distrib = configs['Common']['distro']
    ssh_dir = f'/home/{user}/.ssh'
    try:
        if not os.path.exists(ssh_dir):
            os.mkdir(ssh_dir)
            shutil.chown(ssh_dir, user)
            print(f'Oprettede mappen /home/{user}/.ssh')
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke oprette /home/{user}/.ssh')

    if os.path.exists(f'/home/{user}/.ssh/id_rsa'):
        print('key eksisterer')
    else:
        os.chdir(f'/home/{user}/.ssh')
        run('ssh-keygen', shell=True, check=True)
        change_owner(ssh_dir, user, user)
        os.chmod(f'{ssh_dir}/id_rsa', 0o600)
        os.chmod(f'{ssh_dir}/id_rsa.pub', 0o644)
        if distrib in ['arch', 'manjaro']:
            run('eval $(ssh-agent)', shell=True, check=True)
        output = run(['ssh-add', 'id_rsa'])
        print(output)
    print('afsluttet oprettelse af ssh key')
