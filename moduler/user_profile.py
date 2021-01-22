# -*- coding: utf-8 -*-
#
import os
import sys
import pwd
import shutil
from moduler.fileOperations import add_line
from moduler.utilities import change_owner, copy_dir


def user_profile(configs):
    """
    Opret mapperne /home/{user}/bin /home/{user}/programs
    /home/{user}/.local/bin
    :param configs:
    :return:
    """
    user = pwd.getpwuid(1000).pw_name
    project_path = configs['Common']['project_path']
    bindir = f'/home/{user}/bin/'
    imagedir = f'{bindir}/images'
    if not os.path.exists(imagedir):
        os.makedirs(imagedir, 0o755, exist_ok=True)
        change_owner(bindir, user, user)

    programsdir = f'/home/{user}/programs'
    if not os.path.exists(programsdir):
        os.makedirs(programsdir, 0o755, exist_ok=True)
        shutil.chown(programsdir, user, user)

    local_bindir = f'/home/{user}/.local/bin'
    if not os.path.exists(local_bindir):
        os.makedirs(local_bindir, 0o755, exist_ok=True)
        shutil.chown(f'/home/{user}/.local', user, user)
        shutil.chown(local_bindir, user, user)

    src_dir = f'{project_path}/assets/images'
    image_dir = f'/home/{user}/bin/images'
    copy_dir(src_dir, image_dir, user)

    src_dir = f'{project_path}/assets/profile'
    dest_dir = f'/home/{user}'
    copy_dir(src_dir, dest_dir, user)

    copy_dir(src_dir, '/root', 'root')

    # set command prompt PS1
    try:
        user = pwd.getpwuid(1000).pw_name
        ps1 = r'PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "'
        add_line(f'/home/{user}/.bashrc', ps1)
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af bashrc med PS1')
    else:
        print(f'bashrc for {user} er  opdateret med command prompt')

    print('User profile opdateret!')
