import configparser

path = 'cfg.ini'
server_section = 'SERVER'
token_field = 'TOKEN'


def read_configuration():
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg


def get_token():
    return read_configuration()[server_section][token_field]
