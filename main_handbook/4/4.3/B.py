def recursive_digit_sum(n):
    if len(str(n)) > 1:
        return recursive_digit_sum(int(str(n)[:-1])) + int(str(n)[-1])
    return int(str(n)[0])
