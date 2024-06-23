# logging_config.py
import logging.config
import os
from logging.handlers import RotatingFileHandler, SysLogHandler
from logstash_async.handler import AsynchronousLogstashHandler

# Advanced Logging Configuration with Rotating File Handler, SysLog Handler, and Logstash Handler
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'logstash': {
            'format': '%(message)s',
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
        'syslog_handler': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': 'LOCAL0',
            'formatter': 'default'
        },
        'logstash_handler': {
            'class': 'logstash_async.handler.AsynchronousLogstashHandler',
            'host': 'logstash.example.com',
            'port': 5000,
            'formatter': 'logstash'
        }
    },
    'loggers': {
        'pinet_manager': {
            'level': 'DEBUG',
            'handlers': ['file_handler', 'syslog_handler', 'logstash_handler']
        }
    }
})
