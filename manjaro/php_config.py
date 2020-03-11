#!/usr/bin/env python3
# konfiguration af XDebug og php.ini

import sys, os, shutil, shlex
import subprocess
from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config
from moduler.xdebug_ini import create_xdebug_ini


def config_php(configs):
    print('Konfiguration af php.ini')

    try:
        ini_file = f'/etc/php/php.ini'
        conf = '../config/php_config.ini'
        cmd = shlex.split(f'sed -i -f {conf} {ini_file}')
        res = subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Opdatering af php.ini fejlede')
    else:
        print(f'{ini_file} er opdateret')

    print('konfiguration af XDebug')
    xdebug_host = configs['Common']['xdebug-host']
    dstdir = f'/etc/php/conf.d'
    dstfile = f'{dstdir}/xdebug.ini'
    create_xdebug_ini('xdebug.jinja', dstfile, xdebug_host)


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    try:
        filename = '../config/config.ini'
        configs = fetch_config(filename)
        config_php(configs)
    except Exception as err:
        print('Der opstod fejl ved konfiguration caf php')
        print(err)
        sys.exit(1)
    else:
        print('PHP konfiguration er udført')
