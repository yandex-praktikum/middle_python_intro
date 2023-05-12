"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

        Args:
            name: Имя пользователя

        Returns:
            str: Текст приветствия
    """
    name = name.title()
    return 'Привет, {name}'.format(name=name)
