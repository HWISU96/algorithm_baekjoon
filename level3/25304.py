x = int(input())
n = int(input())

sum_money = 0
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum_money = (a*b)
    sum += sum_money

if x == sum:
    print('Yes')
else:
    print('No')