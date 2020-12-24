# -*- coding: utf-8 -*-
# Installation og konfiguration af Nginx med php-fpm

import sys
import subprocess
from moduler.install_programs import install_program, is_installed
from jinja2 import Environment, FileSystemLoader
from moduler.basis_web import copy_web


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
        tmpl = 'nginx-ubuntu.jinja'
        php_version = configs['Common']['php-version']
        create_site_config(tmpl, project_path, php_version)
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


def create_site_config(tmpl, project_path, php_version):
    try:
        file_loader = FileSystemLoader(f'{project_path}/templates')
        env = Environment(loader=file_loader)
        template = env.get_template(tmpl)
        outfile = '/etc/nginx/sites-available/default'
        output = template.render(php_version=php_version)
        # print(output)
        with open(outfile, 'wt') as fout:
            fout.write(output)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke generere default nginx site')
