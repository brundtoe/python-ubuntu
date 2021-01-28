# -*- coding: utf-8 -*-
#
# installation af jetBrains ToolBox
from os import path
import pwd
from moduler.fileOperations import fetch_archive
from moduler.desktopfile import create_desktop_file


def install_jetbrains_toolbox(configs):
    """
    Installation af JetBrains Toolbox
    :param configs: parametre fra configpaser config/config.ini
    :return: void
    """
    # https://www.jetbrains.com/toolbox-app/download/download-thanks.html?platform=linux

    version = configs['Common']['jetbrains-toolbox']
    program_folder = f'jetbrains-toolbox-{version}'
    down_file = f'{program_folder}.tar.gz'
    user = pwd.getpwuid(1000).pw_name
    if path.exists(f'/home/{user}/programs/{program_folder}'):
        print('JetBrains toolbox er allerede installeret')
        return
    print('Installation af JetBrains ToolBox')
    url = f"https://download.jetbrains.com/toolbox/{down_file}"
    # sha256 = "https://download.jetbrains.com/toolbox/jetbrains-toolbox-{version}.tar.gz.sha256"
    program = 'JetBrains Toolbox'

    fetch_archive(url, user, program, version)

    program = 'JetBrains'
    tmpl = f'{program}.jinja'
    project_path = configs['Common']['project_path']
    create_desktop_file(program, project_path, tmpl, user)
    print('Afsluttet Installation af JetBrains ToolBox')
