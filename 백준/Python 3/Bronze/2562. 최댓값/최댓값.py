import sys

answer, n = 0, 0

for i in range(1, 10):
    num = int(sys.stdin.readline().strip())
    if answer < num:
        answer = num
        n = i
        
print(answer)
print(n)