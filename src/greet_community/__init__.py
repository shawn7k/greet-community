"""A small package that says hello."""


def greet(name: str) -> str:
    name = name.strip() or "world"
    return f"Hello, {name}!"