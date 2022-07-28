import logging

# Создаем логгер
logger = logging.getLogger()

# Пишем логи и в консоль и в файл
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log.txt", encoding='utf-8')

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Задаем формат логов
logging_format = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
console_handler.setFormatter(logging_format)
file_handler.setFormatter(logging_format)

# Выставляем уровень логирования
logger.setLevel('INFO')
