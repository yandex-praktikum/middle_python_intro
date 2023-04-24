"""Генератор приветствий."""
def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        int: Текст приветствия
      """

    return 'Привет, ' + name.title()

