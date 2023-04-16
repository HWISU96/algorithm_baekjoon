import sys
input = sys.stdin.readline

n = int(input())
x = 1
y = 1

# for i in range(1, n+1):
#     x += i

for i in range(1, n + 1):
    x += i
    print(x)
    if n <= x:
        break
print(x)