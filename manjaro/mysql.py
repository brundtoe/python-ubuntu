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
            run(mysql_install_db)
        except Exception as err:
            print(err)
            sys.exit('Kan ikke installere MariaDB')

    run(['systemctl','enable',mysql_daemon])
    run(['systemctl','start',mysql_daemon])

    create_db_users(configs)

