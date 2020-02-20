#!/usr/bin/env python3
#
# installation af FreeFileSync

from moduler.fileOperations import fetch_config, fetch_archive


def install_freefilesync(configs):
    """
    Installation af FreeFileSync
    :param configs: configparser fra config/config.ini
    :return: void
    """
    url = configs['freefilesync.org']['url']
    user = configs['Common']['user']
    program = 'FreeFileSync'
    version = configs['Common']['freefilesync']
    fetch_archive(url, user, program, version)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_freefilesync(configs)
