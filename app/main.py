"""Генератор приветствий."""
import pprint

def Greeting(name: str) -> str:
      """Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Retu
          int: Текст приветствия
      """
      pprint.pprint(name.lower())
      return 'Привет, name'
