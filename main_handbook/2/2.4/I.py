n = int(input())
nums = []
while n > 0:
    nums.append(max(i for i in input()))
    n -= 1
print("".join(nums))