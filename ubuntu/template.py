#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
import shlex
from subprocess import run
from moduler.fileOperations import fetch_config
from moduler.install_repo import install_repo
from moduler.apt_update import apt_update
from moduler.install_programs import install_program
from moduler.download_file import fetch_file
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

repo_key = f""
program = f""
sources_string = f""
try:
    install_repo(repo_key, program, sources_string)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')




options = configs['Common']['install_options']
try:
    apt_update()
    install_program('', options)
    print(f'{program} installeret')

except Exception as err:
    print(err)
    print(f'Installationen af {program} fejlede')