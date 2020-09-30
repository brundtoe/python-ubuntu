#!../venv/bin/python
# Installation af Composer, konfiguration af XDebug

import sys, os, shutil, shlex
import subprocess
from moduler.fileOperations import fetch_config
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
    programs = configs['php.install']
    options = configs['Common']['install_options']
    install_programs(programs, options)

    print('Installation af Composer')
    url = configs['composer']['repo']
    sha256url = configs['composer']['sha256']
    user = configs['Common']['user']
    install_composer(url, sha256url, user)

    print('konfiguration af XDebug')
    version = configs['Common']['php-version']
    xdebug_host = configs['Common']['xdebug-host']
    dstfile = f'/etc/php/{version}/mods-available/xdebug.ini'
    create_xdebug_ini('xdebug.jinja', dstfile,xdebug_host)

    print('Konfiguration af php.ini')
    php_components = ['cli', 'cgi', 'fpm']
    version = configs['Common']['php-version']
    config_php_ini(php_components, version)

def install_composer(url, sha256url, user):
    composerfile = '../outfile/composer'
    try:
        fetch_file(url, composerfile)
    except Exception as err:
        print(err)
        exit(1)
    else:
        # Der skal være to mellemrum før composer.phar
        composer_hash = f'{hash_file(composerfile)}  composer.phar'

    sha256file = '../outfile/composerSha256'
    sha256sum = ''
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

    ## kopier til /home/{user}/bin
    dest = f'/home/{user}/bin/composer'
    shutil.copy(composerfile, dest)
    os.chmod(dest, 0o755)
    shutil.chown(dest, user, user)

def config_php_ini(php_components, version):

    for component in php_components:
        ini_file = f'/etc/php/{version}/{component}/php.ini'
        print(ini_file)
        conf = '../config/php_config.ini'
        try:
            cmd = shlex.split(f'sed -i -f {conf} {ini_file}')
            res = subprocess.run(cmd)
        except Exception as err:
            print(err)
            sys.exit('Opdatering af php.ini fejlede')
        else:
            print(f'{ini_file} er opdateret')

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../config/config.ini'
    configs = fetch_config(filename)

    try:
        install_php(configs)
    except Exception as err:
        print('Der opstod fejl ved installation af php')
        print(err)
        sys.exit(1)
    else:
        print('PHP installation og konfiguration er udført')
