# -*- coding: utf-8 -*-
# Installation af smartgit
#
from os import path
import pwd
from moduler.fileOperations import fetch_archive
from moduler.desktopfile import create_desktop_file


def install_smartgit(configs):
    """
    Installation af SmartGit
    Forudsætter installation af gtk2
    :param configs: parametre fra config.ini
    :return: void
    """
    # https://www.syntevo.com/smartgit/download/
    version = configs['Common']['smartgit']
    filename = f'smartgit-linux-{version}.tar.gz'
    if path.exists(f'/tmp/{filename}'):
        print(f'SmartGit version {version} er installet')
        return
    # url_deb = f"https://www.syntevo.com/downloads/smartgit/smartgit-{version}.deb"
    url = f"https://www.syntevo.com/downloads/smartgit/{filename}"
    user = pwd.getpwuid(1000).pw_name
    program = 'SmartGit'
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    project_path = configs['Common']['project_path']
    create_desktop_file(program, project_path, tmpl, user)
