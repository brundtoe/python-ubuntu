#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
import shutil
from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config


def city_files(configs, path):
    try:
        print('generering af cities.html')
        #path = os.path.dirname(__file__)
        #print(path)
        file_loader = FileSystemLoader('../templates')
        env = Environment(loader=file_loader)

        template = env.get_template('cities.jinja')
        inventory_hostname = configs['Common']['host']
        cities = ['Randers', 'Holstebro', 'Jyllinge', 'Roskilde', 'Holbæk']
        output = template.render(cities=cities, inventory_hostname=inventory_hostname)
        # print(output)
        outfile = f'{path}/web/cities.html'
        with open(outfile, 'wt') as fout:
            fout.write(output)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke generere cities.html')


def copy_web(configs, dest):
    path = os.path.dirname(__file__)
    try:
        city_files(configs, path)
        shutil.copytree(f'{path}/web', dest, dirs_exist_ok=True)
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke kopiere til {dest}')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Generering af website cities.html')
    configs = fetch_config('../config/config.ini')
    copy_web(configs)
