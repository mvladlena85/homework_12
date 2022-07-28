import logging

logger = logging.getLogger()
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log.txt", encoding='utf-8')

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logging_format = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
console_handler.setFormatter(logging_format)
file_handler.setFormatter(logging_format)
logger.setLevel('INFO')
