import os, shutil
from moduler.fileOperations import fetch_config
def homebin(user):
    bindir = f'/home/{user}/bin'
    if not os.path.exists(bindir):
        os.mkdir(bindir,0o755)
        shutil.chown(bindir,user,user)

if __name__ == '__main__':
    filename = '../config/config.ini'
    configs = fetch_config(filename)
    user = configs['Common']['user']
    homebin(user)