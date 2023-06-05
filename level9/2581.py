m = int(input())
n = int(input())
decimal = []

for x in range(m, n+1):
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                decimal.append(x)
            break

if len(decimal) > 0:
    print(sum(decimal))
    print(min(decimal))
else:
    print(-1)