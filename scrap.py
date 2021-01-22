# -*- coding: utf-8 -*-
#

import sys
import platform
from moduler.fileOperations import fetch_config
import distro

configs = ''
filename = 'config/config.ini'
try:
    configs = fetch_config(filename)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

#installNfsserver(configs)
print(platform.node())
print(platform.machine())
print(platform.uname())
print(distro.info())
