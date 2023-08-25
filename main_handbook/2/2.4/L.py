n = int(input())
m = int(input())
nums = []
arr = []
for i in range(1, n * m + 1):
    arr.append(i)
    if len(arr) == m:
        nums.append(arr.copy())
        arr.clear()
[print(*k) for k in nums]
"""No release"""


