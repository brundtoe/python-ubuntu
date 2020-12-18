#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Vagrant plugins

import shlex
from subprocess import run
from moduler.fileOperations import fetch_config


def vagrant_plugins(configs):
    plugins = configs['vagrant.plugins']
    for plugin in plugins:
        try:
            cmd = shlex.split(f'vagrant plugin install {plugins[plugin]}')
            run(cmd)
        except Exception as err:
            print(err)
            print(f'installation af vagrant plugin {plugins[plugin]}')


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    vagrant_plugins(configs)
