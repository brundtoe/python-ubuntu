#!/usr/bin/env python3
import shutil
import sys, os
from moduler.fileOperations import fetch_config


# res = subprocess.run(['chown','-R','jackie:jackie','/home/jackie/programs'])
def change_owner(path, user):
    """
    Ændrer rettigheder rekursivt for et directory
    :param path: Absolut path til directory
    :param user: user som skal have rettighederne
    :return: void
    """
    try:
        for root, dirs, files in os.walk(path):
            for momo in dirs:
                dirname = os.path.join(root, momo)
                shutil.chown(dirname, user, user)
            for file in files:
                filename = os.path.join(root, file)
                shutil.chown(filename, user, user)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke ændre rettighederne')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Script skal udføres med root access')
    #
    user = fetch_config('../config/config.ini')['Common']['user']
    path = f'/home/{user}/programs'
    change_owner(path, user)
