from .settings import settings
import logging.config

conf = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple':{
            'format': '%(asctime)s - %(name)s - %(levelname)s: (%(message)s)',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': f'{settings.app.LOG_LEVEL}',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': f'{settings.app.LOG_LEVEL}',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'app.log',
            'mode': 'a',
        }
    },
    'loggers': {'root': {'handlers': ['console', 'file'], 'level': f'{settings.app.LOG_LEVEL}'}},
}

logging.config.dictConfig(conf)