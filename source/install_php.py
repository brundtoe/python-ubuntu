# Installation af Composer, konfiguration af XDebug

import sys, os, shutil
from fileinput import FileInput
from moduler.fileOperations import fetch_config
from moduler.sha256sum import hash_file
from install_programs import install_programs
from moduler.download_file import fetch_file


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


def config_xdebug(version, srcfile):
    dstdir = f'/etc/php/{version}/mods-available'
    dstfile = f'{dstdir}/xdebug.ini'
    if not os.path.exists(dstdir):
        os.makedirs(dstdir)
    try:
        res = shutil.copyfile(srcfile, dstfile)
    except Exception as err:
        print(err)
        raise Exception


def update_inifiles(php_components, version):
    print('opdatering af php.ini')
    for component in php_components:
        ini_file = f'/etc/php/{version}/{component}/php.ini'
        print(ini_file)
        if not os.path.exists(ini_file):
            continue
        try:
            with FileInput(files=ini_file, inplace=True) as fin:
                for line in fin:
                    if line.startswith(';date.timezone ='):
                        print(line.replace(';date.timezone =', 'date.time.zone = UTC'), end='')
                    elif line.startswith(';intl.error_level'):
                        print(line.replace(';intl.error_level', 'intl.error_level'), end='')
                    else:
                        print(line, end='')
        except Exception as err:
            print('Opdatering af php.ini er fejlet')
            exit(1)


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../config/config.ini'
    configs = fetch_config(filename)

    try:
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
        srcfile = '../config/xdebug.ini'
        config_xdebug(version, srcfile)
        # todo se install_php-ini.py for manglende funktionalitet
        print('Opdatering af php.ini filerne')
        php_components = ['cli', 'cgi', 'fpm']
        version = configs['Common']['php-version']
        update_inifiles(php_components, version)
    except Exception as err:
        print('Der opstod fejl ved installation af php')
        print(err)
        sys.exit(1)
    else:
        print('PHP installation og konfigruation er udført')
