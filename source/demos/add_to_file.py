import os
from moduler.fileOperations import isFound
# det efterfølgende skal være en funktion

def existsFile(filename):
    return 

# done: der skal tjekkes for installation af cifs-utils (se tjek install.py og tjek_which.py)
# done: der skal tjekkes for eksistensen af mount mapperne (se create_mount_folders.py)
# done: hvis mount mapperne ikke findes skal de oprettes (se create_mount_folders.py)
# todo: skal kunne tilføje
# todo: der skal også logges
# todo: der skal også være unittest
# todo: skal der anvendes try catch?

if __name__ == "__main__":
    filename = '../../infile/fstab_updated'
    #filename = '../infile/fstab_raw'
    mount_point = '//192.168.0.17/bent'

    if not os.path.exists(filename):
        print(f'Filen {filename} findes ikke')
        exit(1)
    if isFound(filename,mount_point):
        print(f"{mount_point} er defined in {filename}")
        exit(0)
    with open(filename,'a') as file:
        file.write(mount_point)
    print(f'filen {filename} er nu opdateret med {mount_point}')
