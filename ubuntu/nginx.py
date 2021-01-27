# -*- coding: utf-8 -*-
# Installation og konfiguration af Nginx med php-fpm

import sys
import subprocess
from moduler.install_programs import install_program, is_installed
from moduler.basis_web import copy_web
from moduler.site_conf_nginx import create_site_config


def install_nginx(configs):
    print('Installation af nginx')
    project_path = configs['Common']['project_path']
    options = configs['Common']['install_options']
    program = 'nginx'
    try:
        if not is_installed(program):
            res = install_program(program, options)
            if not res:
                sys.exit(f'Installation af {program} er fejlet')
    except Exception as err:
        print(err)
        sys.exit('Kan ikke installere Nginx')

    try:
        tmpl = '000-nginx.jinja'
        server_dir = '/etc/nginx'
        php_version = configs['Common']['php-version']
        site_file = 'default'
        unix_socket = f'/var/run/php/php{php_version}-fpm.sock'
        create_site_config(project_path, server_dir, tmpl, site_file, unix_socket)

    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke opdatere definitionen af nginx default site')

    dest = '/var/www/html'
    try:
        print('Basis website kopieres til /var/www/html')
        copy_web(configs, dest)
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke kopiere basis_web til {dest}')

    try:
        print('Nginx disables')
        subprocess.run(['systemctl', 'disable', 'nginx'])
    except Exception as err:
        print(err)
        sys.exit('Kan ikke disable Nginx')

    try:
        print('Nginx standses')
        subprocess.run(['systemctl', 'stop', 'nginx'])
    except Exception as err:
        print(err)
        sys.exit('Kan ikke standse Nginx')
