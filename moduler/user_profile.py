# -*- coding: utf-8 -*-
#
import os
from os.path import isfile, join

import sys
import shutil
from moduler.fileOperations import addLine


def user_profile(configs):
    """
    Opret mapperne /home/{user}/bin /home/{user}/programs
    /home/{user}/.local/bin
    :param configs:
    :return:
    """
    user = configs['Common']['user']
    path = configs['Common']['path']
    bindir = f'/home/{user}/bin/'
    imagedir = f'{bindir}/images'
    if not os.path.exists(imagedir):
        os.mkdirs(imagedir, 0o755)
        shutil.chown(bindir, user, user)
        shutil.chown(imagedir, user, user)

    programsdir = f'/home/{user}/programs'
    if not os.path.exists(programsdir):
        os.mkdir(programsdir, 0o755)
        shutil.chown(programsdir, user, user)

    local_bindir = f'/home/{user}/.local/bin'
    if not os.path.exists(local_bindir):
        os.mkdir(local_bindir, 0o755)
        shutil.chown(local_bindir, user, user)

    image_dir = f'/home/{user}/bin/images'
    srcdir = f'{path}/assets/images'

    onlyfiles = [f for f in os.listdir(srcdir) if isfile(join(srcdir, f))]
    for file in onlyfiles:
        src = join(srcdir, file)
        dest = join(image_dir, file)
        shutil.copy(src, dest)
        shutil.chown(dest, user, user)

    srcdir = f'{path}/assets/profile'
    destdir = f'/home/{user}'

    onlyfiles = [f for f in os.listdir(srcdir) if isfile(join(srcdir, f))]
    for file in onlyfiles:
        src = join(srcdir, file)
        dest = join(destdir, file)
        shutil.copy(src, dest)
        shutil.chown(dest, user, user)

    shutil.copytree(srcdir, destdir, dirs_exist_ok=True)

    # set command prompt PS1
    try:
        user = configs['Common']['user']
        ps1 = r'PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "'
        addLine(f'/home/{user}/.bashrc', ps1)
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af bashrc med PS1')
    else:
        print(f'bashrc for {user} er  opdateret med command prompt')

    print('User profile opdateret!')
