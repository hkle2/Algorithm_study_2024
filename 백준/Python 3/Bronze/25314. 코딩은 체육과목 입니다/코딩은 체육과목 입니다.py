import sys

N = int(sys.stdin.readline().strip())

answer = ""

for i in range(N // 4):
    answer += "long "

answer += "int"
print(answer)