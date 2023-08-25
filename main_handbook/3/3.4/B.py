first_arr = input().split(", ")
second_arr = input().split(", ")
for first, second in zip(first_arr, second_arr):
    print(f"{first} - {second}")