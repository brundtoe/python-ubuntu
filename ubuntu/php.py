# -*- coding: utf-8 -*-
# Installation af Composer, konfiguration af XDebug

import sys
import os
import pwd
import shutil
import shlex
import subprocess
from moduler.fileOperations import add_line
from moduler.sha256sum import hash_file
from moduler.install_programs import install_programs
from moduler.download_file import fetch_file
from moduler.xdebug_ini import create_xdebug_3_ini


def install_php(configs):
    """
    Installation af PHP og PHP moduler, Composer og konfiguration af XDebug
    :param configs: parametre fra config/config.ini
    :return:
    """
    print('Installation af PHP moduler')
    project_path = configs['Common']['project_path']
    programs = configs['php.install']
    options = configs['Common']['install_options']
    install_programs(programs, options)

    print('Installation af Xdebug version 3')
    xdebug_version = configs['Common']['xdebug_version']
    try:
        update_pecl = shlex.split('pecl channel-update pecl.php.net')
        subprocess.run(update_pecl)
        install_xdebug = shlex.split(f'pecl install xdebug-{xdebug_version}')
        subprocess.run(install_xdebug)
    except OSError as err:
        print(err)
        sys.exit('Installation af xdebug fejlede')

    print('konfiguration af XDebug')
    version = configs['Common']['php-version']
    xdebug_client_host = configs['Common']['xdebug_client_host']
    dstfile = f'/etc/php/{version}/fpm/conf.d/20-xdebug.ini'
    create_xdebug_3_ini('xdebug_3.jinja', project_path, dstfile, xdebug_client_host)

    print('Konfiguration af php.ini')
    php_components = ['cli', 'cgi', 'fpm']
    version = configs['Common']['php-version']
    config_php_ini(php_components, project_path, version)

    print('Konfiguration af php-fpm')
    version = configs['Common']['php-version']
    config_php_fpm(version)

    print('Installation af Composer')
    url = configs['composer']['repo']
    sha256url = configs['composer']['sha256']
    user = pwd.getpwuid(1000).pw_name
    install_composer(url, sha256url, project_path, user)


def install_composer(url, sha256url, project_path, user):
    dest = f'/home/{user}/.local/bin/composer'
    if os.path.exists(dest):
        print('Composer er allerede installeret')
        return
    print('funktionen install_composer er kaldt')
    composerfile = '/tmp/composer'
    try:
        fetch_file(url, composerfile)
        print('composer filen er hentet')
    except Exception as err:
        print('hovsa')
        print(err)
        exit(1)

    # Der skal være to mellemrum før composer.phar
    composer_hash = f'{hash_file(composerfile)}  composer.phar'

    sha256file = '/tmp/composerSha256'
    try:
        fetch_file(sha256url, sha256file)
        with open(sha256file) as fin:
            sha256sum = fin.readline().strip()
    except Exception as err:
        print(err)
        exit(1)
    else:

        if not sha256sum == composer_hash:
            print('Composer.phar er ikke verificeret')
            exit(1)
    try:
        # kopier til /home/{user}/.local/bin

        print(f'Kopierer composer til {dest} ')
        shutil.copy(composerfile, dest)
        os.chmod(dest, 0o755)
        shutil.chown(dest, user, user)
        os.remove(composerfile)
        os.remove(sha256file)
    except Exception as err:
        print(err)
        exit(1)


def config_php_ini(php_components, project_path, version):

    conf = f'{project_path}/config/php_config.ini'
    for component in php_components:
        ini_file = f'/etc/php/{version}/{component}/php.ini'
        print(ini_file)
        try:
            cmd = shlex.split(f'sed -Ei -f {conf} {ini_file}')
            subprocess.run(cmd)
        except Exception as err:
            print(err)
            sys.exit('Opdatering af php.ini fejlede')
        else:
            print(f'{ini_file} er opdateret')


def config_php_fpm(version):
    fpm_pool = f"/etc/php/{version}/fpm/pool.d/www.conf"
    platform = "env[PLATFORM] = VAGRANT"
    add_line(fpm_pool, platform)
    print(f'{fpm_pool} er opdateret')
    cmd = shlex.split(f'systemctl restart php{version}-fpm')
    subprocess.run(cmd)
    print('genstartede php-fpm')
