import sys
import subprocess
from moduler.fileOperations import download_file

def install_repo(url, program, content):

    try:
        repokey_install(url)
    except Exception as err:
        sys.exit(f'Repository key for {program} kan ikke installeres')

    try:
        sources_list_update(program, content)
    except Exception as err:
        sys.exit(f'/etc/apt/sources.list.d/{program} kan ikke opdateres med {content}')

def repokey_install(url):
    try:
        key_file = download_file(url)
        if not key_file:
            raise Exception
    except Exception as err:
        raise Exception
    try:
        subprocess.run(['apt-key','add', key_file],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as err:
        raise Exception

def sources_list_update(program, content):
    outfile = f'/etc/apt/sources.list.d/{program}.list'
    with open(outfile, 'w') as fout:
        fout.write(content)
        fout.write('\n')