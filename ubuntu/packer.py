# -*- coding: utf-8 -*-
#
# installation af Packer
import re
import shlex
from os import chown, chmod
from shutil import move
from subprocess import run, PIPE

from moduler.fileOperations import fetch_archive


def install_packer(configs):
    """
    Installation af Packer til opbygning af vagrant bokse med chef/bento
    :param configs: parametre fra config.ini
    :return: void
    """
    # https://packer.io/
    version = configs['Common']['packer']
    url = f"https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_amd64.zip"
    user = configs['Common']['user']
    program = 'Packer'
    findes = None
    packer_file = f'/home/{user}/.local/bin/packer'
    try:
        cmd = shlex.split(f'{packer_file} -v')
        res = run(cmd, stdout=PIPE, stderr=PIPE)
    except Exception as err:
        print(err)
        print('Packer skal installeres')
    else:
        findes = re.search(version, res.stdout.decode('UTF-8'))
    if findes is None:
        fetch_archive(url, user, program, version, 'zip')
        move(f'/home/{user}/programs/packer', packer_file)
        chown(packer_file, 1000, 1000)
        chmod(packer_file, 0o755)
        print('Packer er installeret')
    else:
        print('Packer er allerede installeret')
