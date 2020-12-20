#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
import shlex
import subprocess
from moduler.fileOperations import fetch_config, addLine
from jinja2 import Environment, FileSystemLoader
from moduler.apt_update import apt_update
from moduler.install_programs import install_program


def my_cnf_exists(configs):
    my_cnf_file = f'/home/{configs["Common"]["user"]}/.my.cnf'
    if os.path.exists(my_cnf_file):
        return True
    else:
        return False


def root_my_cnf(passwd):
    cnf = f"""[client]
user = homestead
password = {passwd}
host = localhost

[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_bin
"""
    outfile = '/root/.my.cnf'
    with open(outfile, 'wt') as fout:
        fout.write(cnf)


def user_my_cnf(user):
    cnf = """[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_bin
"""
    outfile = f'/home/{user}/.my.cnf'
    with open(outfile, 'wt') as fout:
        fout.write(cnf)


def create_db_user(configs, path, mysql_passwd):
    print('Opdaterer mysql users')
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    template = env.get_template('mysql_users.jinja')
    output = template.render(mysql_passwd=mysql_passwd)
    outfile = f'{path}/mysql_setup.sql'
    with open(outfile, 'wt') as fout:
        fout.write(output)
    cmd = shlex.split(f'sudo mysql -uroot -p{mysql_passwd} mysql < {outfile}')
    subprocess.run(cmd)

def secure_installation():
    try:
        cmd = shlex.split(f'./mysql_secure.sh')
        subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke udføre MySQL Secure installation')


if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

config_file = '../config/config.ini'
try:
    configs = fetch_config(config_file)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {config_file} kan ikke læses')
else:
    print(f'Konfigurationsfilen {config_file} er indlæst')

try:
    if not my_cnf_exists(configs):
        print('Installation af mysql')
        apt_update()
        options = configs['Common']['install_options']
        install_program('mysql-server', options )
        install_program('libmysqlclient', options)
except Exception as err:
    print(err)
    sys.exit('Kan ikke installere mysql')

try:
    if not my_cnf_exists(configs):
        print('mysql secure installation')
        secure_installation()
except Exception as err:
    print(err)
    print('Kan ikke udføre secure installation')

filename_env = '../config/.env_develop'
mysql_passwd = fetch_config(filename_env)['Common']['mysql_passwd']
path = os.path.dirname(__file__)
try:
    #    if not my_cnf_exists(configs):
    print('Bruger- og databaseoprettelse')
    create_db_user(configs, path, mysql_passwd)
except Exception as err:
    print(err)
    sys.exit('Kan ikke opdatere mysql users')

try:
    if not my_cnf_exists(configs):
        print('Opdatering af my.cnf')
        root_my_cnf(mysql_passwd)
        user = configs['Common']['user']
        user_my_cnf(user)
except Exception as err:
    print(err)
    sys.exit('Kan ikke konfigurere MySQL')

print('mysql installeret')