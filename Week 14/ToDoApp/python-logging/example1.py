import logging

logger = logging.getLogger('logger_sample')
logger.setLevel(logging.DEBUG)

# First Handler
file_handler = logging.FileHandler(filename='ex2.log', mode='a')
file_formatter = logging.Formatter('%(asctime)s -- %(levelname)s:%(levelno)s -- %(message)s')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.ERROR)

# Second Handler
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(name)s -- %(levelname)s -- %(message)s')
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.DEBUG)


logger.addHandler(file_handler)
logger.addHandler(console_handler)


logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')