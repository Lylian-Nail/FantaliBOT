import configparser

def config(filename='config/config.ini'):
    config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))
    config.read(filename)
    return config
