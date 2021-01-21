# -*- coding: utf-8 -*-
#
# Nginx site configuration

import os
from jinja2 import Environment, FileSystemLoader


def create_site_config(project_path, server_dir, tmpl, site_file, unix_socket):
    if not os.path.exists(f"{server_dir}/sites-available"):
        os.makedirs(f"{server_dir}/sites-available", 0o755, exist_ok=True)

    if not os.path.exists(f"{server_dir}/sites-enabled"):
        os.makedirs(f"{server_dir}/sites-enabled", 0o755, exist_ok=True)

    file_loader = FileSystemLoader(f'{project_path}/templates')
    env = Environment(loader=file_loader)

    template = env.get_template(tmpl)
    output = template.render(unix_socket=unix_socket)
    # print(output)
    outfile = f'{server_dir}/sites-available/{site_file}'
    with open(outfile, 'wt') as fout:
        fout.write(output)

    if os.path.exists(f'{server_dir}/sites-enabled/default'):
        os.unlink(f'{server_dir}/sites-enabled/default')
    os.symlink(f'{server_dir}/sites-available/default',
               f'{server_dir}/sites-enabled/default')
