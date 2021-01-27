# -*- coding: utf-8 -*-
# Installation og konfiguration af Apache

import os
import sys
import shlex
import subprocess
from moduler.fileOperations import add_line
from moduler.install_programs import install_programs
from moduler.basis_web import copy_web
from moduler.site_conf_apache import create_site_conf
from moduler.xdebug_ini import create_xdebug_3_ini


def install_apache(configs):
    print('Installation af Apache Webserver')
    project_path = configs['Common']['project_path']
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
        cmd = shlex.split(f'sed -Ei -f {project_path}/config/apache2.conf /etc/apache2/apache2.conf')
        subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke opdatere /etc/apache2/apache2.conf')

    try:
        print('Apache konfigureres med PLATFORM=VAGRANT')
        add_line('/etc/apache2/envvars', 'export PLATFORM=VAGRANT')
    except Exception as err:
        print(err)
        sys.exit('Kan ikke opdatere /etc/apache2/envvars')

    apache_dir = "/etc/apache2"
    tmpl = '000-apache.jinja'
    create_site_conf(project_path, apache_dir, tmpl, 'apache2')

    print('konfiguration af XDebug')
    version = configs['Common']['php-version']
    php_path = f"/etc/php/{version}"
    xdebug_client_host = configs['Common']['xdebug_client_host']
    dstfile = f'{php_path}/mods-available/xdebug.ini'
    if not os.path.exists(dstfile):
        create_xdebug_3_ini('xdebug_3.jinja', project_path, dstfile, xdebug_client_host)
    if os.path.exists(f'{php_path}/apache2/conf.d/20-xdebug.ini'):
        os.unlink(f'{php_path}/apache2/conf.d/20-xdebug.ini')
    os.symlink(f'{php_path}/mods-available/xdebug.ini',
               f'{php_path}/apache2/conf.d/20-xdebug.ini')

    dest = '/var/www/html'
    print('Basis website kopieres til /var/www/html')
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
    print('Installation af Apache Webserver')