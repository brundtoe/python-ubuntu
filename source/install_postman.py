#!/usr/bin/env python3
#
# installation af Postman

from moduler.fileOperations import fetch_config, fetch_archive


def install_postman(configs):
    """
    Installation af Postman til test af REST API
    :param configs: parametre fra config.ini
    :return: void
    """

    url = configs['postman.com']['url']
    user = configs['Common']['user']
    program = 'Postman'
    version = configs['Common']['postman']
    fetch_archive(url,user,program,version)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_postman(configs)
