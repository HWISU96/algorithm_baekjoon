array = []

for i in range(10):
    num = int(input())
    reward = (num%42)
    array.append(reward)

A = list(set(array))

print(len(A))