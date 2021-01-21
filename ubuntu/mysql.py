# -*- coding: utf-8 -*-
#
# Installation af MySQL
#

import os
import sys
import shlex
import shutil
import subprocess
from moduler.fileOperations import fetch_config
from moduler.apt_update import apt_update
from moduler.install_programs import install_program
from moduler.mysql_data import create_db_users


def install_mysql(configs):
    user = configs['Common']['user']
    project_path = configs['Common']['project_path']
    mysql_daemon = 'mariadb'

    if os.path.exists('/usr/lib/systemd/system/mysql.service'):
        print('MySQL er allerede installeret')
    else:
        try:
            print('Installation af mysql')
            apt_update()
            options = configs['Common']['install_options']
            install_program('mysql-server', options)
            install_program('libmysqlclient', options)
        except Exception as err:
            print(err)
            sys.exit('Kan ikke installere mysql')

    subprocess.run(['systemctl', 'enable', mysql_daemon])
    subprocess.run(['systemctl', 'start', mysql_daemon])

    create_db_users(configs)
