# -*- coding: utf-8 -*-
#
# Installation af MySQL
#

import os
import sys
import shlex
from subprocess import run
from manjaro.packages import install_program
from moduler.mysql_data import create_db_users


def install_mysql(configs):
    mysql_daemon = 'mariadb'
    mysql_install_db = shlex.split('mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql')

    if not os.path.exists('/usr/lib/systemd/system/mysql.service'):
        print('Installation af MariaDB')
        try:
            print('Installation af MariaDB')
            install_program(mysql_daemon)
            run(mysql_install_db)
        except Exception as err:
            print(err)
            sys.exit('Kan ikke installere MariaDB')
        run(['systemctl', 'enable', mysql_daemon])
        run(['systemctl', 'start', mysql_daemon])
    else:
        print('MariaDB er allerede installeret')

    print('Konfigurer userer og databaser')
    create_db_users(configs)

    print('Afsluttet Installation af MariaDB')
