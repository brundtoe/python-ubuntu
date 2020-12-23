# -*- coding: utf-8 -*-
#
# Installation af Docker
#

import sys
from os import path, chmod

from moduler.apt_update import apt_update
from moduler.download_file import fetch_file
from moduler.groups import usermod
from moduler.install_programs import install_programs
from moduler.install_repo import install_repo


def install_docker(configs):
    if path.exists('/etc/apt/sources.list.d/docker.list'):
        print('Docker er allerede installeret')
        return
    # https://docs.docker.com/install/linux/docker-ce/ubuntu/
    repo_key = "https://download.docker.com/linux/ubuntu/gpg"
    program = "docker"
    lts_release = configs['Common']['lts_release']
    sources_string = f"deb https://download.docker.com/linux/ubuntu {lts_release} stable"

    try:
        install_repo(repo_key, program, sources_string)
    except Exception as err:
        print(err)
        sys.exit(f'{program} repository er ikke installeret')
    else:
        print(f'{program} repository er installeret')

    options = configs['Common']['install_options']
    user = configs['Common']['user']
    try:
        apt_update()
        programs = {'docker-ce': '', 'docker-ce-cli': '', 'containerd.io': ''}
        install_programs(programs, options)
        usermod(user, 'docker')
        print(f'{program} installeret')
    except Exception as err:
        print(err)
        print(f'Installationen af {program} fejlede')

    version = configs['Common']['docker_compose']
    uri = 'https://github.com/docker/compose/releases/download'
    url = f'{uri}/{version}/docker-compose-Linux-x86_64'
    outfile = '/usr/local/bin/docker-compose'
    try:
        fetch_file(url, outfile)
        chmod(outfile, 0o755)
    except Exception as err:
        print(err)
        print('Kan ikke installere docker-compose')
    else:
        print('docker compose er installereet')
