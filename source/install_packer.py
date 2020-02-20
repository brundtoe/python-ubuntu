#!/usr/bin/env python3
#
# installation af Packer

from moduler.fileOperations import fetch_config, fetch_archive

def install_packer(configs):
    """
    Installation af Packer til opbygning af vagrant bokse med chef/bento
    :param configs: parametre fra config.ini
    :return: void
    """
    url = configs['packer.io']['url']
    user = configs['Common']['user']
    version = configs['Common']['packer']
    program = 'Packer'
    fetch_archive(url,user,program,version,'zip')

if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_packer(configs)
