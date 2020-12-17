#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af nodejs og globale node packages
#

import os
import sys
import shlex
import subprocess
from moduler.apt_update import apt_update
from moduler.install_programs import install_program
from moduler.fileOperations import fetch_config, addLine
from moduler.install_repo import repokey_install

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

try:
    apt_update()
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
else:
    print('apt-get update og apt-get upgrade udført')

config_file = '../config/config.ini'
try:
    configs = fetch_config(config_file)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {config_file} kan ikke læses')
else:
    print(f'Konfigurationsfilen {config_file} er indlæst')

version = configs['Common']['nodejs_release']
distro = configs['Common']['lts_release']
repo_key = "https://deb.nodesource.com/gpgkey/nodesource.gpg.key"
repo_nodejs = f"https://deb.nodesource.com/node_{version} {distro} main"

try:
    repokey_install(repo_key)
    code = f'deb {repo_nodejs}\n'
    source = f'deb-src {repo_nodejs}\n'
    outfile = f'/etc/apt/sources.list.d/nodesource.list'
    addLine(outfile, code)
    addLine(outfile, source)
except Exception as err:
    print('kunne ikke registrere node.js repository')
else:
    print('Installerede node.js repository')

options = configs['Common']['install_options']
try:
    apt_update()
    install_program('nodejs', options)
    programs = "express-generator json-server nodemon pm2"
    cmd = shlex.split(f"npm install -g {programs}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except Exception as err:
    print('Kunne ikke opdatere systemet med nodejs og globalemoduler')
