#!../venv/bin/python
# Installation og konfiguration af Apache

import sys
import os
import shutil
import shlex
import subprocess
from moduler.fileOperations import fetch_config, addLine
from moduler.install_programs import install_programs
from moduler.basis_web import copy_web

def install_apache(configs):
    version = configs['Common']['php-version']
    try:
        programs = configs['apache.install']
        options = configs['Common']['install_options']
        install_programs(programs, options)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke installere Apache')

    try:
        print('Apache rewrite enables')
        subprocess.run(['a2enmod', 'rewrite'])
        subprocess.run(['systemctl', 'restart', 'apache2'])
    except Exception as err:
        print(err)
        sys.exit('Kan ikke enable Apache rewrite')

    try:
        print('Apache konfigureres apache2.conf')
        cmd = shlex.split('sed -i -f ../config/apache2.conf /etc/apache2/apache2.conf')
        subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke opdatere /etc/apache2/apache2.conf')

    try:
        print('Apache konfigureres med PLATFORM=VAGRANT')
        addLine('/etc/apache2/envvars', 'export PLATFORM=VAGRANT')
    except Exception as err:
        print(err)
        sys.exit('Kan ikke opdatere /etc/apache2/envvars')

    dest = '/var/www/html'
    try:
        copy_web(configs, dest)
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke kopiere basis_web til {dest}')

    try:
        print('Apache standses')
        subprocess.run(['systemctl', 'stop', 'apache2'])
    except Exception as err:
        print(err)
        sys.exit('Kan ikke standse Apache')

    try:
        print('Apache disables')
        subprocess.run(['systemctl', 'disable', 'apache2'])
    except Exception as err:
        print(err)
        sys.exit('Kan ikke disable Apache')


if __name__ == '__main__':
    if os.geteuid() != 0:
       sys.exit('Scriptet skal udføres  med root access')
    print('Installation og konfiguration af Apache med PHP')
    configs = fetch_config('../config/config.ini')
    install_apache(configs)
