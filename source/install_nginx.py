#!../venv/bin/python
# Installation og konfiguration af Nginx med php-fpm

import sys, os
import subprocess
from moduler.fileOperations import fetch_config
from moduler.install_programs import install_program, is_installed
from jinja2 import Environment, FileSystemLoader

def install_nginx(configs):
    try:
        program = 'nginx'
        options = configs['Common']['install_options']
        if not is_installed('nginx'):
            res = install_program(program, options)
            if not res:
                sys.exit(f'Installation af {program} er fejlet')
    except Exception as err:
        print(err)
        sys.exit('Kan ikke installere Nginx')

    try:
        tmpl = 'nginx-ubuntu.jinja'
        php_version = configs['Common']['php-version']
        program = 'nginx'
        create_site_config(program, tmpl, php_version)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke opdatere definitionen af nginx default site')

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



def create_site_config(program, tmpl, php_version):
    try:
        file_loader = FileSystemLoader('../templates')
        env = Environment(loader=file_loader)
        template = env.get_template(tmpl)
        outfile = '/etc/nginx/sites-available/default'
        output = template.render(php_version=php_version)
        # print(output)
        with open(outfile, 'wt') as fout:
            fout.write(output)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke generere desktopfile for {program}')

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Installation og konfiguration af Nginx med PHP-FPM')
    configs = fetch_config('../config/config.ini')
    install_nginx(configs)
