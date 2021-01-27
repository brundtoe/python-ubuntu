# -*- coding: utf-8 -*-
#
import os
import sys
import subprocess
import shlex
from moduler.fileOperations import fetch_config, add_line
import distro
import platform
from moduler.utilities import update_config

configs = ''
# filename = 'config/config.ini'
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = f'{dir_path}/config/config.ini'
try:
    configs = fetch_config(filename)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

configs['Common']['project_path'] = os.path.dirname(os.path.realpath(__file__))
update_config(configs)
print(configs['Common']['project_path'])
print(configs['Common']['distro'])
print(configs['Common']['release'])
print(configs['Common']['hostname'])
