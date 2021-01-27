# -*- coding: utf-8 -*-
#
import os
import sys
import subprocess
import shlex
import re
import platform
from moduler.configuration import get_config

project_path = os.path.dirname(os.path.realpath(__file__))
filename = 'config/config.ini'
configs = get_config(project_path, filename)

host = configs['Common']['hostname']
hostnames = configs['hostnames']
print(configs['Common']['virtualization'])

