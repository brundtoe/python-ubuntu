#!../venv/bin/python
#
# installation af FreeFileSync

from moduler.fileOperations import fetch_config, fetch_archive
from moduler.desktopfile import create_desktop_file

def install_freefilesync(configs):
    """
    Installation af FreeFileSync
    :param configs: configparser fra config/config.ini
    :return: void
    """
    # https://freefilesync.org/download.php
    version = configs['Common']['freefilesync']
    url = f"https://freefilesync.org/download/FreeFileSync_{version}_Linux.tar.gz"
    user = configs['Common']['user']
    program = 'FreeFileSync'
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)

if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_freefilesync(configs)
