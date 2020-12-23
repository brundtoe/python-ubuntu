# -*- coding: utf-8 -*-import sys
#
# installation af Postman

from moduler.fileOperations import fetch_archive
from moduler.desktopfile import create_desktop_file


def install_postman(configs):
    """
    Installation af Postman til test af REST API
    :param configs: parametre fra config.ini
    :return: void
    """

    # https://www.postman.com/downloads/release-notes
    version = configs['Common']['postman']
    # url = "https://dl.pstmn.io/download/version/${Common:postman}/linux64"
    url = "https://dl.pstmn.io/download/latest/linux64"
    user = configs['Common']['user']
    program = 'Postman'
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    project_path = configs['Common']['project_path']
    create_desktop_file(program, project_path, tmpl, user)


