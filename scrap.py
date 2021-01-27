# -*- coding: utf-8 -*-
#
import os
import sys
import subprocess
import shlex
import re
import platform
from moduler.configuration import update_config, fetch_config

configs = ''
# filename = 'config/config.ini'
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = f'{dir_path}/config/config.ini'
try:
    configs = fetch_config(filename)
    configs['Common']['project_path'] = os.path.dirname(os.path.realpath(__file__))
    update_config(configs)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

print(configs['Common']['virtualization'])
