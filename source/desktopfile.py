from jinja2 import Environment, FileSystemLoader
from moduler.fileOperations import fetch_config

def create_desktop_file(program, tmpl, user):
    """
    Opret en desktop fil på baggrund af en Jinja template
    :param program: Programmet som skal have en desktop file
    :param tmpl:    Den anvendte template
    :param user:    user konto hvor desktop file skal placeres
    :return:        void
    """
    file_loader = FileSystemLoader('../templates')
    env = Environment(loader=file_loader)

    template = env.get_template(tmpl)

    outfile = f'/home/{user}/Desktop/{program}.desktop'
    output = template.render(user=user)
    print(output)
    with open(outfile,'wt') as fout:
        fout.write(output)

if __name__ == '__main__':
    #program = 'FreeFileSync'
    program = 'NoSQLBooster'
    tmpl = f'{program}.jinja'
    user = fetch_config('../config/config.ini')['Common']['user']
    create_desktop_file(program, tmpl, user)