def answer(func):
    def inner(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"
    return inner