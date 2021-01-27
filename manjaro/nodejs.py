# -*- coding: utf-8 -*-
#
#

import sys
import shlex
import subprocess
from .packages import install_program


def install_nodejs(configs):
    pgm = configs['Common']['nodejs_arch_lts']
    try:
        install_program(pgm)
        install_program('npm')
    except OSError as err:
        print(err)
        sys.exit('Installation af nodejs fejlede')

    node_modules = [
        'express-generator',
        'json-server',
        'nodemon',
        'pm2'
    ]
    for node_module in node_modules:
        try:
            cmd = shlex.split(f'npm -g install {node_module}')
            subprocess.run(cmd)
        except OSError as err:
            print(err)
            sys.exit(f'Kunne ikke installere node modulet {node_module}')
