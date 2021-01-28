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
    print('Installation af SmartGit')
    version = configs['Common']['smartgit']
    filename = f'smartgit-linux-{version}.tar.gz'
    user = pwd.getpwuid(1000).pw_name
    if path.exists(f'/home/{user}/programs/smartgit'):
        print(f'SmartGit version {version} er allerede installet')
        return
    # url_deb = f"https://www.syntevo.com/downloads/smartgit/smartgit-{version}.deb"
    url = f"https://www.syntevo.com/downloads/smartgit/{filename}"
    program = 'SmartGit'
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    project_path = configs['Common']['project_path']
    create_desktop_file(program, project_path, tmpl, user)
    print('Afsluttet Installation af SmartGit')
