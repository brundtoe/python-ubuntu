# -*- coding: utf-8 -*-
#

import os
from os.path import isfile, join

def copy_dir(src_dir, dest_dir, user='root'):
    onlyfiles = [f for f in os.listdir(src_dir) if isfile(join(src_dir, f))]
    for file in onlyfiles:
        src = join(src_dir, file)
        dest = join(dest_dir, file)
#        shutil.copy(src, dest)
#        shutil.chown(dest, user, user)
        print(src, dest)

copy_dir('assets/web','/var/www/html')
