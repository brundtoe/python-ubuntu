# -*- coding: utf-8 -*-
"""
MySQL Import af mysql data
"""

import os
import sys
import shlex
import distro
from subprocess import run, PIPE, Popen
from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config


def create_db_users(configs):
    distrib = distro.linux_distribution()[0]
    project_path = configs['Common']['project_path']

    try:
        name_db_active = 'pgrep mysql' if (distrib in ['Ubuntu', 'Debian GNU/Linux']) else 'pgrep mariadb'
        print('name_db_active', name_db_active)
        db_server_active = shlex.split(name_db_active)
        run(db_server_active, check=True)
    except Exception as err:
        print(err)
        sys.exit('Kald af pgrep mysql fejlede - tjek om mariadb kører')

    current_dir = os.getcwd()
    os.chdir('/root')
    run(['mysql_secure_installation'], shell=True)
    os.chdir(current_dir)
    # generer sql script fra en template
    env_config = fetch_config(f'{project_path}/config/.env_develop')
    mysql_passwd = env_config['Common']['mysql_passwd']
    athlon38_passwd = env_config['Common']['athlon38_passwd']

    tmpl = 'mysql_users.jinja'
    sql_file = '/tmp/mysql_data.sql'
    try:
        create_sql_script(project_path, tmpl, sql_file, mysql_passwd, athlon38_passwd)
    except OSError:
        sys.exit(f'Kain ikke generere sql script {sql_file}')

    # opret brugere og databaser
    try:
        with open(sql_file) as file:
            proc = Popen(f'mysql -u root -p{mysql_passwd}', shell=True, stdin=file,
                         stdout=PIPE, stderr=PIPE, universal_newlines=True)
            proc.communicate()

    except Exception as err:
        print(err)
    else:
        print('Mysql bruger og databaser er oprettet')
    finally:
        cmd = shlex.split(f'rm -rf {sql_file}')
        run(cmd)


def create_sql_script(project_path, tmpl, outfile, mysql_passwd, athlon38_passwd):
    try:
        file_loader = FileSystemLoader(f'{project_path}/templates')
        env = Environment(loader=file_loader)

        template = env.get_template(tmpl)

        output = template.render(mysql_passwd=mysql_passwd, athlon38_passwd=athlon38_passwd)
        # print(output)
        with open(outfile, 'wt') as fout:
            fout.write(output)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke generere mysql script {tmpl}')
