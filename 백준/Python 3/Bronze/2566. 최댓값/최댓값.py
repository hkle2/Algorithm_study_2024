import sys

table = []
answer = 0
r, c = 0, 0

for i in range(9):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if answer < table[i][j]:
            answer = table[i][j]
            r, c = i, j

print(answer)
print(r+1, c+1)