#!/usr/bin/env python3
# Installation og konfiguration af Apache

import sys, os, shlex
import subprocess
from moduler.fileOperations import fetch_config
from moduler.install_programs import install_programs


def install_apache(configs):
    try:
        version = configs['Common']['php-version']
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
        cmd = shlex.split('sed -i -f ../config/apache2.conf /etc/apache2/apache2.conf')
        subprocess.run(cmd)
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
        phpinfo = '<?php phpinfo();\n'
        dest = '/var/www/html/index.php'
        with open(dest, 'w') as fout:
            fout.write(phpinfo)
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke oprette {dest}')

    try:
        print('Apache genstartes')
        subprocess.run(['systemctl', 'restart', 'apache2'])
    except Exception as err:
        print(err)
        sys.exit('Kan ikke genstarte Apache')


if __name__ == '__main__':
    if os.geteuid() != 0:
       sys.exit('Scriptet skal udføres  med root access')
    print('Installation og konfiguration af Apache med PHP')
    configs = fetch_config('../config/config.ini')
    install_apache(configs)
