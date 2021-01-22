# -*- coding: utf-8 -*-
#

import pwd
from moduler.utilities import is_active, service_action


def flip_server(configs):
    print("Flip http webserver")
    user_name = pwd.getpwuid(1000).pw_name
    try:
        if user_name == 'www-data':
            service = 'apache2'
        else:
            print('else')
            service = 'httpd'
        status = is_active(service)
        print(f'Apache status: {status}.')
        if status == 'active':
            service_action('stop', service)
            service_action('start', 'nginx')
            print('apache2 standses og nginx startes')
        else:
            service_action('stop', 'nginx')
            service_action('start', service)
            print('Nginx standses og apache2 startes')
    except Exception as err:
        print(err)
        print('Flip server fejlede')
