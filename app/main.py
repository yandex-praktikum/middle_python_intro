"""Генератор приветствий."""
import logging


def greeting(name: str) -> str:
    """Вернуть текст приветствия.

    Args:
        name: Имя пользователя.

    Returns:
        str: Текст приветствия.
    """
    name = name.title()
    logging.info(name)
    return 'Привет, {name}'.format(name=name)
