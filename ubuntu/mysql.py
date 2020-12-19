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
    print('Installation af mysql')
    apt_update()
    options = configs['Common']['install_options']
    install_program('mysql-server', options )
    install_program('libmysqlclient', options)
except Exception as err:
    print(err)
    sys.exit('Kan ikke installere mysql')

try:
    print('MySQL Secure installation .........')
    #full_path = '/home/projects/sourcecode/python-ubuntu/ubuntu'
    cmd = shlex.split(f'./mysql_secure.sh')
    subprocess.run(cmd)
    print('MySQL Secure installation afsluttet')
except Exception as err:
    print(err)
    sys.exit('Kan ikke udføre MySQL Secure installation')

filename_env = '../config/.env_develop'
mysql_passwd = fetch_config(filename_env)['Common']['mysql_passwd']
try:
    print("Configure MySQL Password Lifetime")
    mysqld_conf_file = '/etc/mysql/mysql.conf.d/mysqld.cnf'
    addLine(mysqld_conf_file, 'default_password_lifetime = 0')
    print('Remote login disabled')
    bind_address = "sed -i '/^bind-address/s/bind-address.*=.*/bind-address = 0.0.0.0/'"
    cmd = shlex.split(f'{bind_address} {mysqld_conf_file}')
    subprocess.run(cmd)
    print('Update mycnf')
    root_my_cnf(mysql_passwd)
    user = configs['Common']['user']
    user_my_cnf(user)
except Exception as err:
    print(err)
    sys.exit('Kan ikke konfigurere MySQL')

path = os.path.dirname(__file__)
try:
    print('Opdaterer mysql users')
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)
    template = env.get_template('mysql_users.jinja')
    output = template.render(mysql_passwd=mysql_passwd)
    #print(output)
    outfile = f'{path}/mysql_setup.sql'
    with open(outfile, 'wt') as fout:
        fout.write(output)
    #cmd = shlex.split('sudo mysql -uroot mysql < mysql_setup.sql')
    #subprocess.run(cmd)
    #os.remove(outfile)
except Exception as err:
    print(err)
    sys.exit('Kan ikke opdatere mysql users')


print('mysql installeret')