def number_length(num):
    if str(num)[0] == '-':
        return len(str(num)[1::])
    return len(str(num))