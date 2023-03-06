"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    words = name.split(' ')
    upper_words = [word[0].upper() + word[1::] for word in words]
    return 'Привет, {0}'.format(' '.join(upper_words))
