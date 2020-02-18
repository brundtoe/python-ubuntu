from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config

def create_xdebug_ini(tmpl,xdebug_host = True):

    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)

    template = env.get_template(tmpl)

    xdebug_remote = 'xdebug.remote_host=localhost'
    if not xdebug_host:
        xdebug_remote = 'xdebug.remote_connect_back=1'

    outfile = '../config/xdebug.ini'
    output = template.render(xdebug_remote = xdebug_remote)
    print(output)
    with open(outfile,'wt') as fout:
        fout.write(output)

if __name__ == '__main__':
    tmpl = 'xdebug.jinja'
    xdebug_host = fetch_config('../config/config.ini')['Common'].getboolean('xdebug-host')
    create_xdebug_ini(tmpl, xdebug_host)