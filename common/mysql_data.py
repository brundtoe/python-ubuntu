# -*- coding: utf-8 -*-
"""
MySQL Import af mysql data
"""

import os
import sys
import shlex
from subprocess import run, PIPE, Popen


def create_db_users(configs):
    distribution = configs['Common']['distribution']
    project_path = configs['Common']['project_path']

    try:
        name_db_active = 'pgrep mariadb' if (distribution == 'manjaro') else 'pgrep mysql'
        print('name_db_active', name_db_active)
        db_server_active = shlex.split(name_db_active)
        run(db_server_active, check=True)
    except Exception as err:
        print(err)
        sys.exit('Kald af pgrep mysql fejlede - tjek om mariadb kører')

    filename = f'{project_path}/config/mysql_data.sql'
    if not os.path.exists(filename):
        sys.exit(f'SQL scripts: {filename} eksisterer ikke')

    try:
        with open(filename) as file:
            proc = Popen('mysql -u root -p', shell=True, stdin=file,
                         stdout=PIPE, stderr=PIPE, universal_newlines=True)
            proc.communicate()
    except Exception as err:
        print(err)
        sys.exit('opdatering af mysql data fejlede')
    else:
        print('Mysql databasen er opdateret')
