"""code for logs creation"""
import configparser
import json
import logging
from logging.config import dictConfig

configParse = configparser.ConfigParser()
# make option to check as incase sensitive
configParse.optionxform = lambda option: option
configParse.read("price_optimization_tool/config.ini")

LOGGING_CONFIG = json.loads(configParse['log_conf']['logging_config'])
dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(name='rest_log')
