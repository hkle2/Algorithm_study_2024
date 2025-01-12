import sys

table = []
answer = 0
row, col = 0, 0

for _ in range(9):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if answer < table[i][j]:
            answer = table[i][j]
            row, col = i, j

print(answer)
print(row+1, col+1)
