# -*- coding: utf-8 -*-
#
import os
import sys
from moduler.fileOperations import fetch_config
import pwd

configs = ''
filename = 'config/config.ini'
try:
    configs = fetch_config(filename)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

print(pwd.getpwuid(33).pw_name)
