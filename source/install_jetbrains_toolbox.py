# installation af Google Chrome

import sys,os, shutil
from moduler.fileOperations import download_file, fetch_config

try:
    configs = fetch_config('../config/config.ini')
    url = configs['jetbrains.toolbox']['url']
    version = configs['Common']['jetbrains-toolbox']
    user = configs['Common']['user']
    print(url)
    outfile = download_file(url)
    shutil.unpack_archive(outfile,f'/home/{user}/bin/','gztar')
    # outdir = f'/home/{user}/Downloads/jetbrains-toolbox-{version}'
    # src = f'/jetbrains-toolbox{outdir}'
    # dst = f'/home/{user}/bin/jetbrains-toolbox'
    # shutil.copyfile(src,dst)
    # os.remove(outdir)
except Exception as err:
    sys.exit('Download af jetbrains toolbox er fejlet\n',err)
else:
    print('JetBrains toolbox er downloded og pakket ud')


