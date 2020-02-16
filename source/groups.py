# adding user to groups
# adduser and usermod results in the same result
# exception is raised when group or user does not exist
# jf. stackoweerflow så er det via subrpocess

import sys, os, shlex, subprocess
from moduler.fileOperations import fetch_config
def adduser(user, group):

    cmd =  shlex.split(f'adduser {user} {group}')
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode:
            raise Exception
    except Exception as err:
        print()
        sys.exit(res.stderr.decode('UTF-8'))
    print(res.stdout.decode('UTF-8'))

def usermod(user,group, options = ''):
    cmd = shlex.split(f'usermod {options} -G {group} -a {user}')
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode:
            raise Exception
    except Exception as err:
        print()
        sys.exit(res.stderr.decode('UTF-8'))
    print(res.stdout.decode('UTF-8'))

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('scriptet skal udføres med root adgang')

    user = fetch_config('../config/config.ini')['Common']['user']
    group = 'docker'
    ##add user to existing group
    adduser(user,'cdrom')
    # add user og gruppe
    usermod(user,group)





