import logging
import os

from app.configs.db_uri import SQLALCHEMY_DATABASE_URI

logger = logging.getLogger(__name__)

APP_NAME = 'edyst'
ENV = 'development'
DEBUG = True
LOG_DIR = 'logs'
SECRET_KEY = 'edyst-top-secret'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration for the python logging module
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': logging.DEBUG,
        'handlers': ['console', 'file'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': logging.DEBUG,
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': logging.DEBUG,
            'formatter': 'detailed',
            'filename':  LOG_DIR + '/' + APP_NAME.lower() + '.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        }
    },
    'formatters': {
        'detailed': {
            'format': ('%(asctime)s %(name)-17s line:%(lineno)-4d '
                        '%(levelname)-8s %(message)s')
        }
    },
}

LOG_FILENAME = LOG_DIR + '/' + APP_NAME.lower() + '.log'
if os.path.exists(LOG_FILENAME):
    logger.debug("Log file exists - using {}".format(LOG_FILENAME))
else:
    try:
        os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)
    except OSError as e:
        logger.error("Unable to create log file at {}".format(LOG_FILENAME))
        logger.info("Error: {}".format(e))
    with open(LOG_FILENAME, 'w') as f:
        logger.info("Created new log file... {}".format(LOG_FILENAME))

