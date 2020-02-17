# installation af Postman

from moduler.fileOperations import fetch_config, fetch_archive


def install_postman(configs):

    url = configs['postman.com']['url']
    user = configs['Common']['user']
    program = 'Postman'
    version = configs['Common']['postman']
    fetch_archive(url,user,program,version)



