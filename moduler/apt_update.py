#!/usr/bin/env python3
import sys, os
from subprocess import run


def apt_update():
    """
    Opdater Ubuntu
    :return: void
    """
    try:
        res_update = run(['apt-get', 'update'])
        if res_update.returncode:
            raise Exception
        res_upgrade = run(['apt-get', 'upgrade', '-y'])
        if res_upgrade.returncode:
            raise Exception
    except Exception as err:
        print(err)
        sys.exit('Kan ikke opdatere systemet')


if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')
    apt_update()
