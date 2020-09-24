#!/usr/bin/env python3
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

if os.path.exists(f'/home/{user}/.ssh/id_rsa'):
    print('key eksisterer')
else:
    os.chdir(f'/home/{user}/.ssh')
    #subprocess.call('ssh-keygen', shell=True)
    subprocess.run('ssh-keygen',input=b"id_rsa\n")
    output = subprocess.run(['ssh-add','id_rsa'])
    print(output)


