board = []

for row in range(9):
    row = list(map(int, input().split()))
    board.append(row)

row = 0
col = 0
max = -1

for i in range(9):
    for j in range(9):
        if board[i][j] > max:
            max = board[i][j]
            row = i+1
            col = j+1

print(max)
print(row, col)