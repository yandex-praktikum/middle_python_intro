"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
         str: Текст приветствия
    """
    return f'Привет, {name.title()}'
