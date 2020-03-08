#!/usr/bin/env python3
# konfiguration af XDebug og php.ini

import sys, os, shutil, shlex
import subprocess
from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config


def config_php(configs):
    print('konfiguration af XDebug')
    config_xdebug(configs)
    #
    print('Konfiguration af php.ini')

    try:
        ini_file = f'/etc/php/php.ini'
        conf = '../config/php_manjaro.ini'
        cmd = shlex.split(f'sed -i -f {conf} {ini_file}')
        res = subprocess.run(cmd)
    except Exception as err:
        print(err)
        sys.exit('Opdatering af php.ini fejlede')
    else:
        print(f'{ini_file} er opdateret')


def config_xdebug(configs):
    xdebug_host = configs['Common']['xdebug-host']
    create_xdebug_ini('xdebug.jinja', xdebug_host)

    srcfile = f'../config/xdebug.ini'
    dstdir = f'/etc/php/conf.d'
    dstfile = f'{dstdir}/xdebug.ini'

    try:
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)
        shutil.copyfile(srcfile, dstfile)
    except Exception as err:
        print(err)
        raise Exception


def create_xdebug_ini(tmpl, xdebug_host=True):
    """
    generer Xdebug.ini
    :param tmpl: den anvendte Jinja2 template
    :param xdebug_host: angivelse af om det er en host eller en vagrant maskine
    :return: void
    """
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)

    template = env.get_template(tmpl)

    xdebug_remote = 'xdebug.remote_host=localhost'
    if not xdebug_host:
        xdebug_remote = 'xdebug.remote_connect_back=1'

    outfile = '../config/xdebug.ini'
    output = template.render(xdebug_remote=xdebug_remote)
    print(output)
    with open(outfile, 'wt') as fout:
        fout.write(output)

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    try:
        filename = '../config/config.ini'
        configs = fetch_config(filename)
        config_php(configs)
    except Exception as err:
        print('Der opstod fejl ved konfiguration caf php')
        print(err)
        sys.exit(1)
    else:
        print('PHP konfiguration er udført')
