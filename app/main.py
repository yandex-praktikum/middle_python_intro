"""Greetings generator."""


def greeting(name: str) -> str:
    """Return greeting text. All name parts must be capitalized.

    Args:
        name: User's name

    Returns:
        str: Greeting text
    """
    name_parts = name.split(' ')
    name = ' '.join((part.capitalize() for part in name_parts))
    return 'Привет, {0}'.format(name)
