# -*- coding: utf-8 -*-
#
#
import os
import sys
import shlex
import shutil
import subprocess
from moduler.basis_web import copy_web
from moduler.fileOperations import add_line
from jinja2 import Environment, FileSystemLoader


def install_apache(configs):
    project_path = configs['Common']['project_path']
    try:
        cmd = shlex.split('pacman -Syu --noconfirm')
        subprocess.run(cmd)
    except OSError as err:
        print(err)
        sys.exit('Systemopdatering fejlede')

    try:
        cmd = shlex.split('pacman -S --noconfirm apache')
        subprocess.run(cmd)
        # cmd = shlex.split(systemctl disable httpd)
        # cmd = shlex.split(systemctl stop httpd)
        subprocess.run(['systemctl', 'disable', 'httpd'])
        subprocess.run(['systemctl', 'stop', 'httpd'])
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved installation af Apache http webserver')
    else:
        print('pacman installation af Apache http webserver udført')

    apache_dir = "/etc/httpd"
    apache_conf = f"{apache_dir}/conf/httpd.conf"

    config_httpd(project_path, apache_dir, apache_conf)

    if not os.path.exists(f"{apache_dir}/sites-available"):
        os.makedirs(f"{apache_dir}/sites-available",  0o755, exist_ok=True)

    if not os.path.exists(f"{apache_dir}/sites-enabled"):
        os.makedirs(f"{apache_dir}/sites-enabled",  0o755, exist_ok=True)

    create_site_conf(project_path, apache_dir, 'httpd')

    dest = '/var/www/html'
    if not os.path.exists(f"{dest}"):
        os.makedirs(f"{dest}",  0o755, exist_ok=True)

    try:
        print('Basis website kopieres til /var/www/html')
        copy_web(configs, dest)
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke kopiere basis_web til {dest}')


def config_httpd(project_path, apache_dir, apache_conf):

    conf = f'{project_path}/config/httpd.conf'
    ini_file = '/etc/php/php.ini'
    print(ini_file)
    try:
        cmd = shlex.split(f'sed -i -f {conf} {apache_conf}')
        subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit(f'Opdatering af {apache_conf} fejlede')
    else:
        print(f'{apache_conf} er opdateret')

    src = f"{project_path}/config/php-fpm.conf"
    dest = f"{apache_dir}/conf/extra/php-fpm.conf"
    shutil.copy(src, dest)

    add_line(apache_conf, 'Include conf/extra/php-fpm.conf')
    add_line(apache_conf, 'Include sites-enabled/*.conf')


def create_site_conf(project_path, apache_dir, app_user):

    file_loader = FileSystemLoader(f'{project_path}/templates')
    env = Environment(loader=file_loader)

    template = env.get_template('000-apache.jinja')
    output = template.render(app_user=app_user)
    # print(output)
    outfile = f'{apache_dir}/sites-available/000-default.conf'
    with open(outfile, 'wt') as fout:
        fout.write(output)

    if os.path.exists(f'{apache_dir}/sites-enabled/000-default.conf'):
        os.unlink(f'{apache_dir}/sites-enabled/000-default.conf')
    os.symlink(f'{apache_dir}/sites-available/000-default.conf',
               f'{apache_dir}/sites-enabled/000-default.conf')
