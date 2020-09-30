#!/usr/bin/env python3
#
# installation af FreeFileSync

from fileOperations import fetch_config, fetch_archive
from desktopfile import create_desktop_file

def install_freefilesync(configs):
    """
    Installation af FreeFileSync
    :param configs: configparser fra config/manjaro.ini
    :return: void
    """
    url = configs['freefilesync.org']['url']
    user = configs['Common']['user']
    program = 'FreeFileSync'
    version = configs['Common']['freefilesync']
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)

if __name__ == '__main__':
    configs = fetch_config('../config/manjaro.ini')
    install_freefilesync(configs)
