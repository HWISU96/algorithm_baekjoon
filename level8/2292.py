n = int(input())
room = 1
count = 1

while n != 1:
    for i in range(1, n + 1):
        room += 6 * i
        count += 1
        if n <= room:
            break
    break

print(count)