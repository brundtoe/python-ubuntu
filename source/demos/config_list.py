# importer fra config.ini og transformer til dictionary

from configparser import ConfigParser, ExtendedInterpolation
import os

def fetch_config(filename):
    config = ConfigParser(interpolation=ExtendedInterpolation())
    if not os.path.exists(filename):
        print(f'Kan ikke læse konfiguationsfilen {filename}')
        exit(1)
    try:
        config.read(filename)
    except Exception as err:
        print(err)
    return config

if __name__ == '__main__':
    filename = '../../config/config.ini'
    configs = fetch_config(filename)
    # programs = {item: conf[item] for item in conf}
    # print sectionerne
    for config in configs:
        print(config)
    # print indholdet af en sektion
    print('*' * 20)
    programs = configs['programs']
    for program in programs:
        print(program)
    print('*' * 20)
    # print værdier for en nægle i en sektion
    print(configs['php.install']['php-cgi'])