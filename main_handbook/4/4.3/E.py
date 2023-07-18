def result_accumulator(func):
    s = []

    def inner(*args, method="accumulate"):
        if method == "accumulate":
            s.append(func(*args))
        if method == 'drop':
            s.append(func(*args))
            res = s.copy()
            s.clear()
            return res
    return inner
