# -*- coding: utf-8 -*-
#

import sys
import shlex
from subprocess import run
from .packages import install_programs
from moduler.xdebug_ini import create_xdebug_3_ini
from moduler.fileOperations import add_line


def install_php(configs):

    programs = configs['manjaro.php']
    project_path = configs['Common']['project_path']
    try:
        cmd = shlex.split('pacman -Syu --noconfirm')
        run(cmd)
    except OSError as err:
        print(err)
        sys.exit('Systemopdatering fejlede')

    try:
        install_programs(programs)
    except OSError as err:
        print(err)
        print('Der opstod fejl ved installation af php packages software')
        return
    else:
        print('pacman installation af base software udført')

    print('konfiguration af XDebug')
    xdebug_client_host = configs['Common']['xdebug_client_host']
    dstfile = '/etc/php/conf.d/xdebug.ini'
    create_xdebug_3_ini('xdebug_3.jinja', project_path, dstfile, xdebug_client_host)

    config_php_ini(project_path)
    config_php_fpm()


def config_php_ini(project_path):

    conf = f'{project_path}/config/php_manjaro.ini'
    ini_file = '/etc/php/php.ini'
    print(ini_file)
    try:
        cmd = shlex.split(f'sed -Ei -f {conf} {ini_file}')
        run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Opdatering af php.ini fejlede')
    else:
        print(f'{ini_file} er opdateret')


def config_php_fpm():
    fpm_pool = "/etc/php/php-fpm.d/www.conf"
    platform = "env[PLATFORM] = VAGRANT"
    add_line(fpm_pool, platform)
    print(f'{fpm_pool} er opdateret')
    cmd = shlex.split('systemctl restart php-fpm')
    run(cmd)
    print('genstartede php-fpm')
