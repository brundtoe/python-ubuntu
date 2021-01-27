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
from moduler.site_conf_apache import create_site_conf
from moduler.basis_web import create_web_site


def install_apache(configs):
    print('Installation af Http Webserver Apache')
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

    tmpl = '000-apache.jinja'
    create_site_conf(project_path, apache_dir, tmpl, 'httpd')

    doc_root = '/var/www/html'
    create_web_site(configs, doc_root)
    print('Afsluttet Installation af Http Webserver Apache')


def config_httpd(project_path, apache_dir, apache_conf):

    conf = f'{project_path}/config/httpd.conf'
    ini_file = '/etc/php/php.ini'
    print(ini_file)
    try:
        cmd = shlex.split(f'sed -Ei -f {conf} {apache_conf}')
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
