#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som opretter en default ssh key for user,
# hvis den ikke allerede eksisterer
# 
# Scriptet runnes som alm user

import sys, os
import subprocess
from moduler.fileOperations import fetch_config

configs = ''
user = ''
try:
    filename = '../config/config.ini'
    configs = fetch_config(filename)
    user = configs['Common']['user']
except Exception as err:
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

try:
    sshDir = f'/home/{user}/.ssh'
    if not os.path.exists(sshDir):
        os.mkdir(sshDir)
        print(f'Oprettede mappen /home/{user}/.ssh')
except Exception as err:
    sys.exit(f'Kan ikke oprette /home/{user}/.ssh')


if os.path.exists(f'/home/{user}/.ssh/id_rsa'):
    print('key eksisterer')
else:
    os.chdir(f'/home/{user}/.ssh')
    #subprocess.call('ssh-keygen', shell=True)
    subprocess.run('ssh-keygen',input=b"id_rsa\n\n\n", check=true)
    if configs['Common']['distribution'] == 'manjaro':
        subprocess.run('eval $(ssh-agent)', shell=True, check=True)
    output = subprocess.run(['ssh-add','id_rsa'])
    print(output)


