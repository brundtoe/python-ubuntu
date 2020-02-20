#!/usr/bin/env python3
#
import sys, os, shlex, subprocess
from moduler.fileOperations import fetch_config


def adduser(user, group):
    """
    add a user to a group
    :param user: user name
    :param group: group name
    :return:
    """
    cmd = shlex.split(f'adduser {user} {group}')
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode:
            raise Exception
    except Exception as err:
        print()
        sys.exit(res.stderr.decode('UTF-8'))
    print(res.stdout.decode('UTF-8'))


def usermod(user, group, options=''):
    """
    Add a user to a group using usermod
    :param user: username
    :param group: groupname
    :param options: options to linux cmd usermod
    :return:
    """
    cmd = shlex.split(f'usermod {options} -G {group} -a {user}')
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
    group = 'docker'
    ##add user to existing group
    adduser(user, 'vboxusers')
    # modificer user 
    usermod(user, group)
