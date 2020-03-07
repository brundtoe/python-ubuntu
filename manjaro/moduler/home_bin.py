#!/usr/bin/env python3
#
import os, shutil

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

    try:
        shutil.copyfile('../config/.vimrc', f'{home}/.vimrc')
    except Exception as err:
        print(err)
        sys.exit('kan ikke kopiere .vimrc')
        
    dstdir = f'/home/{user}/bin/images'
    srcdir = '../images'
    if not os.path.exists(dstdir):
        shutil.copytree(srcdir, dstdir)
