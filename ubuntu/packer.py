# -*- coding: utf-8 -*-import sys
#
# installation af Packer
from os import chown
from shutil import move
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
    fetch_archive(url, user, program, version, 'zip')
    move(f'/home/{user}/programs/packer', f'/home/{user}/.local/bin/packer')
    chown(f'/home/{user}/.local/bin/packer', 1000, 1000)


