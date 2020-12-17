#!/usr/bin/env python3
#
import os, shutil

def homebin(user):
    """
    Opret mapperne /home/{user}/bin /home/{user}/programs
    /home/{user}/.local/bin
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

    local_bindir = f'{home}/.local/bin'
    if not os.path.exists(local_bindir):
        os.mkdir(local_bindir, 0o755)
        shutil.chown(local_bindir, user, user)

    dstdir = f'/home/{user}/bin/images'
    srcdir = '../images'
    if not os.path.exists(dstdir):
        shutil.copytree(srcdir, dstdir)
        shutil.chown(dstdir, user, user)

    dst_alias = f'/home/{user}/.bash_aliases'
    src_alias = '../config/.bash_aliases'
    if not os.path.exists(dst_alias):
        shutil.copy(src_alias, dst_alias)
        shutil.chown(dst_alias, user, user)

    dstvimrc = f'/home/{user}/.vimrc'
    srcvimrc = '../config/.vimrc'
    if not os.path.exists(dstvimrc):
        shutil.copy(srcvimrc, dstvimrc)
        shutil.chown(dstvimrc, user, user)

    dstvimrc = f'/home/{user}/.tmux.conf'
    srcvimrc = '../config/.tmux.conf'
    if not os.path.exists(dstvimrc):
        shutil.copy(srcvimrc, dstvimrc)
        shutil.chown(dstvimrc, user, user)

    dstvimrc = f'/root/.vimrc'
    srcvimrc = '../config/.vimrc'
    if not os.path.exists(dstvimrc):
        shutil.copy(srcvimrc, dstvimrc)
        shutil.chown(dstvimrc, 'root', 'root')
