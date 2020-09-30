#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen -env med password til wdmycloud
#
import sys, os, shutil
from moduler.fileOperations import fetch_config
from moduler.apt_update import apt_update
from moduler.install_programs import install_programs

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


try:
    apt_update()
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
else:
    print('apt-get update og apt-get upgrade udført')


try:
    programs = configs['extra.programs']
    options = configs['Common']['install_options']
    install_programs(programs,options)
except Exception as err:
    sys.exit('Der opstod fejl ved installation af ekstra software')
else:
    print('apt-get installation af ekstra software udført')

try:
    srcfile = '../config/mongod.conf'
    dstfile = '/etc/mongod.conf'
    shutil.copy(srcfile,dstfile)
except Exception as err:
    print(err)
    sys.exit(f'Kan ikke kopiere {srcfile} til {dstfile}')
else:
    print('MongoDB konfigurationsfil er kopieret')
print('*' * 50)
print('Installation af ekstra prorgammer er afsluttet')
