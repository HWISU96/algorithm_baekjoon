coin = [25, 10, 5, 1]
t = int(input())

for _ in range(t):
    c = int(input())  # 124
    for i in coin:
        print(c // i, end=' ')
        c = c % i

