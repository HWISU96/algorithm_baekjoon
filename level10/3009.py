x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

if x_list[0] != x_list[1] and x_list[0] != x_list[2]:
    x = x_list[0]
elif x_list[1] != x_list[0] and x_list[1] != x_list[2]:
    x = x_list[1]
else:
    x = x_list[2]

if y_list[0] != y_list[1] and y_list[0] != y_list[2]:
    y = y_list[0]
elif y_list[1] != y_list[0] and y_list[1] != y_list[2]:
    y = y_list[1]
else:
    y = y_list[2]

print(x, y)