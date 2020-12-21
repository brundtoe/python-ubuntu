#!/usr/bin/env python3
# -*- coding: utf-8 -*-import sys
#
import sys, os, shlex
import subprocess
from moduler.fileOperations import fetch_config


def is_installed(program):
    """
    Kontrol af om et progrma er installeret
    :param program: programnavn
    :return: True hvis installeret ellers False
    """
    cmd = shlex.split(f"dpkg -s {program}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode == 0


def install_program(program, options):
    """
    Installation af et enkelt program
    :param program: programnavn
    :param options: optioner
    :return: True hvis installationen er udført ellers False
    """
    cmd = shlex.split(f"apt install {options} {program}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode == 0


def install_programs(programs, options):
    """
    Installer et antal programmer
    :param programs: fra en configparser fra config.ini
    :param options: installationsoptioner fra config.ini
    :return: void
    """
    for program in programs:
        pgm = programs[program]
        if not pgm:
            pgm = program
        if is_installed(pgm):
            continue
        res = install_program(pgm, options)
        if not res:
            sys.exit(f'Installation af {pgm} er fejlet')
        else:
            print('programmet', pgm, 'er installeret')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scritet skal udføres  med root access')
    print('script install_programs')
    configs = fetch_config('../config/config.ini')
    programs = configs['programs']
    options = configs['Common']['install_options']
    install_programs(programs, options)
