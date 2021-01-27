#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
import sys
import os
from moduler.configuration import fetch_config
from moduler.apt_update import apt_update
from moduler.install_programs import install_programs

configs = ''

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

filename = '../config/config.ini'
try:
    configs = fetch_config(filename)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

try:
    apt_update()
except Exception as err:
    print(err)
    sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
else:
    print('apt-get update og apt-get upgrade udført')

try:
    programs = configs['extra.programs']
    options = configs['Common']['install_options']
    install_programs(programs, options)
    install_programs(programs, options)
except Exception as err:
    print(err)
    sys.exit('Der opstod fejl ved installation af ekstra software')
else:
    print('apt-get installation af ekstra software udført')
