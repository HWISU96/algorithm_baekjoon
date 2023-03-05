array = []
n, m = map(int, input().split())

for i in range(n):
    array.append(i+1)

for _ in range(m):
    i, j = map(int, input().split())
    array[i-1:j] = array[i-1:j][::-1]

print(*array)