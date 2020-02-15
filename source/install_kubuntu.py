#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen -env med password til wdmycloud
#
import sys, os, shlex
from subprocess import run
from moduler.fileOperations import fetch_config

configs = ''

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

try:
    filename = '../config/config.ini'
    configs = fetch_config(filename)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

try:
    timezone = configs['Common']['timezone']
    cmd = shlex.split(f'timedatectl set-timezone {timezone}')
    res = run(cmd)
except Exception as err:
    sys.exit(f'Der opstod fejl ved set-timezone {timezone}')
else:
    print(f'timezone er sat til {timezone}')


from add_mountpoints import add_mountpoints
try:
    user = configs['Common']['user']
    mount_points = configs[configs['Common']['host']]
    add_mountpoints(user, mount_points)
except Exception as err:
    sys.exit('Der opstod fejl ved tilføjelse af mount points for interne diske')
else:
    print('Mount points for interne diske er tilføjet')

try:
    mount_points = configs['mount.points']
    user = configs['Common']['user']
    add_mountpoints(user, mount_points)
except Exception as err:
    sys.exit('Der opstod fejl ved tilføjelse af mount points for wdmycloud')
else:
    print('Mount points for wdmycloud er tilføjet')

from smbcredentials import smbcredentials
try:
    user = configs['Common']['user']
    filename = '../config/.env_develop'
    password = fetch_config(filename)['Common']['password']
    smbcredentials(user, password)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af ~/.smbcredentials')
else:
    print('~/.smbcredentials er opdateret med mountpoint')

from fstab_update import update_fstab
try:
    mount_string = configs['Common']['mount_string']
    mount_points = configs['mount.points']
    fstab = configs['etc.fstab']
    update_fstab(mount_string,mount_points,fstab)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af /etc/fstab')
else:
    print('/etc/fstab er opdateret med mountpoint')

from moduler.fileOperations import addLine
try:
    filename = '/etc/sysctl.d/99-local.conf'
    text = 'fs.inotify.max_user_watches=524288\n'
    addLine(filename, text)
except Exception as err:
    sys.exit(f'Der opstod fejl ved opdatering af {filename}')
else:
    print(f'{filename} er opdateret med {text}')

from home_bin import homebin
try:
    user = configs['Common']['user']
    homebin(user)
except Exception as err:
    sys.exit(f'Der opstod fejl ved oprettelse af /home/{user}/bin')
else:
    print(f'/home/{user}/bin er opdateret')

from apt_update import apt_update
try:
    apt_update()
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
else:
    print('apt-get update og apt-get upgrade udført')

from install_programs import install_programs
try:
    programs = configs['programs']
    options = configs['Common']['install_options']
    install_programs(programs,options)
except Exception as err:
    sys.exit('Der opstod fejl ved installation af base software')
else:
    print('apt-get installation af base software udført')

from install_repo import install_repo
try:
    url = configs['mongodb.org']['repo_key']
    program = 'mongodb'
    content = configs['mongodb.org']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

try:
    url = configs['virtualbox.org']['repo_key']
    program = 'virtualbox'
    content = configs['virtualbox.org']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

try:
    url = configs['docker.com']['repo_key']
    program = 'docker'
    content = configs['docker.com']['sources_string']
    install_repo(url, program, content)
except Exception as err:
    sys.exit(f'{program} repository er ikke installeret')
else:
    print(f'{program} repository er installeret')

from puppet_repo_install import puppet_repo
try:
    url = configs['puppetlabs.com']['repo']
    puppet_repo(url)
except Exception as err:
    print('Puppet repository er ikke installeret',err)
    sys.exit(1)
else:
    print('Puppet repository er installeret')

from nodejs_repo_install import nodejs_repo
try:
    url = configs['nodejs.org']['repo']
    nodejs_repo(url)
except Exception as err:
    print('Node.js repository er ikke installeret',err)
    sys.exit(1)
else:
    print('Node.js repository er installeret')

try:
    programs = configs['extra.programs']
    options = configs['Common']['install_options']
    install_programs(programs,options)
except Exception as err:
    sys.exit('Der opstod fejl ved installation af ekstra software')
else:
    print('apt-get installation af ekstra software udført')

from install_php import install_composer, config_xdebug, update_inifiles
try:
    print('Installation af PHP moduler')
    programs = configs['php.install']
    options = configs['Common']['install_options']
    install_programs(programs,options)

    print('Installation af Composer')
    url = configs['composer']['repo']
    sha256url = configs['composer']['sha256']
    user = configs['Common']['user']
    install_composer(url,sha256url,user)

    print('konfiguration af XDebug')
    version = configs['Common']['php-version']
    xdebug_host = configs['Common']['xdebug-host']
    srcfile = f'../config/{xdebug_host}'
    config_xdebug(version,srcfile)
    print('Konfiguration af php.ini')
    php_components = ['cli', 'cgi', 'fpm']
    version = configs['Common']['php-version']
    update_inifiles(php_components, version)
except Exception as err:
    print('Der opstod fejl ved installation af php')
    print(err)
    sys.exit(1)
else:
    print('PHP installation og konfigruation er udført')

print('*' * 50)
print('installation og konfigurations er afsluttet')
