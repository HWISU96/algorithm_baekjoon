a , b = map(int, input().split())
c = int(input())

A = 0
B = 0

mok = 0
na = 0

if (b + c) // 60 == 0:
    A = a
    B = (b+c)

if (b + c) // 60 > 0:
    mok = (b+c) // 60
    na = (b+c) % 60
    A = a + mok
    B = na
    if A >= 24:
        A = A-24

print(A, B)