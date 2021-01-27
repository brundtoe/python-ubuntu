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

    print('Installation af JetBrains ToolBox')
    version = configs['Common']['jetbrains-toolbox']
    down_file = f'jetbrains-toolbox-{version}.tar.gz'
    if path.exists(f'/tmp/{down_file}'):
        print('JetBrains toolbox er installeret')
        return
    url = f"https://download.jetbrains.com/toolbox/{down_file}"
    # sha256 = "https://download.jetbrains.com/toolbox/jetbrains-toolbox-{version}.tar.gz.sha256"
    user = pwd.getpwuid(1000).pw_name
    program = 'JetBrains Toolbox'

    fetch_archive(url, user, program, version)

    program = 'JetBrains'
    tmpl = f'{program}.jinja'
    project_path = configs['Common']['project_path']
    create_desktop_file(program, project_path, tmpl, user)
    print('Afsluttet Installation af JetBrains ToolBox')
