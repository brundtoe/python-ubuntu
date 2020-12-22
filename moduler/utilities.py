# -*- coding: utf-8 -*-
# linux os utilities
#
import shlex
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
    res = subprocess.run(cmd,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'service {service} is: {res.stdout.decode("UTF - 8")}')
    return res.stdout.decode('UTF-8')[0:-1]


def service_action(action, service):
    cmd = shlex.split(f'systemctl {action} {service}')
    res = subprocess.run(cmd)
    return res.returncode == 0
