# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
import shlex
import shutil
import subprocess
from moduler.fileOperations import fetch_config
from moduler.apt_update import apt_update
from moduler.install_programs import install_program


def install_mysql(configs):
    user = configs['Common']['user']
    path = configs['Common']['path']
    try:
        if not my_cnf_exists(user):
            print('Installation af mysql')
            apt_update()
            options = configs['Common']['install_options']
            install_program('mysql-server', options )
            install_program('libmysqlclient', options)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke installere mysql')

    try:
        if not my_cnf_exists(user):
            print('mysql secure installation')
            secure_installation()
    except Exception as err:
        print(err)
        print('Kan ikke udføre secure installation')

    filename_env = f'{path}/config/.env_develop'
    mysql_passwd = fetch_config(filename_env)['Common']['mysql_passwd']
    try:
        if not my_cnf_exists(user):
            print('Bruger- og databaseoprettelse')
            create_db_user(user, path, mysql_passwd)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke opdatere mysql users')

    print('mysql installeret')


def my_cnf_exists(user):
    my_cnf_file = f'/home/{user}/.my.cnf'
    if os.path.exists(my_cnf_file):
        return True
    else:
        return False


def create_db_user(user, path, mysql_passwd):
    print('Opdaterer mysql users')
    user_script = f'{path}/ubuntu/mysql_setup.sh'
    cmd = shlex.split(f'{user_script} {mysql_passwd} {user}')
    subprocess.run(cmd)
    if my_cnf_exists(user):
        shutil.chown(f'/home/{user}/.my.cnf', user, user)


def secure_installation(path):
    try:
        cmd = shlex.split(f'{path}/ubuntu/mysql_secure.sh')
        subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke udføre MySQL Secure installation')

