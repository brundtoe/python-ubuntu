#!/usr/bin/env python3
#
import sys, os, shlex, subprocess
from moduler.fileOperations import fetch_config


def usermod(user, group, options=''):
    """
    Add a user to a group using usermod
    :param user: username
    :param group: groupname
    :param options: options to linux cmd usermod
    :return:
    """
    cmd = shlex.split(f'usermod {options} -G {group} -a {user}')
    res = ''
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode:
            raise Exception
    except Exception as err:
        print()
        sys.exit(res.stderr.decode('UTF-8'))
    print(res.stdout.decode('UTF-8'))


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('scriptet skal udføres med root adgang')

    user = fetch_config('../config/config.ini')['Common']['user']
    usermod(user, 'docker')
    usermod(user, 'vboxusers')
