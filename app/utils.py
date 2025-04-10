import re

def camel_to_snake(name: str) -> str:
    """
    Преобразует строку из camelCase в snake_case.
    :param name: строка в camelCase.
    :return: строка в snake_case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def transform_keys(data: dict) -> dict:
    """
    Преобразует ключи словаря из camelCase в snake_case.
    :param data: словарь с ключами в camelCase.
    :return: словарь с ключами в snake_case.
    """
    return {camel_to_snake(k): v for k, v in data.items()}