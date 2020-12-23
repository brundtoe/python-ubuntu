# -*- coding: utf-8 -*-import sys
#
# installation af FreeFileSync

import shutil
import shlex
import os
import subprocess

from moduler.desktopfile import create_desktop_file


def install_freefilesync(configs):
    """
    Installation af FreeFileSync
    :param configs: configparser fra config/config.ini
    :return: void
    """
    # https://freefilesync.org/download.php
    version = configs['Common']['freefilesync']
    filename = f"FreeFileSync_{version}_Linux.tar.gz"
    url = f"https://freefilesync.org/download/{filename}"
    user = configs['Common']['user']
    program = 'FreeFileSync'
    down_file = f'/tmp/{filename}'
    if not os.path.exists(down_file):
        cmd = shlex.split(f'curl -L -o "{down_file}" {url}')
        subprocess.run(cmd)
    unpackedfile = f'/home/{user}/programs'
    shutil.unpack_archive(f'/tmp/{filename}', unpackedfile)

    tmpl = f'{program}.jinja'
    project_path = configs['Common']['path']
    create_desktop_file(program, project_path, tmpl, user)


