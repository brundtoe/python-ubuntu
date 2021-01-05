# -*- coding: utf-8 -*-
#
# Installation af MySQL
#

import os
import sys
import shlex
import shutil
from subprocess import run, Popen, PIPE
from moduler.fileOperations import fetch_config, add_line
from manjaro.packages import install_program
from common.mysql_data import create_db_users


def install_mysql(configs):

    user = configs['Common']['user']
    project_path = configs['Common']['project_path']
    mysql_daemon = 'mariadb'
    mysql_server_config_file = '/etc/my.cnf.d/server.cnf'
    mysql_install_db = shlex.split('mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql')


    if os.path.exists('/usr/lib/systemd/system/mysql.service'):
        print('MariaDB er allerede installeret')
    else:
        try:
            print('Installation af MariaDB')
            install_program('mariadb')
            run(mysql_install_db, shell=True)
            run(['systemctl','enable',mysql_daemon])
        except Exception as err:
            print(err)
            sys.exit('Kan ikke installere MariaDB')

    try:
        add_line(mysql_server_config_file,'default_password_lifetime = 0')
        regexp = 's/\#bind-address.*=.*/bind-address = 0.0.0.0/'
        cmd = shlex.split(f"sed -i '{regexp}' {mysql_server_config_file}")
        run(cmd)
    except OSError as err:
        print(f'Opdatering af {mysql_server_config_file} fejlede')

    run(['systemctl','start',mysql_daemon])
    env_config = fetch_config(f'{project_path}/config/.env_develop')
    mysql_passwd = env_config['Common']['mysql_passwd']
    print(f'Mysql secure installation med {mysql_passwd}')
    run(['mariadb-secure-installation'], shell=True)
    run(['systemctl','restart',mysql_daemon])
    return
    sql_file = f'{project_path}/config/mysql_secure.sql'
    try:
        env_config = fetch_config(f'{project_path}/config/.env_develop')
        mysql_passwd = env_config['Common']['mysql_passwd']
        with open(sql_file) as file:
            proc = Popen(f'mysql -u root -p{mysql_passwd}', shell=True, stdin=file,
                         stdout=PIPE, stderr=PIPE, universal_newlines=True)
            proc.communicate()
    except OSError as err:
        print(err)

    