# -*- coding: utf-8 -*-
#

# from os import path
import sys
import platform
import os

ver = platform.release()
print(ver)
print(ver[0:1] + ver[2:3])

print(platform.linux_distribution())

