# -*- coding: utf-8 -*-import sys
#
# installation af FreeFileSync

import shutil
import shlex
import os
import subprocess
import time
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
    down_file = f'/tmp/{filename}'
    user = configs['Common']['user']
    outfile = f'/home/{user}/programs'
    num_tries = 1
    max_tries = 3

    if not os.path.exists(down_file):
        while num_tries <= max_tries:
            curl_cmd = shlex.split(f'curl -L -o "{down_file}" {url}')
            subprocess.run(curl_cmd)
            res = unpack_freefilesync(down_file, outfile)
            if res:
                program = 'FreeFileSync'
                tmpl = f'{program}.jinja'
                project_path = configs['Common']['project_path']
                create_desktop_file(program, project_path, tmpl, user)
                break
            print(f'Download forsøg {num_tries} fejlede')
            time.sleep(10)
            num_tries += 1


def unpack_freefilesync(down_file, outfile):

    try:
        shutil.unpack_archive(down_file, outfile)
    except Exception as err:
        print(err)
        os.remove(down_file)
        return False
    else:
        return True
