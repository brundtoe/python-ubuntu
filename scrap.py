# -*- coding: utf-8 -*-
#
import os
import sys
import subprocess
import shlex
from moduler.fileOperations import fetch_config, add_line


configs = ''
filename = 'config/config.ini'
try:
    configs = fetch_config(filename)
except Exception as err:
    print(err)
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')


project_path = configs['Common']['project_path']
config_file = '/etc/ssh/sshd_config'
try:
    print('Secure SSH configuration af /etc/ssh/sshd_config')
    if os.path.exists(config_file):
        cmd = shlex.split(f'sed -Ei -f {project_path}/config/secure_ssh.ini {config_file}')
        print(cmd)
        subprocess.run(cmd)
        add_line(config_file, 'Protocol 2')
    else:
        print(f'Kan ikke opdatere {config_file}')
except Exception as err:
    print(err)
    sys.exit(f'Exception Kan ikke opdatere {config_file}')


