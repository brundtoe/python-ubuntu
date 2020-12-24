# -*- coding: utf-8 -*-
#
import sys
from jinja2 import Environment, FileSystemLoader


def create_desktop_file(program,project_path, tmpl, user, version = None):
    """
    Opret en desktop fil på baggrund af en Jinja template
    :param program: Programmet som skal have en desktop file
    :param tmpl:    Den anvendte template
    :param user:    user konto hvor desktop file skal placeres
    :return:        void
    """
    try:
        file_loader = FileSystemLoader(f'{project_path}/templates')
        env = Environment(loader=file_loader)

        template = env.get_template(tmpl)

        outfile = f'/home/{user}/Desktop/{program}.desktop'
        output = template.render(user=user, version=version)
        # print(output)
        with open(outfile, 'wt') as fout:
            fout.write(output)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke generere desktopfile for {program}')

