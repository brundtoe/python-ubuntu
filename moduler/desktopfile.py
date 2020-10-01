#!/usr/bin/env python3
import sys
from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config


def create_desktop_file(program, tmpl, user, version = None):
    """
    Opret en desktop fil på baggrund af en Jinja template
    :param program: Programmet som skal have en desktop file
    :param tmpl:    Den anvendte template
    :param user:    user konto hvor desktop file skal placeres
    :return:        void
    """
    try:
        file_loader = FileSystemLoader('../templates')
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

if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    programs = configs['desktop.items']
    user = configs['Common']['user']
    for item in programs:
        program = programs[item]
        tmpl = f'{program}.jinja'
        create_desktop_file(program, tmpl, user)
