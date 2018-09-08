import os
import sys
import logging
from flask import Flask
from logging.handlers import RotatingFileHandler
from app.config import config

log = logging.getLogger(__name__)
log.setLevel(config['global']['loglevel'])
log.propagate = False

INFO_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
DEBUG_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s [in %(pathname)s:%(lineno)d]'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'
formatter = logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(config['global']['logfile'], 'a', 1 * 1024 * 1024, 10)
file_handler.setFormatter(formatter)
log.addHandler(file_handler)

if config['global']['logconsole'] == 'True':
    log.addHandler(stream_handler)


def not_exist_makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def setup_logger(app: Flask, log_dir: str ='.'):
    app.logger.removeHandler(app.logger.handlers[0])

    formatter = logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT)
    debug_log = os.path.join(app.root_path, '../log/debug.log')
    not_exist_makedirs(os.path.dirname(debug_log))

    debug_file_handler = RotatingFileHandler(
        debug_log, maxBytes=100000, backupCount=10
    )

    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = os.path.join(app.root_path, '../log/error.log')
    not_exist_makedirs(os.path.dirname(error_log))
    error_file_handler = RotatingFileHandler(
        error_log, maxBytes=100000, backupCount=10
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

    stream_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(stream_handler)

    app.logger.setLevel(logging.DEBUG)
