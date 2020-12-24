# -*- coding: utf-8 -*
#
import sys
import shlex
import subprocess


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
        print(err)
        sys.exit(res.stderr.decode('UTF-8'))
    print(res.stdout.decode('UTF-8'))
