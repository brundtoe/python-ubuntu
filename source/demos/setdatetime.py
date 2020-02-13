import subprocess
import shlex

cmd = shlex.split('timedatectl set-timezone Europe/Copenhagen')
#cmd = shlex.split('timedatectl set-timezone UTC')
res = subprocess.run(cmd)