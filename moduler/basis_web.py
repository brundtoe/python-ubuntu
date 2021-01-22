# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import sys
import platform
from jinja2 import Environment, FileSystemLoader
from moduler.utilities import copy_dir


def city_files(configs, project_path):
    try:
        print('generering af cities.html')
        file_loader = FileSystemLoader(f'{project_path}/templates')
        env = Environment(loader=file_loader)

        template = env.get_template('cities.jinja')
        inventory_hostname = configs['Common']['host']
        cities = ['Randers', 'Holstebro', 'Jyllinge', 'Roskilde', 'Holbæk']
        output = template.render(cities=cities, inventory_hostname=inventory_hostname)
        # print(output)
        outfile = '/var/www/html/cities.html'
        with open(outfile, 'wt') as fout:
            fout.write(output)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke generere cities.html')


def copy_web(configs,  dest):
    project_path = configs['Common']['project_path']
    try:
        city_files(configs, project_path)
        copy_dir(f'{project_path}/assets/web', dest, 'root')
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke kopiere til {dest}')
