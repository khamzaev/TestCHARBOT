import logging
from logging.handlers import RotatingFileHandler
import sys

# Настройка логгера
def setup_logger():
    logger = logging.getLogger("telegram_bot")
    logger.setLevel(logging.DEBUG)

    # Формат логов
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Вывод в консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Вывод в файл с ротацией
    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Добавляем обработчики в логгер
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Глобальный логгер
logger = setup_logger()
