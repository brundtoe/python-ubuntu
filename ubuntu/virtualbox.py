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
from moduler.groups import usermod

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

config_file = '../config/config.ini'
try:
    configs = fetch_config(config_file)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {config_file} kan ikke læses')
else:
    print(f'Konfigurationsfilen {config_file} er indlæst')

# lsb_release er første del af release navnet *lsb_release -sc*
vbox_lts_release = configs['Common']['vbox_lts_release']
sources_string = f"deb http://download.virtualbox.org/virtualbox/debian {vbox_lts_release} contrib"

try:
    repo_key = "https://www.virtualbox.org/download/oracle_vbox_2016.asc"
    program = 'virtualbox'
    install_repo(repo_key, program, sources_string)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

options = configs['Common']['install_options']
vbox_version = configs['Common']['vbox_version']
user = configs['Common']['user']
try:
    apt_update()
    install_program(f'virtualbox-{vbox_version}', options)
    usermod(user, 'vboxuser')
    print('Installation af Virtualbox er afsluttet')
except Exception as err:
    print('Kunne ikke opdatere systemet med Virtualbox')

vbox_ext_pack = configs['Common']['vbox_ext_pack']
ext_pack_filename = f"Oracle_VM_VirtualBox_Extension_Pack-{vbox_ext_pack}.vbox-extpack"
extention_pack = f"https://download.virtualbox.org/virtualbox/{vbox_ext_pack}/{ext_pack_filename}"

dest = f'/home/{user}/Downloads/{ext_pack_filename}'
try:
    fetch_file(extention_pack, dest)
    print('Virtualbox Extension pack er downloaded')
    os.chmod(f'{dest}', 0o755)
    cmd = shlex.split(f'VBoxManage extpack install {dest}')
    run(cmd)
    print('Virtualbox extension pack er installeret')
except Exception as err:
    print(err)
    print('Kunne ikke opdatere systemet med Virtualbox extension pack')
