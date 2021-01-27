# -*- coding: utf-8 -*-
#
# installation af Postman
from os import path
import pwd
from moduler.fileOperations import fetch_archive
from moduler.desktopfile import create_desktop_file


def install_postman(configs):
    """
    Installation af Postman til test af REST API
    :param configs: parametre fra config.ini
    :return: void
    """
    print('Installation af Postman')
    # https://www.postman.com/downloads/release-notes
    version = configs['Common']['postman']
    filename = f'Postman-{version}.tar.gz'
    if path.exists(f'/tmp/{filename}'):
        print(f'Postman version {version} er installeret')
        return
    url = f"https://dl.pstmn.io/download/latest/linux"
    user = pwd.getpwuid(1000).pw_name
    program = 'Postman'
    fetch_archive(url, user, program, version, filename=filename)

    tmpl = f'{program}.jinja'
    project_path = configs['Common']['project_path']
    create_desktop_file(program, project_path, tmpl, user)
    print('Afsluttet Installation af Pstman')
