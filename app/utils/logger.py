import sys
import logging
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