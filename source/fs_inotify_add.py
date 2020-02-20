#!/usr/bin/env python3
import sys, os
from moduler.fileOperations import addLine

"""
Scriptet tilføjer fs.inotify.max_user_watches til 99-local.conf 
"""
if __name__ == "__main__":
    if os.geteuid() != 0:
        print('Scriptet skal udføres med root access')
        exit(2)

    try:
        filename = '/etc/sysctl.d/99-local.conf'
        text = 'fs.inotify.max_user_watches=524288\n'
        addLine(filename, text)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke tilføje linje til {filename}')
