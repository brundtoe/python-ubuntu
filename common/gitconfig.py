#!../ven/bin/python
# -*- coding: utf-8 -*-
#
# oprettelse af global git config

import sys
from shutil import copyfile

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
    copyfile('../config/global.gitconfig',f'/home/{user}/.gitconfig')

except Exception as err:
    sys.exit(f' filen /home/{user}/.gitconfig kan ikke oprettes')
else:
    print(f' filen /home/{user}/.gitconfig er opdateret')