# -*- coding: utf-8 -*-
#
#
import os
import shlex
from subprocess import run


def install_mongodb(configs):
    if os.geteuid() == 0:
        print('MongoDB kan ikke installeres med root access')
        return

    distro = configs['Common']['distribution']
    if distro == 'ubuntu':
        print('På Ubuntu skal installationen foretages fra systemmenuen')
        return

    if os.path.exists('/lib/systemd/system/mongodb.service'):
        print('MongoDB er allerede installereet')
    #    return

    cmd = shlex.split('sudo pacman -Syu --needed base-devel')
    res = run(cmd)
    if res.returncode != 0:
        print('Systemopdatering fejlede')
        return

    build_dir = '/tmp/build'
    if not os.path.exists(build_dir):
        os.makedirs(build_dir, 0o755, exist_ok=True)
    
    mongo_bin_dir = f'{build_dir}/mongodb-bin'
    if not os.path.exists(mongo_bin_dir):
        os.makedirs(mongo_bin_dir, 0o755, exist_ok=True)
        cmd = shlex.split(f'git clone https://aur.archlinux.org/mongodb-bin.git {mongo_bin_dir}')
        res = run(cmd)
        if res.returncode !=0:
            print('cloning af mongodb-bin fejlede')

    mongo_tools_dir = f'{build_dir}/mongodb-tools-bin'
    if not os.path.exists(mongo_tools_dir):
        os.makedirs(mongo_bin_dir, 0o755, exist_ok=True)
        cmd = shlex.split(f'git clone https://aur.archlinux.org/mongodb-tools-bin.git {mongo_tools_dir}')
        res = run(cmd)
        if res.returncode !=0:
            print('cloning af mongodb-tools-bin fejlede')

    old_dir =os.getcwd()
    os.chdir(mongo_bin_dir)
    res = run(['makepkg', '-si'])
    os.chdir(old_dir)

    old_dir =os.getcwd()
    os.chdir(mongo_tools_dir)
    res = run(['makepkg', '-si'])
    os.chdir(old_dir)

    cmd = shlex.split('sudo systemctl enable mongodb')
    res = run(cmd)

    cmd = shlex.split('sudo systemctl start mongodb')
    res = run(cmd)
    