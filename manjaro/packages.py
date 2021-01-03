# -*- coding: utf-8 -*-
#
#

import sys
import shlex
import subprocess

programs = [
    'dkms',
    'linux-headers',
    'perl'
]


def install_programs(programs):
    """
    Installer et antal programmer
    :param programs: fra en configparser fra config.ini
    :return: void
    """
    for program in programs:
        pgm = programs[program]
        if not pgm:
            pgm = program
        if is_installed(pgm):
            continue
        res = install_program(pgm)
        if not res:
            sys.exit(f'Installation af {pgm} er fejlet')
        else:
            print('programmet', pgm, 'er installeret')


def is_installed(program):
    """
    Kontrol af om et program er installeret
    :param program: programnavn
    :return: True hvis installeret ellers False
    """
    cmd = shlex.split(f"pacman -Qi {program}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode == 0


def install_program(program):
    """
    Installation af et enkelt program
    :param program: programnavn
    :return: True hvis installationen er udført ellers False
    """
    cmd = shlex.split(f"pacman -Su --noconfirm {program}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode == 0


def install_packages(configs):
    programs = configs['programs']
    try:
        cmd = shlex.split('pacman -Syu --noconfirm')
        subprocess.run(cmd)
    except OSError as err:
        print(err)
        sys.exit('Systemopdatering fejlede')

    try:
        install_programs(programs)
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved installation af base software')
    else:
        print('pacman installation af base software udført')
