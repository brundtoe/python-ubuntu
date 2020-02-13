import os
from moduler.fileOperations import addLine

if __name__ == "__main__":
    if os.geteuid() != 0:
        print('Scriptet skal udføres med root access')
        exit(2)
    filename = '/etc/sysctl.d/99-local.conf'
    text = 'fs.inotify.max_user_watches=524288\n'

    addLine(filename,text)
