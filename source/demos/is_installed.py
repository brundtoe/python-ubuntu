import os, sys, shlex, subprocess
import re


try:
    cmd = shlex.split('VBoxManage --version')
    res = subprocess.run(cmd, stdout=subprocess.PIPE)
    version = re.search('^\d{1,}\.\d{1,}\.\d{1,}',res.stdout.decode('utf-8'))

    print('Python regexp',version.group(0))

    # todo awk fungerer kun når der anvendes single gnyffer
    # awk fungerer ikke med \d i stedet skal digits defineres som [0-9]

    awkcmd = "VBoxManage --version |  awk -Fr '{print $1}'"
    # næste linje fungerer kun direkte i terminalen
    #awkcmd = "VBoxManage --version |  awk 'BEGIN{ FS="r"} { print $1}'"
    awkres = subprocess.run(awkcmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if awkres.stderr:
        print(awkres.stderr.decode('UTF-8'))
    else:
        awkversion = awkres.stdout.decode('UTF-8')
        print('AWK versionen', awkversion)
except Exception as err:
    print('Virtualbox er ikke installeret')