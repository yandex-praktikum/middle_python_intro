"""Greetings generator."""


def greeting(name: str) -> str:
    """Return greeting text. All name parts must be capitalized.

    Args:
        name: User's name

    Returns:
        str: Greeting text
    """
    name = name.title()
    return 'Привет, {0}'.format(name)
