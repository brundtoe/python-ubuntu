#! ../venv/bin/python
"""
MySQL Oprettelse af brugere og databaser samt Import af mysql data
"""

import os, sys, shlex, subprocess
from moduler.fileOperations import fetch_config

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


# tjek at mysqlserver er aktiv
# pgrep mysql hvis stautskoden er != 0 så kører den ikke


sql_file = f'/home/{user}/dumps/mysqlbackup/mystore/mystore_authors.sql'
if not os.path.exists(sql_file):
    sys.exit(f'SQL scriptet: {sql_file} eksisterer ikke')

res = ''
try:
    sql_stmt = f'mysql -u {user} -p < /home/jackie/dumps/mysqlbackup/mystore/mystore_authors.sql;'
    cmd = shlex.split(sql_stmt)
    cmd = f'mysql -u jackie -p < /home/jackie/dumps/mysqlbackup/mystore/mystore_authors.sql;'
    res = subprocess.run(cmd,input=b'aura-73-glf\n')
except Exception as err:
    print(err)
    print(res)
else:
    print(res)
