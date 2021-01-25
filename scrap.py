# -*- coding: utf-8 -*-
#
import os
import sys
import subprocess
import shlex
from moduler.fileOperations import fetch_config, add_line
import distro

configs = ''
#filename = 'config/config.ini'
filename = '/home/projects/sourcecode/python-demo/config/config.ini'
try:
    configs = fetch_config(filename)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

distrib = distro.linux_distribution()
print(distrib)
print(distrib[2].lower())
