import json
import logging
import logging.config


def get_logger(name, template='default'):
    with open('/home/anton/PycharmProjects/OOP_advanced/loggers.json', "r") as json_file:
        dict_config = json.load(json_file)
        dict_config["loggers"][name] = dict_config["loggers"][template]
    logging.config.dictConfig(dict_config)
    return logging.getLogger(name)
