n, m = map(int, input().split())
array = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i,j+1,1):
        array[x-1] = k

for i in range(n):
    print(array[i], end=' ')