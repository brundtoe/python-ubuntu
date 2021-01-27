# -*- coding: utf-8 -*-
#
#
import os
import sys
from subprocess import run
from jinja2 import Environment, FileSystemLoader
from manjaro.packages import install_program
from moduler.basis_web import copy_web
from moduler.site_conf_nginx import create_site_config


def install_nginx(configs):
    try:
        install_program('nginx')
        run(['systemctl', 'disable', 'nginx'])
        run(['systemctl', 'stop', 'nginx'])
    except OSError as err:
        print(err)
        print('Kunne ikke installere Nginx')
        return

    server_dir = '/etc/nginx'
    project_path = configs['Common']['project_path']
    templ = 'nginx.conf.jinja'
    app_user = 'http'
    outfile = f'{server_dir}/nginx.conf'
    create_server_conf(project_path, templ, outfile, app_user)

    templ = '000-nginx.jinja'
    site_file = 'default'
    unix_socket = '/var/run/php-fpm/php-fpm.sock'
    create_site_config(project_path, server_dir, templ, site_file, unix_socket)

    doc_root = '/var/www/html'
    create_web_site(configs, doc_root)


def create_server_conf(project_path, templ, outfile, app_user, enable_modules=''):
    file_loader = FileSystemLoader(f'{project_path}/templates')
    env = Environment(loader=file_loader)

    template = env.get_template(templ)
    output = template.render(app_user=app_user, enable_modules=enable_modules)
    # print(output)
    with open(outfile, 'wt') as fout:
        fout.write(output)


def create_web_site(configs, dest):
    if not os.path.exists(f"{dest}"):
        os.makedirs(f"{dest}", 0o755, exist_ok=True)

    try:
        print('Basis website kopieres til /var/www/html')
        copy_web(configs, dest)
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke kopiere basis_web til {dest}')
