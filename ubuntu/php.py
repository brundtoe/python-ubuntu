# -*- coding: utf-8 -*-
# Installation af Composer, konfiguration af XDebug

import sys
import os
import shutil
import shlex
import subprocess
from moduler.fileOperations import addLine
from moduler.sha256sum import hash_file
from moduler.install_programs import install_programs
from moduler.download_file import fetch_file
from moduler.xdebug_ini import create_xdebug_ini


def install_php(configs):
    """
    Installation af PHP og PHP moduler, Composer og konfiguration af XDebug
    :param configs: parametre fra config/config.ini
    :return:
    """
    print('Installation af PHP moduler')
    path = configs['Common']['path']
    programs = configs['php.install']
    options = configs['Common']['install_options']
    install_programs(programs, options)

    print('konfiguration af XDebug')
    version = configs['Common']['php-version']
    xdebug_host = configs['Common']['xdebug-host']
    dstfile = f'/etc/php/{version}/mods-available/xdebug.ini'
    create_xdebug_ini('xdebug.jinja', path, dstfile, xdebug_host)

    print('Konfiguration af php.ini')
    php_components = ['cli', 'cgi', 'fpm']
    version = configs['Common']['php-version']
    config_php_ini(php_components, path, version)

    print('Konfiguration af php-fpm')
    version = configs['Common']['php-version']
    config_php_fpm(version)

    print('Installation af Composer')
    url = configs['composer']['repo']
    sha256url = configs['composer']['sha256']
    user = configs['Common']['user']
    install_composer(url, sha256url, path, user)


def install_composer(url, sha256url, path, user):
    print('funktionen install_composer er kaldt')
    composerfile = f'{path}/outfile/composer'
    try:
        fetch_file(url, composerfile)
        print('composer filen er hentet')
    except Exception as err:
        print('hovsa')
        print(err)
        exit(1)

    # Der skal være to mellemrum før composer.phar
    composer_hash = f'{hash_file(composerfile)}  composer.phar'

    sha256file = f'{path}/outfile/composerSha256'
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
        dest = f'/home/{user}/.local/bin/composer'
        print(f'Kopierer composer til {dest} ')
        shutil.copy(composerfile, dest)
        os.chmod(dest, 0o755)
        shutil.chown(dest, user, user)
        os.remove(composerfile)
        os.remove(sha256file)
    except Exception as err:
        print(err)
        exit(1)


def config_php_ini(php_components, path, version):

    conf = f'{path}/config/php_config.ini'
    for component in php_components:
        ini_file = f'/etc/php/{version}/{component}/php.ini'
        print(ini_file)
        try:
            cmd = shlex.split(f'sed -i -f {conf} {ini_file}')
            subprocess.run(cmd)
        except Exception as err:
            print(err)
            sys.exit('Opdatering af php.ini fejlede')
        else:
            print(f'{ini_file} er opdateret')


def config_php_fpm(version):
    fpm_pool = f"/etc/php/{version}/fpm/pool.d/www.conf"
    platform = "env[PLATFORM] = VAGRANT"
    addLine(fpm_pool, platform)
    print(f'{fpm_pool} er opdateret')
    cmd = shlex.split(f'systemctl restart php{version}-fpm')
    subprocess.run(cmd)
    print('genstartede php-fpm')
