t1 = int(input())
t2 = int(input())
t3 = int(input())

if t1 == 60 and t2 == 60 and t3 == 60:
    print('Equilateral')
elif t1 + t2 + t3 == 180 and t1 == t2 or t1 == t3 or t2 == t3:
    print('Isosceles')
elif t1 + t2 + t3 == 180 and t1 != t2 != t3:
    print('Scalene')
else:
    print('Error')