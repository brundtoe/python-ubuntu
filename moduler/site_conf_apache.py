# -*- coding: utf-8 -*-
#
# Apace site configuration

import os
from jinja2 import Environment, FileSystemLoader


def create_site_conf(project_path, apache_dir, tmpl, app_user):

    file_loader = FileSystemLoader(f'{project_path}/templates')
    env = Environment(loader=file_loader)

    template = env.get_template(tmpl)
    output = template.render(app_user=app_user)
    # print(output)
    outfile = f'{apache_dir}/sites-available/000-default.conf'
    with open(outfile, 'wt') as fout:
        fout.write(output)

    if os.path.exists(f'{apache_dir}/sites-enabled/000-default.conf'):
        os.unlink(f'{apache_dir}/sites-enabled/000-default.conf')
    os.symlink(f'{apache_dir}/sites-available/000-default.conf',
               f'{apache_dir}/sites-enabled/000-default.conf')
