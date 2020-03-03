#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen -env med password til wdmycloud
#
import sys, os
from moduler.fileOperations import fetch_config

configs = ''

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

try:
    filename = '../config/config.ini'
    configs = fetch_config(filename)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

from moduler.install_repo import install_repo
try:
    url = configs['mongodb.org']['repo_key']
    program = 'mongodb'
    content = configs['mongodb.org']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

try:
    url = configs['virtualbox.org']['repo_key']
    program = 'virtualbox'
    content = configs['virtualbox.org']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

try:
    url = configs['docker.com']['repo_key']
    program = 'docker'
    content = configs['docker.com']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

try:
    configs = fetch_config('../config/config.ini')
    url = configs['google.chrome']['repo_key']
    program = 'google-chrome'
    content = configs['google.chrome']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

from moduler.puppet_repo_install import puppet_repo
try:
    url = configs['puppetlabs.com']['repo']
    puppet_repo(url)
except Exception as err:
    print('Puppet repository er ikke installeret',err)
    sys.exit(1)
else:
    print('Puppet repository er installeret')

from moduler.nodejs_repo_install import nodejs_repo
try:
    url = configs['nodejs.org']['repo']
    nodejs_repo(url)
except Exception as err:
    print('Node.js repository er ikke installeret',err)
    sys.exit(1)
else:
    print('Node.js repository er installeret')

print('*' * 50)
print('Registrering af repositories er afsluttet')