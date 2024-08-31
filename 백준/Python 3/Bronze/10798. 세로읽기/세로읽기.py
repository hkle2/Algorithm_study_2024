import sys

boards = []
length = []
answer = ""

for n in range(5):
    s = sys.stdin.readline().strip()
    boards.append(s)
    length.append(len(s))


for i in range(max(length)):
    for j in range(len(boards)): 
        try:
            answer += boards[j][i]
        except:
            pass

print(answer)