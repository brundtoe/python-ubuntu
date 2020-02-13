# tjek for installation
import sys, os, shlex
import subprocess
from moduler.fileOperations import fetch_config

def is_installed(program):
    cmd = shlex.split(f"dpkg -s {program}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode is 0

def install_program(program, options):
    """Installation af et enkelt program"""
    cmd = shlex.split(f"apt install {options} {program}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return res.returncode is 0

def install_programs(programs, options):
    for program in programs:
        if is_installed(program):
            continue
        pgm = programs[program]
        if not pgm:
            pgm = program
        res = install_program(pgm, options)
        if not res:
            raise Exception
            sys.exit(f'Installation af {program} er fejlet')
        else:
            print('programmet', program, 'er installeret - returkode')

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scritet skal udføres  med root access')
    print('script install_programs')
    configs = fetch_config('../config/config.ini')
    programs = configs['programs']
    options = configs['Common']['install_options']
    install_programs(programs,options)