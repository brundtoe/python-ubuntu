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
    url = configs['freefilesync.org']['url']
    user = configs['Common']['user']
    program = 'FreeFileSync'
    version = configs['Common']['freefilesync']
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_freefilesync(configs)
