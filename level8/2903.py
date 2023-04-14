n = int(input())
dot = 2

for i in range(n):
    dot += dot - 1

print(dot**2)