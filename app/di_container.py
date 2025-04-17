from injectable import load_injection_container


# Настройка контейнера зависимостей
def configure_di():
    """
    Инициализация контейнера зависимостей.

    Загружает DI контейнер для автоматического внедрения зависимостей.
    """
    load_injection_container()

