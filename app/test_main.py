"""Тесты генератора приветствий."""

import pytest

from main import greeting


@pytest.mark.parametrize(
    'name,expected',
    [('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга')],
)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени.

    Args:
        name: Имя пользователя
        expected: Ожидаемый текст приветствия
    """
    assert greeting(name) == expected


def test_capitalize():
    """Все слова в имени начинаются с большой буквы."""
    name = 'яндекс практикум'
    assert greeting(name) == 'Привет, Яндекс Практикум'
