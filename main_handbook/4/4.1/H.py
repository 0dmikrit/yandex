def is_palindrome(n):
    if isinstance(n, int):
        n = str(n)
    if n == n[::-1]:
        return True
    return False