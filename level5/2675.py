t = int(input())

for _ in range(t):
    r, s = input().split()
    num = int(r)
    p = ''
    for i in range(len(s)):
        p = p + (s[i]*num)
    print(p)
