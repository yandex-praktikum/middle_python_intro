"""Генератор приветствий."""


def greeting(name: str) -> str:
    """
    Возвращает текст приветствия.

    Args:
        name (str): user's name.

    Returns:
        str: text of greeting.
    """
    return 'Привет, {0}'.format(name.title())
