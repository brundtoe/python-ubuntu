# Opretter bin og programsdir for {user}
import os, shutil
from moduler.fileOperations import fetch_config
def homebin(user):
    home = f'/home/{user}'
    bindir = f'{home}/bin'
    if not os.path.exists(bindir):
        os.mkdir(bindir,0o755)
        shutil.chown(bindir,user,user)

    programsdir = f'{home}/programs'
    if not os.path.exists(programsdir):
        os.mkdir(programsdir,0o755)
        shutil.chown(programsdir,user,user)

    shutil.copyfile('../config/.vimrc',f'{home}/.vimrc')

if __name__ == '__main__':
    filename = '../config/config.ini'
    configs = fetch_config(filename)
    user = configs['Common']['user']
    homebin(user)