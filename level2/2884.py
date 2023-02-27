h , m = map(int, input().split())

if m >= 45:
    m = m-45
elif h != 0 and m < 45:
    h = h-1
    m = m+15
elif h == 0 and m < 45:
    h = h+23
    m = m+15

print(h,m)
