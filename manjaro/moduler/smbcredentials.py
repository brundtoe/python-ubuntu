#!/usr/bin/env python3
#
import sys, os, shutil
import argparse
from moduler.fileOperations import fetch_config


def smbcredentials(user, password):
    """
    Opdatering af password tiæ brug ved etablering af forbindelse til wdmycloud
    :param user: brugernavn
    :param password: det anvendte password
    :return:
    """
    text = f'user={user}\npassword={password}\n'
    filename = f'/home/{user}/.smbcredentials'
    with open(filename, 'w') as fout:
        fout.write(text)
    shutil.chown(filename, user, user)
    os.chmod(filename, 0o600)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-pwd', type=str, help='Character to multiply', default='',
                        dest='password')
    args = parser.parse_args()

    if not args.password:
        sys.exit('Der skal overføres et password')

    filename = '../../config/manjaro.ini'
    user = fetch_config(filename)['Common']['user']
    smbcredentials(user, args.password)
