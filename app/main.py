"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

        Args:
            name: Имя пользователя

        Returns:
            str: Текст приветствия
    """
    name = name.split(' ')
    name = [word.capitalize() for word in name]
    str_ = ' '.join(name)
    return 'Привет, {str_}'.format(str_=str_)
