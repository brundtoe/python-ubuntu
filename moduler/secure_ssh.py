# -*- coding: utf-8 -*-
#
# secure konfig af ssh server
#
import os
import sys
import shlex
import subprocess
from moduler.fileOperations import add_line


def secure_ssh_server(configs):

    project_path = configs['Common']['project_path']
    regexp_file = f'{project_path}/config/secure_ssh.ini'
    sshd_config_file = '/etc/ssh/sshd_config'
    try:
        print('Secure SSH configuration af /etc/ssh/sshd_config')
        if os.path.exists(regexp_file) and os.path.exists(sshd_config_file):
            cmd = shlex.split(f'sed -Ei -f {regexp_file} {sshd_config_file}')
            subprocess.run(cmd)
            add_line(sshd_config_file, 'Protocol 2')
        else:
            print(f'Kan ikke opdatere {sshd_config_file}')
    except Exception as err:
        print(err)
        sys.exit(f'Exception Kan ikke opdatere {sshd_config_file}')
    else:
        print('Securing ssh server afsluttet')
