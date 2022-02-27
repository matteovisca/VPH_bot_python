import os
import platform
from dotenv import load_dotenv

if platform.platform().__contains__('macOS'):
    print("Esecuzione su MAC!")
    load_dotenv('.env.local')
else:
    load_dotenv()

class Config(object):
    ###########################
    ##   TELEGRAM SETTINGS  ##
    ##########################
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    DEFAULT_WELCOME = os.environ.get('TG_DEFAULT_INIT_MESSAGE', 'Benvenuto nel bot per la generazione dei Report! ')
    ##########################
    ##   PROJECT SETTINGS   ##
    ##########################
    CLIENT = os.environ.get('CLIENT')
    PORTGRPC = os.environ.get('PORTGRPC')
    IPGRPC = os.environ.get('IPGRPC')
    ENABLE_PLUGINS = True
    DEFAULT_LANGUAGE = "EN"
    VERSION = '0.0.1'
    VERSION_NAME = 'cheyenne'
    if BOT_TOKEN is None:
        print("The environment variable TOKEN was not set correctly!")
        quit(1)
