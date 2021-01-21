# -*- coding: utf-8 -*-
# linux os utilities
#
import os
from os.path import isfile, join
import sys
import shlex
import shutil
import subprocess


def get_username(user_id):
    cmd = shlex.split(f'id -un {user_id}')
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode:
        raise Exception
    else:
        return res.stdout.decode('UTF-8')[0:-1]


def is_active(service):
    cmd = shlex.split(f'systemctl is-active {service}')
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'service {service} is: {res.stdout.decode("UTF - 8")}')
    return res.stdout.decode('UTF-8')[0:-1]


def service_action(action, service):
    cmd = shlex.split(f'systemctl {action} {service}')
    res = subprocess.run(cmd)
    return res.returncode == 0


def change_owner(path, user, group):
    """
    Ændrer rettigheder rekursivt for et directory
    :param path: Absolut path til directory
    :param user: user som skal have rettighederne
    :return: void
    """
    shutil.chown(path, user, group)
    try:
        for root, dirs, files in os.walk(path):
            for momo in dirs:
                dirname = os.path.join(root, momo)
                shutil.chown(dirname, user, group)
            for file in files:
                filename = os.path.join(root, file)
                shutil.chown(filename, user, group)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke ændre rettighederne')


def copy_dir(src_dir, dest_dir, user='root'):
    onlyfiles = [f for f in os.listdir(src_dir) if isfile(join(src_dir, f))]
    for file in onlyfiles:
        src = join(src_dir, file)
        dest = join(dest_dir, file)
        shutil.copy(src, dest)
        shutil.chown(dest, user, user)
