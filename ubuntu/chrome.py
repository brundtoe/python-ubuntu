#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Google Chrome
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

# https://www.google.com/linuxrepositories/
# https://www.ubuntuupdates.org/ppa/google_chrome
repo_key = "https://dl.google.com/linux/linux_signing_key.pub"
program = 'google-chrome'
sources_string = "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
try:
    install_repo(repo_key, program, sources_string)
    print(f'{program} repository er installeret')
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')

options = configs['Common']['install_options']
try:
    apt_update()
    install_program('google-chrome-stable', options)
    print(f'{program} installeret')
except Exception as err:
    print(err)
    print(f'Installationen af {program} fejlede')