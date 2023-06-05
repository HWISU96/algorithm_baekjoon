import sys
import time

start = time.time()

input = sys.stdin.readline

n = int(input()) - 2
x = 2
y = 1
max_num = 2

if n == -1:
    x = 1
    y = 1

for i in range(n):
    if max_num % 2 == 0:
        if max_num != y:
            x -= 1
            y += 1
        else:
            y += 1
            max_num += 1
            continue

    if max_num % 2 == 1:
        if max_num != x:
            x += 1
            y -= 1
        else:
            x += 1
            max_num +=1

print(f'x:{x}')
print(f'y:{y}')
print(f'max_num: {max_num}')

end = time.time()
print(f"{end - start:.5f} sec")