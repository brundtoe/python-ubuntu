#!/usr/bin/env python3
#
import os, shutil
from moduler.fileOperations import fetch_config


def homebin(user):
    """
    Opret mapperne /home/{user}/bin og /home/{user}/programs
    :param user:
    :return:
    """
    home = f'/home/{user}'
    bindir = f'{home}/bin'
    if not os.path.exists(bindir):
        os.mkdir(bindir, 0o755)
        shutil.chown(bindir, user, user)

    programsdir = f'{home}/programs'
    if not os.path.exists(programsdir):
        os.mkdir(programsdir, 0o755)
        shutil.chown(programsdir, user, user)

    shutil.copyfile('../config/.vimrc', f'{home}/.vimrc')

    dstdir = f'/home/{user}/bin/images'
    srcdir = '../images'
    if not os.path.exists(dstdir):
        shutil.copytree(srcdir, dstdir)


if __name__ == '__main__':
    filename = '../config/config.ini'
    configs = fetch_config(filename)
    user = configs['Common']['user']
    homebin(user)
