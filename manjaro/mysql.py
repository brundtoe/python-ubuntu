# -*- coding: utf-8 -*-
#
# Installation af MySQL
#

import os
import sys
import shlex
import shutil
import subprocess
from moduler.fileOperations import fetch_config, add_line
from manjaro.packages import install_program
from common.mysql_data import create_db_users


def install_mysql(configs):
    user = configs['Common']['user']
    project_path = configs['Common']['project_path']
    mysql_daemon = 'mariadb'
    mysql_server_config_file = '/etc/my.cnf.d/server.cnf'
    mysql_install_db = shlex.split('mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql')


    if os.path.exists('/usr/lib/systemd/system/mysql.service'):
        print('MariaDB er allerede installeret')
    else:
        try:
            print('Installation af MariaDB')
            install_program('mariadb')
            subprocess.run(mysql_install_db)
            subprocess.run(['systemctl','enable',mysql_daemon])
        except Exception as err:
            print(err)
            sys.exit('Kan ikke installere MariaDB')

    try:
        add_line(mysql_server_config_file,'default_password_lifetime = 0')
        regexp = 's/\#bind-address.*=.*/bind-address = 0.0.0.0/'
        cmd = shlex.split(f"sed -i '{regexp}' {mysql_server_config_file}")
        subprocess.run(cmd)
    except OSError as err:
        print(f'Opdatering af {mysql_server_config_file} fejlede')

    subprocess.run(['systemctl','start',mysql_daemon])

