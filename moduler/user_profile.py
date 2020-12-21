#!/usr/bin/env python3
#
import os
import shutil


def userProfile(user):
    """
    Opret mapperne /home/{user}/bin /home/{user}/programs
    /home/{user}/.local/bin
    :param user:
    :return:
    """

    bindir = f'/home/{user}/bin'
    if not os.path.exists(bindir):
        os.mkdir(bindir, 0o755)
        shutil.chown(bindir, user, user)

    programsdir = f'/home/{user}/programs'
    if not os.path.exists(programsdir):
        os.mkdir(programsdir, 0o755)
        shutil.chown(programsdir, user, user)

    local_bindir = f'/home/{user}/.local/bin'
    if not os.path.exists(local_bindir):
        os.mkdir(local_bindir, 0o755)
        shutil.chown(local_bindir, user, user)

    image_dir = f'/home/{user}/bin/images'
    srcdir = '../images'
    if not os.path.exists(image_dir):
        shutil.copytree(srcdir, images_dir)
        shutil.chown(image_dir, user, user)

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