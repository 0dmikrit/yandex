arr = [*input().split(", "), *input().split(", "), *input().split(", ")]
for i, line in enumerate(sorted(arr), start=1):
    print(f"{i}. {line}")