#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
import shutil
import shlex
from subprocess import run
from moduler.fileOperations import fetch_config
from moduler.download_file import fetch_file
from moduler.sha256sum import hash_file


def install_composer(url, sha256url, user):
    composerfile = '../outfile/composer'
    try:
        fetch_file(url, composerfile)
    except Exception as err:
        print(err)
        exit(1)
    else:
        # Der skal være to mellemrum før composer.phar
        composer_hash = f'{hash_file(composerfile)}  composer.phar'

    sha256file = '../outfile/composerSha256'
    sha256sum = ''
    try:
        fetch_file(sha256url, sha256file)
        with open(sha256file) as fin:
            sha256sum = fin.readline().strip()
    except Exception as err:
        print(err)
        exit(1)
    else:

        if not sha256sum == composer_hash:
            print('Composer.phar er ikke verificeret')
            exit(1)

    ## kopier til /home/{user}/.local/bin
    dest = f'/home/{user}/.local/bin/composer'
    shutil.copy(composerfile, dest)
    os.chmod(dest, 0o755)
    shutil.chown(dest, user, user)


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../config/config.ini'
    configs = fetch_config(filename)

    print('Installation af Composer')
    url = configs['composer']['repo']
    sha256url = configs['composer']['sha256']
    user = configs['Common']['user']
    install_composer(url, sha256url, user)

