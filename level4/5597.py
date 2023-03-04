array = []
for i in range(30):
    array.append(i+1)

for _ in range(28):
    num = int(input())
    array.remove(num)

array.sort()

for i in range(2):
    print(array[i])