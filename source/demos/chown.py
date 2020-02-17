import shutil
import os
import subprocess
from os.path import join, getsize

# res = subprocess.run(['chown','-R','bent:bent','/home/bent/programs'])

user = 'bent'
for root, dirs, files in os.walk('/home/bent/programs/FreeFileSync'):
    for momo in dirs:
        dirname = os.path.join(root, momo)
        shutil.chown(dirname, user, user)
    for file in files:
        filename = os.path.join(root, file)
        shutil.chown(filename, user, user)
