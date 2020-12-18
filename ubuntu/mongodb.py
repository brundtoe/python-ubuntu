#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
from shutil import copyfile
from moduler.fileOperations import fetch_config
from moduler.install_repo import install_repo
from moduler.apt_update import apt_update
from moduler.install_programs import install_program

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

config_file = '../config/config.ini'
try:
    configs = fetch_config(config_file)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {config_file} kan ikke læses')
else:
    print(f'Konfigurationsfilen {config_file} er indlæst')

# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
mongodb_release = configs['Common']['mongodb_release']
lsb_mongodb = configs['Common']['lsb_mongodb']
repo_key = f"https://www.mongodb.org/static/pgp/server-{mongodb_release}.asc"
release = f"{lsb_mongodb}/mongodb-org/{mongodb_release}"
sources_string = f"deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu {release} multiverse"
program = 'mongodb'
try:
    install_repo(repo_key, program, sources_string)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

options = configs['Common']['install_options']
try:
    apt_update()
    install_program('mongodb-org', options)
    print('MongoDB installeret')
    src = "../config/mongod.conf"
    dest = "/etc/mongod.conf"
    copyfile(src, dest)
except Exception as err:
    print(err)
    print('Installationen af MongoDB fejlede')
