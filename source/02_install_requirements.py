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

from moduler.apt_update import apt_update
try:
    apt_update()
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
else:
    print('apt-get update og apt-get upgrade udført')

from moduler.install_programs import install_programs
try:
    programs = configs['programs']
    options = configs['Common']['install_options']
    install_programs(programs,options)
except Exception as err:
    sys.exit('Der opstod fejl ved installation af base software')
else:
    print('apt-get installation af base software udført')

print('*' * 50)
print('Installation af forudsætninger er udført')
