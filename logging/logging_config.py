# logging_config.py
import logging.config
import os
from logging.handlers import RotatingFileHandler

# Advanced Logging Configuration with Rotating File Handler
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.getcwd(), 'logs', 'pinet_manager.log'),
            'maxBytes': 1024*1024*5,  # 5MB
            'backupCount': 5,
            'formatter': 'default'
        },
        'console_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'pinet_manager': {
            'level': 'DEBUG',
            'handlers': ['file_handler', 'console_handler']
        }
    }
})
