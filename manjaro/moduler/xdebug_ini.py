#!/usr/bin/env python3
#

from jinja2 import Environment, FileSystemLoader
from fileOperations import fetch_config


def create_xdebug_ini(tmpl, dstfile, xdebug_host=True):
    """
    generer Xdebug.ini
    :param tmpl: den anvendte Jinja2 template
    :param dstfile: destination for xdebug.ini
    :param xdebug_host: angivelse af om det er en host eller en vagrant maskine
    :return: void
    """
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)

    template = env.get_template(tmpl)

    xdebug_remote = 'xdebug.remote_host=localhost'
    if not xdebug_host:
        xdebug_remote = 'xdebug.remote_connect_back=1'

    output = template.render(xdebug_remote=xdebug_remote)
    print(output)
    with open(dstfile, 'wt') as fout:
        fout.write(output)


if __name__ == '__main__':
    tmpl = 'xdebug.jinja'
    xdebug_host = fetch_config('../../config/manjaro.ini')['Common'].getboolean('xdebug-host')
    create_xdebug_ini(tmpl, xdebug_host)
