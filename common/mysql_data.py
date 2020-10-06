#! ../venv/bin/python
"""
MySQL Import af mysql data
"""

import os, sys, shlex
from moduler.fileOperations import fetch_config
from subprocess import run, PIPE, Popen
from pathlib import PurePath

configs = ''
user = ''
try:
    filename = '../config/config.ini'
    configs = fetch_config(filename)
    user = configs['Common']['user']
except Exception as err:
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

try:
    db_server_active = shlex.split('pgrep mariadb')
    res = run(db_server_active, check=True)
except Exception as err:
    print(err)
    sys.exit('Kald af pgrep mysql fejlede - tjek om mariadb kører')

filename = '../config/mysql_data'
if not os.path.exists(filename):
    sys.exit(f'SQL scripts: {filename} eksisterer ikke')

try:
    with open(filename) as file:
        proc = Popen('mysql -u jackie -p',shell=True, stdin=file, 
            stdout=PIPE, stderr=PIPE, universal_newlines=True)
        out, err = proc.communicate()
except Exception as err:
    print(err)
    sys.exit('opdatering af mysql data fejlede')
else:
    print('Mysql databasen er opdateret')
