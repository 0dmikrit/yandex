members = [input() for _ in range(int(input()))]
for i in range(len(members) - 1):
    for j in range(i + 1, len(members)):
        print(f"{members[i]} - {members[j]}")