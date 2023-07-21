def to_string(*items, sep=" ", end="\n"):
    line = ""
    for i in items[:-1]:
        line += str(i) + sep
    line += str(items[-1]) + end
    return line