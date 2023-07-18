num = int(input())
digits = [int(d) for d in str(num)]
min_digit = min(digits)
max_digit = max(digits)
sum_min_max = min_digit + max_digit
remaining_digit = sum(digits) - sum_min_max
if remaining_digit * 2 == sum_min_max:
    print('YES')
else:
    print('NO')