import logging
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

    # Добавляем обработчик в логгер
    logger.addHandler(console_handler)

    return logger


# Глобальный логгер
logger = setup_logger()
