n = int(input())
array = []

array = list(map(int, input().split()))

array.sort()
high_score = array[-1]

for i in range(n):
    array[i] = (array[i] / high_score) * 100

result = sum(array) / len(array)

print(result)