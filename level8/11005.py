N, B = map(int, input().split())

ary = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = str()

while N != 0:
    result += ary[N % B]
    N //= B

print(result[::-1])
