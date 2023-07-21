lines = set()


def modern_print(s):
    if s not in lines:
        lines.add(s)
        print(s)

