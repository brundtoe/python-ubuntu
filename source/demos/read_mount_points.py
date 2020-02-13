from configparser import ConfigParser
import os

config = ConfigParser()
filename = '../../config/config.ini'

if not os.path.exists(filename):
    print(f'kan ikke læse filen {filename}')
    exit(1)
config.read(filename)
print(config.get('mount_points', 'gitdepot'))
mount_points = config['mount_points']
print(mount_points['gitdepot'])
for key in config['mount_points']:
    print(key, config['mount_points'][key])
